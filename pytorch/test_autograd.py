import torch
from torch.autograd import grad
import numpy as np

a = torch.tensor(3., requires_grad=True)
b = a**3
c = b + 10 * torch.exp(-a**2 / 10)
print("c:", float(c))

x = torch.tensor(3., requires_grad=True)
m = x**3
y = m + 10 * torch.exp(-x**2 / 10)
print("y:", float(y))

grads ={}
def save_grad(name):
  def hook(grad):
    print(grad)
    grads[name] = grad
  return hook

def nth_derivative(f, wrt, n):
    for i in range(n):
        if not f.requires_grad:
            return torch.zeros_like(wrt)
        grads = grad(f, wrt, create_graph=True)[0]
        print(grads)
        f = grads.sum()
    return grads
m.register_hook(save_grad("m_g"))
y.register_hook(save_grad("y_g"))


print("---- 1th grad ---")
print("x_g 1th grad by manual:", float(3 * x**2 - 2 * x * torch.exp(-x**2 / 10)))

print("x_g 1th grad by grad:", float(nth_derivative(y, x, 1)))

y.backward(retain_graph=True, create_graph=True)
# will acculate grad
# y.backward(retain_graph=True) 
print("x_g 1th grad by backward:", float(x.grad))
# m.grad is None 
# print("m_g 1th grad by backward:", float(m.grad))
print("m_g hook 1th grad by backward:", float(grads["m_g"]))
# y.grad is None 
# print("y_g 1th grad by backward:", float(y.grad))
print("y_g hook 1th grad by backward:", float(grads["y_g"]))
# ---- 1th grad ---

print("---- 2th grad ---")
u = torch.exp(-x**2 / 10)
print("x_g 2th grad by manual:",float(2 / 5 * u * x**2 + 6 * x - 2 * u))

print("x_g 2th grad by grad:", float(nth_derivative(y, x, 2)))

print("x_g 2th grad by backward:", float(x.grad))
#x.grad.backward()
print("x_g 2th grad by backward:", float(x.grad))
print("y_g hook 1th grad by backward:", float(grads["y_g"]))
print("m_g hook 1th grad by backward:", float(grads["m_g"]))
#print("y_g 2th grad by backward:", float(y.grad))

# ---- 2th grad ---

c.backward()
print("a_g:", a.grad)



