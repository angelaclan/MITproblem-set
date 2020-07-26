from ps2_newton import *


"""evaluate_poly(poly, x)"""
poly = (0.0, 0.0, 5.0, 9.3, 7.0)
x = -13
print(evaluate_poly(poly, x))

holy = (0.0,1.0, 2.0, 3.0, 4.0)
y = 5
print(evaluate_poly(holy, y))

"""compute_deriv(poly)"""
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
print(compute_deriv(poly))

poly = (6.0,)
print(compute_deriv(poly))

"""compute_root(poly, x_0, epsilon)"""
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = .0001
print(compute_root(poly, x_0, epsilon))