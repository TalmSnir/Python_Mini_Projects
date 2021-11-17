import sympy 

x,y=sympy.symbols("x y")
eq=sympy.Eq((2*x+y),0)

init_printing(sympy.Integral(y,x))
