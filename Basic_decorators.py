def decorator_function(original_function):
    def wrapper():
        print("Before function execution")
        original_function()
        print("After function execution")
    
    return wrapper


@decorator_function
def hello():
    print("Hello, World!")


hello()
