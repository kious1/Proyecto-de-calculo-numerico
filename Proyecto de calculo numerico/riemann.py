import math
from sympy import symbols, sympify, lambdify, integrate, Float
from scipy.integrate import quad

#Realizado por: 
#Luis Lunar
#29.985.921
#Carrera: Licenciatura en Informatica
#Materia: Calculo Numerico

def riemann_integration():
    print("Método de Riemann para Integración Numérica")
    print("Ingresa una función con operaciones matemáticas avanzadas")
    print("Ejemplos válidos:")
    print("  - sin(x) + log(x)")
    print("  - exp(x) - x**2")
    print("  - sqrt(x) - cos(x)")
    print("  - x**3 - 2*x - 5")
    print("\nNota: Usa la sintaxis matemática estándar (no necesitas 'math.')\n")
    
    try:
        # Ingreso de la función
        funcion_str = input("Ingresa f(x) (ej: 'exp(x) - 4*x**2'): ")
        
        # Procesamiento con sympy
        x = symbols('x')
        expr = sympify(funcion_str)
        f = lambdify(x, expr, modules=['math'])
        
        print(f"\nFórmula ingresada: f(x) = {expr}")
        
    except Exception as e:
        print(f"¡Error! La función ingresada no es válida. Detalle: {str(e)}")
        return
    
    # Ingreso de valores iniciales
    try:
        a = float(input("Límite inferior 'a' de integración: "))
        b = float(input("Límite superior 'b' de integración: "))
        n = int(input("Número de subintervalos (n): "))
    except:
        print("¡Error! Ingresa valores válidos.")
        return
    
    # Calcular valor real de la integral (forzar cálculo)
    try:
        # Intentar cálculo simbólico exacto
        integral_real_simbolica = integrate(expr, (x, a, b))
        integral_real = float(integral_real_simbolica.evalf())
        metodo_usado = "simbólico (exacto)"
    except:
        # Si falla, usar integración numérica (scipy) como "valor real"
        integral_real, _ = quad(f, a, b)
        metodo_usado = "numérico (scipy.quad)"
    
    
    
    # Algoritmo de Riemann
    delta_x = (b - a) / n
    suma = 0.0
    
    print("\n{:^10s}{:^15s}{:^15s}{:^15s}".format(
        "Intervalo", "Xi", "f(Xi)", "Suma Acum."))
    print("-"*60)
    
    for i in range(n):
        # Calcular el punto Xi y el valor de la función en ese punto
        xi = a + i * delta_x
        f_xi = f(xi)
        suma += f_xi * delta_x
        
        print("{:^10d}{:^15.4f}{:^15.4f}{:^15.4f}".format(
            i+1, xi, f_xi, suma))
    
    print("\nResultado final:")
    print(f"Integral aproximada: {suma:.6f}")
    print(f"Número de subintervalos: {n}")
    print(f"Ancho de subintervalo (Δx): {delta_x:.6f}")
    print(f"Valor real de la integral ({metodo_usado}): {integral_real:.4f}")
    # Cálculo del error
    error = abs((integral_real - suma) / integral_real)
    print(f"Error : {error:.4f}")
   

# Ejecutar el método
if __name__ == "__main__":
    riemann_integration()