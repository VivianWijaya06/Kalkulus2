from numerik import trapezoidal_integration, simpsons_integration  
import math

def f(x):
    return math.sin(x)

a = 0
b = math.pi/2

trap_result = trapezoidal_integration(f, a, b)
simp_result = simpsons_integration(f, a, b)

print("Numerical integration results:")
print(f"Trapezoidal rule: {trap_result:.8f}")
print(f"Simpson's rule: {simp_result:.8f}")
print(f"Exact result: 1.0")

print("\nErrors:")
print(f"Trapezoidal error: {abs(trap_result - 1):.2e}")
print(f"Simpson's error: {abs(simp_result - 1):.2e}")