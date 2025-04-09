# Definición de constantes
PRECIO_VENTA = 120000  # Precio de cada plancha en pesos
COSTO_ADQUISICION = 80000  # Costo de cada plancha en pesos
VENTAS_DIARIAS = 5  # Plancha vendidas diariamente
DURACION_MES = 30  # Días en el mes

def total_plancha_vendida(dia_ventas, dias):
    """Calcula la cantidad total de planchas vendidas en un mes."""
    return dia_ventas * dias

def ingreso_total(precio, total_vendido):
    """Calcula el ingreso total por la venta de planchas."""
    return precio * total_vendido

def costo_total(costo, total_vendido):
    """Calcula el costo total de las planchas vendidas."""
    return costo * total_vendido

def beneficio_total(ingreso, costo):
    """Calcula el beneficio total."""
    return ingreso - costo

def main():
    # Cálculos
    total_vendido = total_plancha_vendida(VENTAS_DIARIAS, DURACION_MES)
    ingreso = ingreso_total(PRECIO_VENTA, total_vendido)
    costo = costo_total(COSTO_ADQUISICION, total_vendido)
    beneficio = beneficio_total(ingreso, costo)

    # Mostrar resultados
    print("Resultados de ventas en un mes:")
    print(f"Total de planchas vendidas: {total_vendido} planchas")
    print(f"Ingreso total: {ingreso} pesos")
    print(f"Costo total: {costo} pesos")
    print(f"Beneficio: {beneficio} pesos")

if __name__ == "__main__":
    main()
