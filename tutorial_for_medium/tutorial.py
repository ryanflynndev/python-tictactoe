def new_decorator(original_func):
    def wrap_func():
        print('Some extra code before')
        original_func()
        print('Some extra code after')
    return wrap_func()
    

@new_decorator
def function_with_decorator():
    print("I'm getting decorated")

