import sympy as s

x = s.symbols('x')
eq1 = s.sympify("sen(45)")
eq1 = eq1.replace(x,5)

print(eq1) # 35