import torch


bert_data_dir='./preprocess/42/bert/data.bin'
bert_data=torch.load(bert_data_dir)

roberta_data_dir='./preprocess/42/roberta/data.bin'
roberta_data=torch.load(roberta_data_dir)

#data=[word for word in open(data_dir)]
print((bert_data['attributes_examples'][0][0]))
print((roberta_data['attributes_examples'][0][0]))