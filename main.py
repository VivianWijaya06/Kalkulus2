def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

def central_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def trapezoidal_integration(f, a, b, n=1000):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    return integral * h

def simpsons_integration(f, a, b, n=1000):
    if n % 2 != 0:
        n += 1 
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    return integral * h / 3

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Function must have different signs at endpoints")
    
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2