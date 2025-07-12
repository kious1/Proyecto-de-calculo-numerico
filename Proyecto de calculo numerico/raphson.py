import math
from sympy import symbols, diff, lambdify, sympify

#Realizado por: 
#Luis Lunar
#29.985.921
#Carrera: Licenciatura en Informatica
#Materia: Calculo Numerico

def newton_raphson_auto():
    print("Método de Newton-Raphson con Derivación Automática")
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
        df_expr = diff(expr, x)  # Derivada simbólica
        df = lambdify(x, df_expr, modules=['math'])
        segunda_derivada = diff(df_expr, x)
        df_segunda = lambdify(x, segunda_derivada, modules=['math'])
        
        print(f"\nFórmula ingresada: f(x) = {expr}")
        print(f"Primera Derivada calculada: f'(x) = {df_expr}")
        print(f"Segunda derivada calculada: f''(x) = {segunda_derivada}\n")
        
    except Exception as e:
        print(f"¡Error! La función ingresada no es válida. Detalle: {str(e)}")
        return
    
    # Ingreso de valores iniciales
    try:
        a = float(input("Límite inferior 'a' del intervalo: "))
        b = float(input("Límite superior 'b' del intervalo: "))
        tol = float(input("Tolerancia (ej: 0.001): "))
    except:
        print("¡Error! Ingresa números válidos.")
        return
    
    # Algoritmo de Newton-Raphson
    iteracion = 0
    error = float('inf')
    x_actual = (a + b) / 2  # Punto inicial en el medio del intervalo
    
    
    
    f_val = f(x_actual)
    df_val = df(x_actual)
    df_segunda_val = df_segunda(x_actual)
    converge = abs(f_val * df_segunda_val / df_val)
    
    if converge < 1:
        print("\n{:^10s}{:^15s}{:^15s}{:^15s}".format(
        "Iteración", "Xi", "Xi + 1", "Error"))
        print("-"*60)
        while error > tol:
            f_R = f(x_actual)
            df_R = df(x_actual)
            
            x_siguiente = round(x_actual - (f_R / df_R), 4)
            error = round(abs((x_siguiente - x_actual) / x_siguiente), 4)
            
            print("{:^10d}{:^15.4f}{:^15.4f}{:^15.4f}".format(
            iteracion, x_actual, x_siguiente, error))
            
            x_actual = x_siguiente
            iteracion += 1
    else:
        print(f"\nError: No se puede converger esta función: {expr}. Intenta con otro intervalo.")
        return
        
    
    print("\nResultado final:")
    print(f"Raíz aproximada: {x_actual:.4f}")
    print(f"Iteraciones realizadas: {iteracion}")

# Ejecutar el método
if __name__ == "__main__":
    newton_raphson_auto()