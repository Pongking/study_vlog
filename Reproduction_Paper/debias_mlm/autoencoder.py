import regex as re
import argparse
import nltk
import torch
from transformers import *

# import numpy
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_digits

# class Autoencoder:
#     def __init__(self,
                 
#                  )
def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',type=str,required=True,help='Data')
    parser.add_argument('--attributes',type=lambda x:list(x.split(',')),required=True)
    parser.add_argument('--stereotypes',type=str)
    parser.add_argument('--output',type=str,required=True)
    parser.add_argument('--block_size',type=int,default=128)
    parser.add_argument('--seed',type=int,default=12)
    parser.add_argument('--model_type',type=str,required=True,
                        choices=['bert','roberta','electra', 'albert', 'dbert'])
    
    args=parser.parse_args()
    return args

def prepare_transformer(args):
    current_path='./model/'
    if args.model_type=='bert':
        pretrained_weights=current_path+'bert-base-uncased'
        model=BertModel.from_pretrained(pretrained_weights)
        tokenizer=BertTokenizer.from_pretrained(pretrained_weights)
    elif args.model_type=='roberta':
        pretrained_weights = current_path+'roberta'
        model = RobertaModel.from_pretrained(pretrained_weights)
        tokenizer = RobertaTokenizer.from_pretrained(pretrained_weights)
    elif args.model_type == 'albert':
        pretrained_weights = current_path+'albert'
        model = AlbertModel.from_pretrained(pretrained_weights)
        tokenizer = AlbertTokenizer.from_pretrained(pretrained_weights)
    elif args.model_type == 'dbert':
        pretrained_weights = current_path+'dbert'
        model = DistilBertModel.from_pretrained(pretrained_weights)
        tokenizer = DistilBertTokenizer.from_pretrained(pretrained_weights)
    # elif args.model_type == 'xlnet':
    #     pretrained_weights = 'xlnet-base-cased'
    #     model = XLNetModel.from_pretrained(pretrained_weights)
    #     tokenizer = XLNetTokenizer.from_pretrained(pretrained_weights)
    elif args.model_type == 'electra':
        pretrained_weights = current_path+'electra'
        model = ElectraModel.from_pretrained(pretrained_weights)
        tokenizer = ElectraTokenizer.from_pretrained(pretrained_weights)
    return model, tokenizer

def encode_to_is(tokenizer,data,add_special_tokens):
    #encode 
    if type(data)==list:
        data=[tuple(tokenizer.encode(sentence,add_special_tokens=add_special_tokens))for sentence in data]
    elif type(data)==dict:
        data={tuple(tokenizer.encode(key,add_special_tokens=add_special_tokens)):tokenizer.encode(value,add_special_tokens=add_special_tokens)
              for key,value in data.items()}
    return data

def split_data(input,dev_rate,max_train_data_size):
    if max_train_data_size>0:
        train=input[:max_train_data_size]
        dev=input[max_train_data_size:]
    else:
        train=input[int(dev_rate*len(input)):]
        dev=input[:int(dev_rate*len(input))]
    return train,dev

def main(args):
    #data=[l.strip() for l in open('./data/news-commentary-v15.en')]
    data=[l.strip() for l in open(args.input)]
    #print(data[:5])
    if args.stereotypes:
        stereotypes=[word.strip() for word in open(args.stereotypes)]
        stereotypes_set=set(stereotypes)
    # print(stereotypes[:5])
    pat = re.compile(r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+""")
    
    #init attributes
    attributes_l=[]
    all_attributes_set=set()
    #load attribute from disk
    for attribute in args.attributes:
        l=[word.strip() for word in open(attribute)]
        attributes_l.append(set(l))
        all_attributes_set|=set(l)
    # print(attributes_l[:2])
    #prepare model and tokenizer
    model,tokenizer=prepare_transformer(args)
    
    if args.stereotypes:
        #encode stereotype
        tok_stereotypes=encode_to_is(tokenizer,stereotypes,add_special_tokens=False)

    neutral_examples=[]
    #init the attributes by the len ,and to be convinent to fill the detail of label
    if args.stereotypes:
        neutral_labels = []
    attributes_examples = [[] for _ in range(len(attributes_l))]
    attributes_labels = [[] for _ in range(len(attributes_l))]

    other_num=0

    for line in data:
        #load every line from data
        netural_flag=True #中性词
        line=line.strip()
        if len(line)<1:
            continue
        leng=len(line.split())
        if leng>args.block_size or leng<=1:
            continue
        #regularization the sentence 
        tokens_orig=[token.strip() for token in re.findall(pat,line)]
        tokens_lower=[token.lower() for token in tokens_orig]
        token_set=set(tokens_lower)
        
        #store attribute in every other attribute_list
        attribute_other_l=[]
        for i,_ in enumerate(attributes_l):
            a_set=set()
            for j,attribute in enumerate(attributes_l):
                if i!=j:
                    a_set|=attribute
            attribute_other_l.append(a_set)
        #preprocess the attribute set 
        for i,(attribute_set,other_set) in enumerate(zip(attributes_l,attribute_other_l)):
            if attribute_set & token_set:
                netural_flag=False
                if not other_set & token_set:
                    orig_line=line
                    line=tokenizer.encode(line,add_special_toekns=True)
                    labels=attribute_set&token_set
                    #get the last label,the reason idtk
                    for label in list(labels):
                        idx=tokens_lower.index(label)
                    #tuple the tokenizer ,then use nltk to convert to ngrams 
                    label=tuple(tokenizer.encode(tokens_orig[idx],add_special_tokens=True))
                    line_ngram=list(nltk.ngrams(line,len(label)))
                    if label not in line_ngram:
                        label=tuple(tokenizer.encode(tokens_orig[idx],add_special_tokens=False))                   
                        line_ngram=list(nltk.ngrams(line,len(label)))
                        if label not in line_ngram:
                            label=tuple(tokenizer.encode(f'a {tokens_orig[idx]} a'))[1:-1]
                            line_ngram=list(nltk.ngrams(line,len(label)))
                            if label not in line_ngram:
                                label = tuple([tokenizer.encode(f'{tokens_orig[idx]}2')[0]])
                                line_ngram = list(nltk.ngrams(line, len(label)))
                    idx=line_ngram.index(label)
                    attributes_examples[i].append(line)
                    attributes_examples[i].append([idx+j for j in range(len(label))])
                break
        #if is netural_flag
        if netural_flag:
            if args.stereotypes:
                if stereotypes_set & token_set:
                    line = tokenizer.encode(line,add_special_tokens=True)
                    labels=stereotypes_set&token_set
                    for label in list(labels):
                        idx=tokens_lower.index(label)
                        label=tuple(tokenizer.encode(tokens_orig[idx],add_special_tokens=True))[1:-1]
                        line_ngram=list(nltk.ngrams(line,len(label)))
                        if label not in line_ngram:
                            label = tuple(tokenizer.encode(tokens_orig[idx], add_special_tokens=False))
                            line_ngram = list(nltk.ngrams(line, len(label)))
                            if label not in line_ngram:
                                label = tuple(tokenizer.encode(f'a {tokens_orig[idx]} a'))[1:-1]
                                line_ngram = list(nltk.ngrams(line, len(label)))
                                if label not in line_ngram:
                                    label = tuple([tokenizer.encode(f'{tokens_orig[idx]}2')[0]])
                                    line_ngram = list(nltk.ngrams(line, len(label)))
                        idx=line_ngram.index(label)
                        neutral_examples.append(line)
                        neutral_labels.append([idx + i for i in range(len(label))])
            else:
                neutral_examples.append(tokenizer.encode(line,add_special_tokens=True))
    print('neutral:',len(neutral_examples))
    for i , examples in enumerate(attributes_examples):
        print(f'attributes{i}:',len(examples))
    data={
        'attributes_examples':attributes_examples,
        'attributes_labels': attributes_labels,
        'neutral_examples': neutral_examples
    }
    if args.stereotypes:
        data['neutral_labels']=neutral_labels
    torch.save(data,args.output+'/data.bin')



if __name__=="__main__":
    args=parse_args()
    main(args)