def test_args_kwargs(first, *args, **kwargs):
   print('Required argument: ', first)

   # 通过函数后，变成了pack的
   # 类型为tuple
   print(type(args))
   for v in args:
      print ('Optional argument (args): ', v)

   # 通过函数后，变成了pack的
   # 类型为dict
   print(type(kwargs))
   for k, v in kwargs.items():
      print ('Optional argument %s (kwargs): %s' % (k, v))

# function 接收的是unpack的
test_args_kwargs(1, 2, 3, 4, k1=5, k2=6)

arg = (1, 2, 3, 4)
kwarg = {"k1":5, "k2":6}
# function 接收的是unpack的
# test unpack
test_args_kwargs(*arg, **kwarg)
