import torch
import torch.nn.functional as F

input=torch.randn(2,2,3)
print(input)
#print(F.softmax(input,dim=0))
print(input.long())
print(input.long().sum())
print(input.long().sum()/input.shape[0])