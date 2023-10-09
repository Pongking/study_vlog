import torch
from transformers import *
# from transformers import pipeline

# print(pipeline('sentiment-analysis')('we love you'))
# print(torch.__version__)
# print(torch.cuda.is_available())
# print(torch.cuda.device_count())
# print(torch.cuda.get_device_name(0))
def cout_sep():
    print("-----------------")
model_path='./model/bert-base-uncased'
# model=AlbertModel.from_pretrained(model_path)
# tokenizer=AlbertTokenizer.from_pretrained(model_path)
model=BertModel.from_pretrained(model_path)
tokenizer=BertTokenizer.from_pretrained(model_path)
sentence="hello,world!Do you miss me,when i miss you?"
token=tokenizer.tokenize(sentence)
indexs=tokenizer.convert_tokens_to_ids(token)
tokens=tokenizer.convert_ids_to_tokens(indexs)
print(token)
print(indexs)
print(tokens)

cout_sep()
input_ids=torch.tensor(tokenizer.encode(sentence))
print(input_ids)
#去除不必要的向量维度 去除0维里大小为1的维度
input_ids_squ=torch.tensor(tokenizer.encode(sentence)).unsqueeze(0)
print(input_ids_squ)

cout_sep()
cls_id=tokenizer._convert_token_to_id('[CLS]')
sep_id=tokenizer._convert_token_to_id('[SEP]')
print(cls_id,sep_id)
cout_sep()
sentence2="how are you"
input_ids2=torch.tensor(tokenizer.encode(sentence2)).unsqueeze(0)
tokens2=tokenizer.tokenize(sentence2)

# for x in input_ids2[0]:
#     print(x)
print(input_ids2[0])
templs=input_ids2[0].numpy()
tmp3=[101]
for i in range(1,len(templs)-1):
    tmp3.append(templs[i]+3)
tmp3.append(102)
inputs_ids3=torch.tensor(tmp3).unsqueeze(0)
print(inputs_ids3)
cout_sep()
outputs1=model(input_ids_squ)
outputs2=model(input_ids2)
outputs3=model(inputs_ids3)
print(outputs1[0].shape)
print(outputs1[1].shape)
cout_sep()
print(outputs2[0].shape)
print(outputs2[1].shape)
cout_sep()
#print(outputs1[0][0][1])
print(tokens[5]+' '+str(outputs1[0][0][6].mean()))
cout_sep()
print(tokens2[2]+' '+str(outputs2[0][0][3].mean()))
cout_sep()
print(outputs3[0][0][0].mean())
# print((180-70)*0.7)