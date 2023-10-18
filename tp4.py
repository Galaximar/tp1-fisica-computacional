#################Ejercicio 1#################
h=0.00001
def dx(cb):
   def dfdx(x):
    return (cb(x+h)-cb(x))/h
   
   return dfdx

def func(x):
  return x**3
derivada=dx(func)
segundaDervada=dx(dx(func))


def secondDerivate(cb):
  def dfdx(x):
    return (cb(x+h)-2*cb(x)+cb(x-h))/h**2
  return dfdx

dxdx=secondDerivate(func)
print("Función x**3 evaluada en 2:\nSegunda derivada por definición:",segundaDervada(2),"\nSegunda derivada dada por el método de aproximación:",dxdx(2))

def system(difusividad):

    def eq(y, t):
        return difusividad
    
    return eq
