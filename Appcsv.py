import pandas as pd
import matplotlib.pyplot as plt

# Función para graficar el número de personajes por planeta
def graph_personajes_por_planeta():
    characters_df = pd.read_csv('starwars/csv/characters.csv')

    # Contar cantidad de personas por planeta
    planet_birth_counts = characters_df['homeworld'].value_counts()

    # Generar el gráfico
    plt.figure(figsize=(12, 8))
    planet_birth_counts.plot(kind='bar', color='skyblue')
    plt.title('Número de personajes nacidos en cada planeta')
    plt.xlabel('Planeta')
    plt.ylabel('Número de personajes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Función para agregar etiquetas a las barras del gráfico
def add_labels(ax):
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() * 1.005, p.get_height() * 1.005))

# Función para graficar diferentes características de las naves
def graph_naves():
    # Cargar el archivo starships.csv
    starships_df = pd.read_csv('starwars/csv/starships.csv')

    # Gráfico de longitud de las naves
    plt.figure(figsize=(12, 8))
    ax = starships_df.set_index('name')['length'].plot(kind='bar', color='skyblue', grid=True)
    add_labels(ax)
    plt.title('Longitud de las Naves')
    plt.xlabel('Nave')
    plt.ylabel('Longitud')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Gráfico de capacidad de carga
    plt.figure(figsize=(12, 8))
    ax = starships_df.set_index('name')['cargo_capacity'].plot(kind='bar', color='lightgreen', grid=True)
    add_labels(ax)
    plt.title('Capacidad de Carga de las Naves')
    plt.xlabel('Naves')
    plt.ylabel('Capacidad de carga')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Gráfico de velocidad máxima
    plt.figure(figsize=(12, 8))
    ax = starships_df.set_index('name')['hyperdrive_rating'].plot(kind='bar', color='salmon', grid=True)
    add_labels(ax)
    plt.title('Gráfico del Hiperimpulsor')
    plt.xlabel('Naves')
    plt.ylabel('Hiperimpulsor')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Gráfico de MGLT
    plt.figure(figsize=(12, 8))
    ax = starships_df.set_index('name')['MGLT'].plot(kind='bar', color='orange', grid=True)
    add_labels(ax)
    plt.title('Gráfico MGLT')
    plt.xlabel('Naves')
    plt.ylabel('MGLT')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Función para calcular la moda de una serie
def calculate_mode(series):
    return series.mode().iloc[0] if not series.mode().empty else None

# Función para calcular estadísticas de las naves
def ship_statistics():
    # Cargar los datos de las naves desde el archivo CSV
    starships_df = pd.read_csv('starwars/csv/starships.csv')

    # Agrupar por clase de nave
    grouped = starships_df.groupby('starship_class')

    # Calcular estadísticas
    stats_df = grouped.agg({
        'hyperdrive_rating': ['mean', 'max', 'min', calculate_mode],
        'MGLT': ['mean', 'max', 'min', calculate_mode],
        'max_atmosphering_speed': ['mean', 'max', 'min', calculate_mode],
        'cost_in_credits': ['mean', 'max', 'min', calculate_mode]
    })

    # Renombrar columnas para mejor legibilidad
    stats_df.columns = ['_'.join(col).strip() for col in stats_df.columns.values]
    stats_df.rename(columns={
        'hyperdrive_rating_calculate_mode': 'hyperdrive_rating_mode',
        'MGLT_calculate_mode': 'MGLT_mode',
        'max_atmosphering_speed_calculate_mode': 'max_atmosphering_speed_mode',
        'cost_in_credits_calculate_mode': 'cost_in_credits_mode'
    }, inplace=True)

    # Mostrar la tabla
    print(stats_df)

# Función para mostrar el menú de la aplicación y manejar la selección del usuario
def menuAppCsv():
    while True:
        print("1. Gráfico de personajes por planeta")
        print("2. Gráfico de naves")
        print("3. Estadísticas de las naves")
        print("4. Salir")
        choice = input("Escoge una opción: ")
        if choice == '1':
            graph_personajes_por_planeta()
        elif choice == '2':
            graph_naves()
        elif choice == '3':
            ship_statistics()
        elif choice == '4':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")