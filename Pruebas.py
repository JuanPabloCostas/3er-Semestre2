import sympy as s

x = s.symbols('x')
eq1 = s.sympify("2*x^2")
eq1 = eq1.replace(x,5)

print(eq1) # 35