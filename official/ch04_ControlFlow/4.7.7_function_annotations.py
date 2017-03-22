
def my_func(ham: str, eggs: str = 'eggs') -> str:
    """Function Annotation
    1st
    2nd
    """
    print("Annotations:", my_func.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(my_func('spam'))
