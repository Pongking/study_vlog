#print("hello,world!")
import torch
# print(torch.cuda.is_available)
# print(torch.__version__)
tensor1 = torch.tensor([[1.0, 2.0, 3.0],[1.0, 2.0, 3.0]])
tensor2 = torch.tensor([[4.0, 5.0, 6.0],[1.0, 2.0, 3.0]])
tensor3 = torch.tensor([[7.0, 8.0, 9.0],[1.0, 2.0, 3.0]])

# 将这三个张量放入一个列表中
tensor_list = [tensor1, tensor2, tensor3]
print(tensor_list)
'''
[tensor([[1., 2., 3.],[1., 2., 3.]]),
tensor([[4., 5., 6.],[1., 2., 3.]]), 
tensor([[7., 8., 9.],[1., 2., 3.]])]
'''
print(torch.stack(tensor_list,0))
'''
tensor([[[1., 2., 3.],[1., 2., 3.]],
        [[4., 5., 6.],[1., 2., 3.]],
        [[7., 8., 9.],[1., 2., 3.]]])
'''
print(torch.stack(tensor_list,1))
'''
tensor([[[1., 2., 3.],
         [4., 5., 6.],
         [7., 8., 9.]],

        [[1., 2., 3.],
         [1., 2., 3.],
         [1., 2., 3.]]])
'''
print(torch.cat(tensor_list,1))
#tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.],
        # [1., 2., 3., 1., 2., 3., 1., 2., 3.]])
print(torch.cat(tensor_list,0))
'''
tensor([[1., 2., 3.],
        [1., 2., 3.],
        [4., 5., 6.],
        [1., 2., 3.],
        [7., 8., 9.],
        [1., 2., 3.]])
'''
print(torch.mean(torch.cat(tensor_list,0),0))
#tensor([2.5000, 3.5000, 4.5000])   
print(torch.mean(torch.cat(tensor_list,0),0).unsqueeze(1))
'''
tensor([[2.5000],
        [3.5000],
        [4.5000]])
'''
print(torch.mean(torch.cat(tensor_list,0),0).unsqueeze(1).squeeze(1))
#tensor([2.5000, 3.5000, 4.5000])
# 计算这些张量的平均值
# average_tensor = torch.mean(torch.cat(tensor_list, 0), 0).detach().unsqueeze(0)

# 打印结果
# print(average_tensor)
# import os
# os.environ['CUDA_VISIBLE_DEVICES']='0'
# import torch
# # print(torch.cuda.is_available())
# class Classifier(torch.nn.Module):
#     def __init__(self):
#         super().__init__()
#         #classifier
#         self.linear_1 = torch.nn.Linear(32*8*4*8,32*8*4)
#         self.linear_2 = torch.nn.Linear(32*8*4,32*8)
#         self.batch_norm_1 = torch.nn.BatchNorm1d(32*8)

#         self.linear_3 = torch.nn.Linear(32*8,32)
#         self.linear_4 = torch.nn.Linear(32,1)

#         self.activation = torch.nn.ReLU()


#     def forward(self,x):
#         x = x.reshape(x.shape[0], -1)
#         x = self.linear_1(x)
#         x = self.activation(x)
#         x = self.linear_2(x)
#         x = self.activation(x)
#         x = self.batch_norm_1(x)

#         x = self.linear_3(x)
#         x = self.activation(x)
#         x = self.linear_4(x)
#         return x
    
# net = Classifier().cuda()
# inp = torch.rand(2,32,8,4,8).cuda()
# gt = torch.rand(2,1).cuda()
# outp = net(inp)
# loss = torch.nn.BCEWithLogitsLoss()(outp, gt)
# loss.backward()

# print(loss)