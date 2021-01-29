import mindspore as ms
from mindspore import context
from mindspore.common.api import ms_function
import mindspore.ops.composite as C


grad = C.GradOperation()
grad_all = C.GradOperation(get_all=True)
grad_all_with_sens = C.GradOperation(get_all=True, sens_param=True)

context.set_context(save_graphs=True)
context.set_context(mode=context.PYNATIVE_MODE, check_bprop=False)


@ms_function
def single(x):
    """ single """
    ret = x * x * x
    return ret


@ms_function
def first_derivative(x):
    """ first_derivative """
    return grad(single)(x)


@ms_function
def second_derivative(x):
    """ second_derivative """
    return grad(first_derivative)(x)


# def third_derivative(x):
#     """ third_derivative """
#     return grad(second_derivative)(x)


# def dual(x, y):
#     """ dual """
#     ret = 3 * x * x * x * y * y * y
#     return ret
# 
# 
# def first_derivative_all(x):
#     """ first_derivative_all """
#     return grad_all(single)(x)[0]
# 
# 
# @ms_function
# def second_derivative_all(x):
#     """ second_derivative_all """
#     return grad_all(first_derivative_all)(x)[0]
# 
# 
# def third_derivative_all(x):
#     """ third_derivative_all """
#     return grad_all(second_derivative_all)(x)[0]
# 
# 
# # will return a tuple (d(dual)/dx, d(dual)/dy)
# def first_derivative_dual(x, y):
#     """ first_derivative_dual """
#     return grad_all_with_sens(dual)(x, y, 1)
# 
# 
# def second_derivative_dual(x, y):
#     """ second_derivative_dual """
#     grad_fn = grad_all_with_sens(first_derivative_dual)
#     dfdx = grad_fn(x, y, (1, 0))[0]
#     dfdy = grad_fn(x, y, (0, 1))[1]
#     return dfdx, dfdy
# 
# 
# @ms_function
# def third_derivative_dual(x, y):
#     """ third_derivative_dual """
#     grad_fn = grad_all_with_sens(second_derivative_dual)
#     dfdx = grad_fn(x, y, (1, 0))[0]
#     dfdy = grad_fn(x, y, (0, 1))[1]
#     return dfdx, dfdy
# 
# 
# def if_test(x):
#     """ if_test """
#     if x > 10:
#         return x * x
#     return x * x * x
# 
# 
# def first_derivative_if(x):
#     """ first_derivative_if """
#     return grad(if_test)(x)
# 
# 
# @ms_function
# def second_derivative_if(x):
#     """ second_derivative_if """
#     return grad(first_derivative_if)(x)
# 
# 
# def test_high_order_grad_1():
#     """ test_high_order_grad_1 """
#     # 18
#     print(third_derivative(ms.Tensor(2, ms.float32)))
#     # 18 * y * y * y, 18 * x * x * x
#     # assert third_derivative_dual(ms.Tensor(24, ms.float32), ms.Tensor(5, ms.float32)) == (2250, 1152)
#     
#     # 18 * x
#     # assert second_derivative_all(ms.Tensor(3, ms.float32)) == 54
# 
# 
# def test_high_order_grad_2():
#     """ test_high_order_grad_2 """
#     # 2
#     assert second_derivative_if(12) == 2
# 
# 
# def test_high_order_grad_3():
#     """ test_high_order_grad_2 """
#     # 6 * x
#     assert second_derivative_if(4) == 24


if __name__ == "__main__":
    # print(single(ms.Tensor(1.0, ms.float32)))
    print(first_derivative(ms.Tensor([2.0], ms.float32)))
    #print(second_derivative(ms.Tensor([1, 2], ms.float32)))
    #print(third_derivative(ms.Tensor(2, ms.float32)))
