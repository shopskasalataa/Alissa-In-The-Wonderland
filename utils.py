# декоратор без параметри
def verify_positive(func):
    # self - все едно на check_positive подавам, каквото подавам на func
    def check_positive(self, *args, **kwargs):
        values = [x for x in args] + [x for x in kwargs.values()]
        def check_positive_arguments(x):
            if isinstance(x, (int, float)):
                return x >= 0
            elif isinstance(x, (list, tuple)):
                return all([check_positive_arguments(y) for y in x])
            else:
                return True 

        if not all([check_positive_arguments(x) for x in values]):
            raise ValueError("All numeric values should be positive.")
        return func(self, *args, **kwargs)

    return check_positive




# @verify_positive
# def f(self, x, y):
#     return None

# if __name__ == '__main__':
#     f('s', 5, [3, -4, 'a'])