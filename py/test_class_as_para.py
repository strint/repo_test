from typing import Callable

is_consistent = False  # 标识consistent作用域

class Tensor:
  def __init__(self, x):
    self.s = 1
    global is_consistent
    if is_consistent:
      self.v = lambda : x / self.s
    else:
      self.v = x

  @property
  def data(self):
    if isinstance(self.v, Callable):
      return self.v()
    else:
      return self.v

class Module:
  def __init__(self, x):
    self.p = Tensor(x)

  def __call__(self, input):
    return input * self.p.data

class ConsistentModule:
  def __init__(self, cls, *args, **kwargs):
    self.cls = cls
    global is_consistent
    # 在consistent作用域下去做Module的初始化
    # 使得Tensor可以根据consistent作用域做特异的初始化，如lazy初始化
    is_consistent = True 
    self.m = self.cls(*args, **kwargs)
    is_consistent = False

  def __call__(self, *args):
    return self.m(*args)

m = Module(2)
print(m(10))    # 返回20

c_m = ConsistentModule(Module, 2)
c_m.m.p.s = 2 # 设置下切分
print(c_m(10))  # 返回10
