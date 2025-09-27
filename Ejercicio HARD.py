import matplotlib.pyplot as plt  # Importa la librería para gráficos

# Datos poblacionales históricos (en miles de habitantes)

años_historicos = [2018, 2019, 2020, 2021, 2022]  # Años para datos históricos
poblacion = {
    "Bogotá": [7830, 7900, 7970, 8050, 8120],       # Población histórica de Bogotá
    "Antioquia": [6420, 6480, 6535, 6590, 6645],    # Población histórica de Antioquia
    "Valle del Cauca": [4840, 4900, 4955, 5020, 5090]  # Población histórica del Valle del Cauca
}

# Función para calcular la tasa de crecimiento anual compuesto

def tasa_crecimiento_compuesto(pinicial, pfinal, n):
    # Calcula tasa anual compuesta usando la fórmula (pfinal/pinicial)^(1/n) - 1
    return (pfinal / pinicial) ** (1 / n) - 1

# Calcular número de años entre datos históricos

n_años = años_historicos[-1] - años_historicos[0]

# Diccionario con tasas de crecimiento calculadas para cada región

tasas_crecimiento = {
    region: tasa_crecimiento_compuesto(datos[0], datos[-1], n_años)
    for region, datos in poblacion.items()
}

# Definir años para proyección futura (5 años)

años_futuros = [2023, 2024, 2025, 2026, 2027]
proyecciones = {}  # Diccionario para almacenar proyecciones

# Calcular proyección para cada región según su tasa de crecimiento anual

for region, tasa in tasas_crecimiento.items():
    poblacion_actual = poblacion[region][-1]  # Último dato histórico
    proyeccion_region = [
        round(poblacion_actual * ((1 + tasa) ** i), 2)  # Fórmula de crecimiento compuesto
        for i in range(1, 6)  # Para los 5 años futuros
    ]
    proyecciones[region] = proyeccion_region  # Guardar proyección

# Interacción con el usuario para elegir región y opción de datos

print("Regiones disponibles:")
for r in poblacion.keys():
    print(f"- {r}")  # Mostrar las regiones disponibles

region = input("\nEscribe la región que deseas consultar: ").strip()  # Pedir región

if region not in poblacion:
    print("\nEsa región no está en la base de datos. Intenta de nuevo.")  # Validar región
else:
    opcion = input(
        "\n¿Qué deseas ver?\n"
        "1. Tasa de crecimiento anual compuesto\n"
        "2. Proyección de población\n"
        "3. Ambas\n"
        "Escribe el número de tu opción: "
    ).strip()  # Pedir opción al usuario

    print("\n----------------------------")

    if opcion == "1":
        # Mostrar solo la tasa de crecimiento anual
        print(f"{region}: {tasas_crecimiento[region]*100:.2f}% anual")
    elif opcion == "2":
        # Mostrar solo la proyección de población
        print(f"Proyección de población para {region}:\n")
        for año, valor in zip(años_futuros, proyecciones[region]):
            print(f"  {año}: {valor} mil habitantes")
    elif opcion == "3":
        # Mostrar tasa de crecimiento y proyección
        print(f"{region}: {tasas_crecimiento[region]*100:.2f}% anual\n")
        print(f"Proyección de población para {region}:\n")
        for año, valor in zip(años_futuros, proyecciones[region]):
            print(f"  {año}: {valor} mil habitantes")
    else:
        print("Opción no válida.")  # Control de opción errónea

    # Preguntas y respuestas para reflexión
    
    print("\n----------------------------")
    print("Preguntas y respuestas:\n")

    print("1. ¿Cómo afecta la tasa de crecimiento poblacional a la planificación de políticas públicas en áreas como salud, infraestructura, y educación?\n")
    print("   Respuesta: Una mayor tasa de crecimiento implica mayor demanda de servicios públicos, "
          "por lo que el gobierno debe planificar más hospitales, colegios y proyectos de infraestructura "
          "para satisfacer las necesidades de la población.\n")

    print("2. ¿Qué factores sociales o económicos podrían haber influido en la tasa de crecimiento poblacional de cada región durante el período analizado?\n")
    print("   Respuesta: Factores como la migración interna, la disponibilidad de empleo, la seguridad, "
          "las condiciones de vida y el acceso a servicios básicos pueden haber impactado en el crecimiento "
          "de cada región.\n")

    print("3. ¿Qué diferencias podrían existir en las tasas de crecimiento entre las distintas regiones y por qué?\n")
    print("   Respuesta: Las diferencias pueden deberse a la concentración de oportunidades laborales, "
          "el desarrollo industrial, la inversión pública y privada, así como factores culturales y sociales "
          "que influyen en la natalidad y la migración.\n")

# ---- GRÁFICOS ----

# Gráfico conjunto para las tres regiones (histórico + proyección)

plt.figure(figsize=(10, 6))  # Crear figura grande
for region in poblacion.keys():
    plt.plot(años_historicos, poblacion[region], marker='o', label=f"{region} Histórico")  # Línea sólido para histórico
    plt.plot(años_futuros, proyecciones[region], marker='o', linestyle='--', label=f"{region} Proyección")  # Línea punteada para proyección
plt.title("Población Histórica y Proyección")  # Título del gráfico
plt.xlabel("Año")  # Etiqueta eje X
plt.ylabel("Población (miles de habitantes)")  # Etiqueta eje Y
plt.legend()  # Mostrar leyenda con las etiquetas
plt.grid(True)  # Activar grilla para facilitar lectura
plt.show()  # Mostrar gráfico

# Gráficos individuales para cada región

for region in poblacion.keys():
    plt.figure(figsize=(8, 5))  # Crear figura
    plt.plot(años_historicos, poblacion[region], marker='o', label="Histórico")  # Histórico
    plt.plot(años_futuros, proyecciones[region], marker='o', linestyle='--', label="Proyección")  # Proyección
    plt.title(f"Población de {region}")  # Título específico
    plt.xlabel("Año")  # Etiqueta eje X
    plt.ylabel("Población (miles de habitantes)")  # Etiqueta eje Y
    plt.legend()  # Leyenda
    plt.grid(True)  # Grilla
    plt.show()  # Mostrar figura

# Gráfico de barras con las tasas de crecimiento anual compuesto (%)

plt.figure(figsize=(8, 5))  # Figura
regiones = list(tasas_crecimiento.keys())  # Nombres de regiones
tasas_pct = [tasas_crecimiento[r] * 100 for r in regiones]  # Convertir a %
plt.bar(regiones, tasas_pct, color=['skyblue', 'lightgreen', 'salmon'])  # Barra con distintos colores
plt.title("Tasa de Crecimiento Anual Compuesto (%)")  # Título
plt.ylabel("Tasa de crecimiento (%)")  # Etiqueta Y
plt.grid(axis='y')  # Grilla solo en Y
plt.show()  # Mostrar gráfico
