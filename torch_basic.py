import torch
import numpy as np

# 1) random numbers

x = torch.rand(2,3)
print(x)
print(x.shape)

# 2) zeros, ones, arange

x = torch.zeros(2,3)
print(x)
print(x.shape)

x = torch.ones(2,3)
print(x)
print(x.shape)

x = torch.arange(0, 3, 0.5)
print(x)
print(x.shape)

# 3) Tensor Data Type

x = torch.FloatTensor(2,3)
print(x)
print(x.shape)
x = torch.FloatTensor([2,3])
print(x)
print(x.shape)
x = x.type_as(torch.IntTensor())
print(x)
print(x.shape)

# 4) Numpy to Tensor, Tensor to Numpy

x1 = np.ndarray(shape=(2,3), dtype=int, buffer=np.array([1,2,3,4,5,6]))
x2 = torch.from_numpy(x1)
print(x2)

x3 = x2.numpy()
print(x3)

# 5) Tensor on GPU & CPU
x = torch.rand(2,3)
x_gpu = x.cuda()
print(x_gpu)
x_cpu = x_gpu.cpu()
print(x_cpu)

# 6) Tensor Size
x = torch.rand(2,3)
print(x.size())

# 7) Indexing, Slicing, Joining
x = torch.rand(4,3)
out = torch.index_select(x, 0, torch.LongTensor([0,3]))
print(x)
print(out)

print(x[:,0])
print(x[0,:])
print(x[0:3,0:3])