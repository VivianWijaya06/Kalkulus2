import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from numerik import bisection_method, central_difference 

def f(x):
    return x**3 - 3*x**2 + 2*x

def f_prime_exact(x):
    return 3*x**2 - 6*x + 2

root1 = bisection_method(lambda x: central_difference(f, x), 0, 1)
root2 = bisection_method(lambda x: central_difference(f, x), 1, 2)

print("Numerical stationary points:")
print(f"x1 = {root1:.6f}")
print(f"x2 = {root2:.6f}")


from math import sqrt
exact_root1 = (3 - sqrt(3))/3
exact_root2 = (3 + sqrt(3))/3

print("\nExact stationary points:")
print(f"x1 = {exact_root1:.6f}")
print(f"x2 = {exact_root2:.6f}")

print("\nComparison:")
print(f"Error for x1: {abs(root1 - exact_root1):.2e}")
print(f"Error for x2: {abs(root2 - exact_root2):.2e}")
