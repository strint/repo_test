# decorator run at function define, to create closure;
# but closure run at function calling

def decorator_a(func):
    print('deco_a start, input func is ', func)
 
    def deco_a_func(*args, **kwargs):
        print('doco_a_func pretreat func', func)
        res = func(*args, **kwargs)
        print('doco_a_func post process func', func)
        return res
 
    print('deco_a end.')
    return deco_a_func  # here return a closure (lambda with captured states)
 
 
def decorator_b(func):
    print('deco_b start, input func is ', func)
 
    def deco_b_func(*args, **kwargs):
        print('doco_b_func pretreat func', func)
        res = func(*args, **kwargs)
        print('doco_b_func post process func', func)
        return res
 
    print('deco_b end.')
    return deco_b_func
 
print("-------test decorator------------")
 
print('define f with decorator') 
# decorator run at function define, to create closure;
# but closure run at function calling
@decorator_a  # run decorator_a,  got input deco_b_func, return lambda deco_a_func 
@decorator_b  # run decorator_b,  got input f, return lambda deco_b_func 
def f(x):
    print('running f.')
    return x 

print('f type ', f)  # f is lambda deco_a_func

print('run f')
print('f(1) result ', f(1)) # run closure deco_a_func(deco_b_func(f()))
print('f(2) result ', f(2))
 

print("------simulate decorator-------------")
print('define g without decorator')
def g(x):
    print('running g.')
    return -x 

print('deocrate g with b')
g = decorator_b(g)
print('deocrate g with a')
g = decorator_a(g)
 
print('run g')
print('g(1) result ', g(1))
print('g(2) result ', g(2))

 
