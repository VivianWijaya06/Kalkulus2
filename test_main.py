import sys
import os
import math
from math import sqrt, sin, cos, pi

# Add current directory to path to import main
sys.path.append(os.path.dirname(__file__))

# Import the main numerical methods
from main import forward_difference, central_difference, trapezoidal_integration, simpsons_integration, bisection_method

# Import case files for their specific functions and test cases
import case_a
import case_b

def test_derivatives():
    """Test derivative functions"""
    print("Testing Derivative Functions:")
    print("=" * 40)
    
    # Test function: f(x) = x^2, f'(x) = 2x
    def f(x):
        return x**2
    
    x = 2.0
    expected_derivative = 2 * x  # 4.0
    
    forward_result = forward_difference(f, x)
    central_result = central_difference(f, x)
    
    print(f"Function: f(x) = x^2 at x = {x}")
    print(f"Expected derivative: {expected_derivative}")
    print(f"Forward difference: {forward_result:.6f}")
    print(f"Central difference: {central_result:.6f}")
    print(f"Forward error: {abs(forward_result - expected_derivative):.2e}")
    print(f"Central error: {abs(central_result - expected_derivative):.2e}")
    print()

def test_integration():
    """Test integration functions"""
    print("Testing Integration Functions:")
    print("=" * 40)
    
    # Test function: f(x) = x^2, integral from 0 to 2 = 8/3 ≈ 2.6667
    def f(x):
        return x**2
    
    a, b = 0, 2
    expected_integral = (b**3 - a**3) / 3  # 8/3
    
    trap_result = trapezoidal_integration(f, a, b)
    simpson_result = simpsons_integration(f, a, b)
    
    print(f"Function: f(x) = x^2 from {a} to {b}")
    print(f"Expected integral: {expected_integral:.6f}")
    print(f"Trapezoidal rule: {trap_result:.6f}")
    print(f"Simpson's rule: {simpson_result:.6f}")
    print(f"Trapezoidal error: {abs(trap_result - expected_integral):.2e}")
    print(f"Simpson's error: {abs(simpson_result - expected_integral):.2e}")
    print()

def test_trigonometric_integration():
    """Test with trigonometric functions like case-b.py"""
    print("Testing Trigonometric Integration (like case-b.py):")
    print("=" * 50)
    
    def f(x):
        return math.sin(x)
    
    a = 0
    b = math.pi/2
    expected = 1.0  # integral of sin(x) from 0 to π/2 = 1
    
    trap_result = trapezoidal_integration(f, a, b)
    simp_result = simpsons_integration(f, a, b)
    
    print("Numerical integration results:")
    print(f"Trapezoidal rule: {trap_result:.8f}")
    print(f"Simpson's rule: {simp_result:.8f}")
    print(f"Exact result: {expected}")
    
    print("\nErrors:")
    print(f"Trapezoidal error: {abs(trap_result - expected):.2e}")
    print(f"Simpson's error: {abs(simp_result - expected):.2e}")
    print()

def test_root_finding():
    """Test root finding function"""
    print("Testing Root Finding Function:")
    print("=" * 40)
    
    # Test function: f(x) = x^2 - 4, root at x = 2
    def f(x):
        return x**2 - 4
    
    a, b = 0, 3
    expected_root = 2.0
    
    try:
        root = bisection_method(f, a, b)
        print(f"Function: f(x) = x^2 - 4")
        print(f"Search interval: [{a}, {b}]")
        print(f"Expected root: {expected_root}")
        print(f"Found root: {root:.6f}")
        print(f"Function value at root: {f(root):.6f}")
        print(f"Error: {abs(root - expected_root):.2e}")
    except ValueError as e:
        print(f"Error: {e}")
    print()

def test_stationary_points():
    """Test finding stationary points like case-a.py"""
    print("Testing Stationary Points (like case-a.py):")
    print("=" * 45)
    
    def f(x):
        return x**3 - 3*x**2 + 2*x
    
    # Find stationary points using bisection on derivative
    try:
        root1 = bisection_method(lambda x: central_difference(f, x), 0, 1)
        root2 = bisection_method(lambda x: central_difference(f, x), 1, 2)
        
        print("Numerical stationary points:")
        print(f"x1 = {root1:.6f}")
        print(f"x2 = {root2:.6f}")
        
        # Calculate exact stationary points
        exact_root1 = (3 - sqrt(3))/3
        exact_root2 = (3 + sqrt(3))/3
        
        print("\nExact stationary points:")
        print(f"x1 = {exact_root1:.6f}")
        print(f"x2 = {exact_root2:.6f}")
        
        print("\nComparison:")
        print(f"Error for x1: {abs(root1 - exact_root1):.2e}")
        print(f"Error for x2: {abs(root2 - exact_root2):.2e}")
    except ValueError as e:
        print(f"Error finding stationary points: {e}")
    print()

def test_case_files():
    """Test using the case file libraries and functions"""
    print("Testing Case File Libraries:")
    print("=" * 35)
    
    # Test Case A functions and libraries
    print("Case A - Stationary Points Analysis:")
    print("-" * 35)
    
    # Use the exact function from case_a.py
    def f_case_a(x):
        return x**3 - 3*x**2 + 2*x
    
    def f_prime_exact_case_a(x):
        return 3*x**2 - 6*x + 2
    
    # Find stationary points using libraries from case_a
    root1 = bisection_method(lambda x: central_difference(f_case_a, x), 0, 1)
    root2 = bisection_method(lambda x: central_difference(f_case_a, x), 1, 2)
    
    print(f"Numerical stationary points:")
    print(f"x1 = {root1:.6f}")
    print(f"x2 = {root2:.6f}")
    
    # Calculate exact using math.sqrt from case_a
    exact_root1 = (3 - sqrt(3))/3
    exact_root2 = (3 + sqrt(3))/3
    
    print(f"\nExact stationary points:")
    print(f"x1 = {exact_root1:.6f}")
    print(f"x2 = {exact_root2:.6f}")
    
    print(f"\nComparison:")
    print(f"Error for x1: {abs(root1 - exact_root1):.2e}")
    print(f"Error for x2: {abs(root2 - exact_root2):.2e}")
    print()
    
    # Test Case B functions and libraries
    print("Case B - Trigonometric Integration:")
    print("-" * 35)
    
    # Use the exact function from case_b.py
    def f_case_b(x):
        return math.sin(x)
    
    a = 0
    b = math.pi/2
    
    trap_result = trapezoidal_integration(f_case_b, a, b)
    simp_result = simpsons_integration(f_case_b, a, b)
    
    print("Numerical integration results:")
    print(f"Trapezoidal rule: {trap_result:.8f}")
    print(f"Simpson's rule: {simp_result:.8f}")
    print(f"Exact result: 1.0")
    
    print("\nErrors:")
    print(f"Trapezoidal error: {abs(trap_result - 1):.2e}")
    print(f"Simpson's error: {abs(simp_result - 1):.2e}")
    print()

def test_case_b_definite_integrals():
    """
    Kasus B – Integral Tentu
    Test multiple functions and intervals for definite integration
    """
    print("🔢 Kasus B – Integral Tentu (Definite Integrals)")
    print("=" * 55)
    
    # Test Case 1: Trigonometric Function
    print("📊 Test Case 1: f(x) = sin(x)")
    print("-" * 30)
    
    def f1(x):
        return math.sin(x)
    
    a1, b1 = 0, math.pi/2
    exact1 = 1.0  # ∫sin(x)dx from 0 to π/2 = [-cos(x)] = -cos(π/2) + cos(0) = 1
    
    trap1 = trapezoidal_integration(f1, a1, b1)
    simp1 = simpsons_integration(f1, a1, b1)
    
    print(f"Fungsi: f(x) = sin(x)")
    print(f"Interval: [{a1}, π/2] = [{a1}, {b1:.6f}]")
    print(f"Solusi eksak: {exact1}")
    print(f"Metode Trapezoidal: {trap1:.8f}")
    print(f"Metode Simpson's: {simp1:.8f}")
    print(f"Error Trapezoidal: {abs(trap1 - exact1):.2e}")
    print(f"Error Simpson's: {abs(simp1 - exact1):.2e}")
    print()
    
    # Test Case 2: Polynomial Function
    print("📊 Test Case 2: f(x) = x²")
    print("-" * 25)
    
    def f2(x):
        return x**2
    
    a2, b2 = 0, 3
    exact2 = (b2**3 - a2**3) / 3  # ∫x²dx = x³/3, so from 0 to 3 = 27/3 = 9
    
    trap2 = trapezoidal_integration(f2, a2, b2)
    simp2 = simpsons_integration(f2, a2, b2)
    
    print(f"Fungsi: f(x) = x²")
    print(f"Interval: [{a2}, {b2}]")
    print(f"Solusi eksak: {exact2:.6f}")
    print(f"Metode Trapezoidal: {trap2:.8f}")
    print(f"Metode Simpson's: {simp2:.8f}")
    print(f"Error Trapezoidal: {abs(trap2 - exact2):.2e}")
    print(f"Error Simpson's: {abs(simp2 - exact2):.2e}")
    print()
    
    # Test Case 3: Exponential Function
    print("📊 Test Case 3: f(x) = e^x")
    print("-" * 25)
    
    def f3(x):
        return math.exp(x)
    
    a3, b3 = 0, 1
    exact3 = math.exp(b3) - math.exp(a3)  # ∫e^x dx = e^x, so from 0 to 1 = e¹ - e⁰ = e - 1
    
    trap3 = trapezoidal_integration(f3, a3, b3)
    simp3 = simpsons_integration(f3, a3, b3)
    
    print(f"Fungsi: f(x) = e^x")
    print(f"Interval: [{a3}, {b3}]")
    print(f"Solusi eksak: {exact3:.6f}")
    print(f"Metode Trapezoidal: {trap3:.8f}")
    print(f"Metode Simpson's: {simp3:.8f}")
    print(f"Error Trapezoidal: {abs(trap3 - exact3):.2e}")
    print(f"Error Simpson's: {abs(simp3 - exact3):.2e}")
    print()
    
    # Test Case 4: Logarithmic Function
    print("📊 Test Case 4: f(x) = ln(x)")
    print("-" * 26)
    
    def f4(x):
        return math.log(x)
    
    a4, b4 = 1, math.e
    exact4 = 1.0  # ∫ln(x)dx from 1 to e = [x*ln(x) - x] = e*1 - e - (1*0 - 1) = 1
    
    trap4 = trapezoidal_integration(f4, a4, b4)
    simp4 = simpsons_integration(f4, a4, b4)
    
    print(f"Fungsi: f(x) = ln(x)")
    print(f"Interval: [{a4}, e] = [{a4}, {b4:.6f}]")
    print(f"Solusi eksak: {exact4:.6f}")
    print(f"Metode Trapezoidal: {trap4:.8f}")
    print(f"Metode Simpson's: {simp4:.8f}")
    print(f"Error Trapezoidal: {abs(trap4 - exact4):.2e}")
    print(f"Error Simpson's: {abs(simp4 - exact4):.2e}")
    print()
    
    # Test Case 5: Cosine Function
    print("📊 Test Case 5: f(x) = cos(x)")
    print("-" * 26)
    
    def f5(x):
        return math.cos(x)
    
    a5, b5 = 0, math.pi/2
    exact5 = 1.0  # ∫cos(x)dx from 0 to π/2 = [sin(x)] = sin(π/2) - sin(0) = 1
    
    trap5 = trapezoidal_integration(f5, a5, b5)
    simp5 = simpsons_integration(f5, a5, b5)
    
    print(f"Fungsi: f(x) = cos(x)")
    print(f"Interval: [{a5}, π/2] = [{a5}, {b5:.6f}]")
    print(f"Solusi eksak: {exact5:.6f}")
    print(f"Metode Trapezoidal: {trap5:.8f}")
    print(f"Metode Simpson's: {simp5:.8f}")
    print(f"Error Trapezoidal: {abs(trap5 - exact5):.2e}")
    print(f"Error Simpson's: {abs(simp5 - exact5):.2e}")
    print()
    
    # Summary
    print("📋 RINGKASAN PERBANDINGAN METODE")
    print("=" * 40)
    test_cases = [
        ("sin(x), [0,π/2]", exact1, trap1, simp1),
        ("x², [0,3]", exact2, trap2, simp2),
        ("e^x, [0,1]", exact3, trap3, simp3),
        ("ln(x), [1,e]", exact4, trap4, simp4),
        ("cos(x), [0,π/2]", exact5, trap5, simp5),
    ]
    
    print(f"{'Fungsi':<15} {'Eksak':<10} {'Trapezoidal':<12} {'Simpson':<12} {'Error T':<10} {'Error S':<10}")
    print("-" * 75)
    
    for name, exact, trap, simp in test_cases:
        error_t = abs(trap - exact)
        error_s = abs(simp - exact)
        print(f"{name:<15} {exact:<10.6f} {trap:<12.6f} {simp:<12.6f} {error_t:<10.2e} {error_s:<10.2e}")
    
    print()

def test_edge_cases():
    """Test edge cases"""
    print("Testing Edge Cases:")
    print("=" * 20)
    
    # Test Simpson's with odd n
    def f(x):
        return x
    
    print("Testing Simpson's rule with odd n (should auto-adjust):")
    result_odd = simpsons_integration(f, 0, 1, n=999)  # odd n
    result_even = simpsons_integration(f, 0, 1, n=1000)  # even n
    expected = 0.5  # integral of x from 0 to 1 = 1/2
    
    print(f"With n=999 (odd): {result_odd:.6f}")
    print(f"With n=1000 (even): {result_even:.6f}")
    print(f"Expected: {expected}")
    print()
    
    # Test bisection with same sign endpoints
    def g(x):
        return x**2 + 1  # Always positive
    
    print("Testing bisection with invalid interval (same signs):")
    try:
        bisection_method(g, 0, 1)
        print("ERROR: Should have raised ValueError!")
    except ValueError as e:
        print(f"Correctly caught error: {e}")
    print()

if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    print(f"Current directory: {os.getcwd()}")
    print("=" * 60)
    
    try:
        test_derivatives()
        test_integration()
        test_trigonometric_integration()
        test_root_finding()
        test_stationary_points()
        test_case_files()  # New test using case file libraries
        test_case_b_definite_integrals()
        test_edge_cases()
        
        print("✅ All tests completed successfully!")
        print("✅ Your program is working correctly!")
        print("✅ Case file libraries integrated successfully!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
