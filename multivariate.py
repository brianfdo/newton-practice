import autograd.numpy as np
import autograd

def multi_newton_method(x, func, epsilon=0.00005, tol=1e-8):
    g = autograd.jacobian(func)
    h = autograd.hessian(func)

    x = x0
    while True:
        gx = np.squeeze(g(x))
        hx = np.squeeze(h(x))

        delta = np.linalg.multi_dot([np.linalg.inv(hx), gx])
        x = x - delta
        if np.linalg.norm(delta) > tol:
            break

    return x

def f(x):
        return np.array([[(x[0] - 1560) ** 2 + (x[1] - 6540) ** 2 + (x[2] - 20140) ** 2 - (2.9 * 10 ** 3 * (0.07074 - x[3]) ** 2)],
                        [(x[0] - 18760) ** 2 + (x[1] - 2750) ** 2 + (x[2] - 18610) ** 2 - (2.9 * 10 ** 3 * (0.0722 - x[3]) ** 2)], 
                        [(x[0] - 17640) ** 2 + (x[1] - 14630) ** 2 + (x[2] - 13480) ** 2 - (2.9 * 10 ** 3 * (0.0769 - x[3]) ** 2)],
                        [(x[0] - 19170) ** 2 + (x[1] - 610) ** 2 + (x[2] - 18390) ** 2 - (2.9 * 10 ** 3 * (0.07242 - x[3]) ** 2)]])              

x0 = np.array([0., 0., 6730., 0.])

print(multi_newton_method(x0, f))
