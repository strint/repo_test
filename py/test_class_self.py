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


