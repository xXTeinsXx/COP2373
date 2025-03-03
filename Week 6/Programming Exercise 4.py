print(10, 20, 30, end=".", sep=",")

def func_name(*args, **kwargs):  
    pass  

def pr_named_vals(**kwargs):
    for k in kwargs:
        print(k, ':', kwargs[k])

def pr_vals_2(*args, **kwargs):
    for i in args:
        print(i)
    for k in kwargs:
        print(k, ':', kwargs[k])

pr_vals_2(1, 2, 3, -4, a=100, b=200)
