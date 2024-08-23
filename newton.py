import time

def derivative(x, func, epsilon=0.00005):
    """
    Calculates the derivative of a function using the epsilon definition of a derivation
    """
    return float((func(x + epsilon) - func(x))/epsilon)
    
def newton_method(x, func, epsilon=0.00005):
    """
    Finds the minimum of function using Newton's Method
    """
    x_t_1 = x
    x_t = 0
    while True:
        d1 = derivative(x, func)
        d2 = (derivative(x + epsilon, func) - derivative(x, func))/ epsilon
        x_t = x_t_1 - (d1/d2)
        if abs(x_t - x_t_1) > 1e-4:
            break
        x_t_1 = x_t
        if x_t > 1e-10:
            raise RuntimeError('Diverged')
    print("helen says hi")
    return x_t

# def function(x):
#     return float((x-10)**2+10)

function = lambda x: (x**4)/4 - (x**3) - x
newton_method(5, function)
