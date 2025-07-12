import math

#Realizado por: 
#Luis Lunar
#29.985.921
#Carrera: Licenciatura en Informatica
#Materia: Calculo Numerico

def biseccion():
    print("Método de Bisección - Ingresa una función con operaciones matemáticas avanzadas")
    print("Ejemplos válidos:")
    print("  - 'math.sin(x) + math.log(x)'")
    print("  - 'math.exp(x) - x**2'")
    print("  - 'math.sqrt(x) - math.cos(x)'\n")
    
    # Ingreso de la función
    funcion_str = input("Ingresa f(x) usando 'math.' antes de funciones (ej: 'math.exp(x) - 4*x**2'): ")
    try:
        f = lambda x: eval(funcion_str, {'math': math, 'x': x})
    except:
        print("¡Error! La función ingresada no es válida.")
        return
    
    # Ingreso de intervalo y tolerancia
    try:
        a = float(input("Límite inferior 'a' del intervalo: "))
        b = float(input("Límite superior 'b' del intervalo: "))
        tol = float(input("Tolerancia (ej: 0.001): "))
    except:
        print("¡Error! Ingresa números válidos.")
        return
    
    # Verificación de cambio de signo
    if f(a) * f(b) >= 0:
        print("Error: No hay cambio de signo en [a, b]. Prueba otro intervalo.")
        return
    
    # Algoritmo de bisección
    iteracion = 0
    c_anterior = 0
    error = float('inf')
    while error > tol:
        c = (a + b) / 2
        
        if c_anterior is not None:
            error = round(abs((c - c_anterior) / c), 4)
        else:
            error = float('inf')
        
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c_anterior = c
        iteracion += 1
    
    print(f"\nResultado:")
    print(f"Raíz aproximada: {(a + b) / 2:.5f}")
    print(f"Iteraciones realizadas: {iteracion}")

# Ejecutar
biseccion()