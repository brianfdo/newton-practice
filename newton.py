def function(x):
    return float(x**2) + 10


epsilon = 0.0000005


def derivative(x):
    return float((function(x + epsilon) - function(x)) / epsilon)


def newton_method(x, func):
    x_t_1 = x
    x_t = 0
    while True:
        d1 = derivative(x)
        print(d1)
        d2 = (derivative(x + epsilon) - derivative(x)) / epsilon
        print(d2)
        x_t = x_t_1 - (d1 / d2)
        print(x_t)
        if abs(x_t - x_t_1) < 6:
            break
        x_t_1 = x_t
    return x_t


newton_method(5, function)
