import numpy as np #importamos la libreria numpy para realizar operaciones matematicas 
# Definimos el precio unitario
precio_unitario = 90000

# Coeficientes de la ecuación cúbica con raíces reales
a, b, c, d = 1, -3, 3, -1  # Estos coeficientes garantizan soluciones reales

# Calculamos el discriminante
discriminante = (18 * a * b * c * d) - (4 * (b ** 3) * d) + ((b ** 2) * (c ** 2)) - (4 * a * (c ** 3)) - (27 * (a ** 2) * (d ** 2))

# Bucle para ingresar los coeficientes de la ecuación cúbica
while True:
    try:
        a = float(input("Ingrese el coeficiente a: "))
        b = float(input("Ingrese el coeficiente b: "))
        c = float(input("Ingrese el coeficiente c: "))
        d = float(input("Ingrese el coeficiente d: "))
        break
    except ValueError:
        print("Por favor, introduce un número válido.") #en caso de error el programa termina 
        
if discriminante < 0:
    print("La ecuación no tiene soluciones reales.")
else:
    print(f"Discriminante: {discriminante}")
    
    # Calculamos q y r
    q = ((3 * a * c) - (b ** 2)) / (9 * (a ** 2))
    r = ((9 * a * b * c) - (27 * (a ** 2) * d) - (2 * (b ** 3))) / (54 * (a ** 3))
    
    delta2 = (q ** 3) + (r ** 2)
    
    if delta2 > 0:
        print("Tres soluciones reales diferentes")
        theta = np.arccos(r / np.sqrt(-q**3))
        x1 = 2 * np.sqrt(-q) * np.cos(theta / 3) - (b / (3 * a))
        x2 = 2 * np.sqrt(-q) * np.cos((theta + 2 * np.pi) / 3) - (b / (3 * a))
        x3 = 2 * np.sqrt(-q) * np.cos((theta - 2 * np.pi) / 3) - (b / (3 * a))
        
    elif delta2 == 0:
        print("Tres soluciones reales, al menos dos son iguales")
        x1 = x2 = (-b / (3 * a)) + (2 * np.cbrt(r))
        x3 = (-b / (3 * a)) - np.cbrt(r)
        
    else:
        print("Una única solución real")
        x1 = (-r + np.cbrt(delta2)) - (b / (3 * a))
    
    # Calculamos ganancias
    ganancias = [round(x * precio_unitario, 2) for x in [x1, x2, x3] if not np.isnan(x)]
    print(f"Las soluciones son: {x1}, {x2}, {x3}")
    print(f"Las ganancias son: {ganancias}")
    print(f"Suma total de ganancias: ${sum(ganancias):,.2f}")







