print("Hello world")


import torch

print(torch.cuda.is_available())

print(torch.cuda.current_device())

print(torch.cuda.get_device_name(0))
