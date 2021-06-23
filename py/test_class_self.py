class inner:
    def __init__(self, m):
        self.m = m

    def __call__(self, x):
        print("self.m: ", self.m)
        print("x: ", x)

class outter:
    def __init__(self, m):
      self.inn = inner(m)

    def __call__(self, x):
      self.inn(x)


o = outter(1)
o2 = outter(2)

o(8)
o.__call__(7)
# 传入self
outter.__call__(o, 6)

print(outter is o.__class__)
# 从实例获取class，然后显示传入self
o.__class__.__call__(o, 6)
# 从实例获取class，然后显示传入一个自定的self
o.__class__.__call__(o2, 6)


is_consistent = False

class P:
  def __init__(self, x):
    global is_consistent
    if is_consistent:
      self.v = x / 2
    else:
      self.v = x

class M:
  def __init__(self, x):
    self.p = P(x)

  def __call__(self, input):
    return input * self.p.v

class CM:
  def __init__(self, cls, *args, **kwargs):
    self.cls = cls
    global is_consistent
    is_consistent = True
    self.m = self.cls(*args, **kwargs)
    is_consistent = False

  def __call__(self, *args):
    return self.m(*args)

m = M(2)
print(m(10))    # 20

c_m = CM(M, 2)
print(c_m(10))  # 10
