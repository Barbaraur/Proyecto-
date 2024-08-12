import pandas as pd
import matplotlib.pyplot as plt

def graph_personajes_por_planeta():
    characters_df = pd.read_csv('starwars/csv/characters.csv')

    # Contar cantidad de personas por planeta
    planet_birth_counts = characters_df['homeworld'].value_counts()

    # Generar el grafico
    plt.figure(figsize=(12, 8))
    planet_birth_counts.plot(kind='bar', color='skyblue')
    plt.title('Numero de personajes nacidos en cada planeta')
    plt.xlabel('Planeta')
    plt.ylabel('Numero de personajes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def add_labels(ax):
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() * 1.005, p.get_height() * 1.005))

def graph_naves():
    # Cargar el archivo starships.csv
    starships_df = pd.read_csv('starwars/csv/starships.csv')

    # Grafico costo de las naves
    plt.figure(figsize=(12, 8))
    ax = starships_df.set_index('name')['length'].plot(kind='bar', color='skyblue', grid=True)
    add_labels(ax)
    plt.title('Longitud de las Naves')
    plt.xlabel('Nave')
    plt.ylabel('Longitud')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Grafico de capacidad de carga
    plt.figure(figsize=(12, 8))
    ax = starships_df.set_index('name')['cargo_capacity'].plot(kind='bar', color='lightgreen', grid=True)
    add_labels(ax)
    plt.title('Capidad de Carga de las Naves')
    plt.xlabel('Naves')
    plt.ylabel('Capacidad de carga')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Grafico de velocidad maxima
    plt.figure(figsize=(12, 8))
    ax = starships_df.set_index('name')['hyperdrive_rating'].plot(kind='bar', color='salmon', grid=True)
    add_labels(ax)
    plt.title('Grafico del Hiperimpulsor ')
    plt.xlabel('Naves')
    plt.ylabel('Hiperimpulsor')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Grafico de MGLT
    plt.figure(figsize=(12, 8))
    ax = starships_df.set_index('name')['MGLT'].plot(kind='bar', color='orange', grid=True)
    add_labels(ax)
    plt.title('Grafico MGLT')
    plt.xlabel('Naves')
    plt.ylabel('MGLT')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def calculate_mode(series):
    return series.mode().iloc[0] if not series.mode().empty else None


def ship_statistics():
    # Load starship data from CSV
    starships_df = pd.read_csv('starwars/csv/starships.csv')

    # Group by starship class
    grouped = starships_df.groupby('starship_class')

    # Calculate statistics
    stats_df = grouped.agg({
        'hyperdrive_rating': ['mean', 'max', 'min', calculate_mode],
        'MGLT': ['mean', 'max', 'min', calculate_mode],
        'max_atmosphering_speed': ['mean', 'max', 'min', calculate_mode],
        'cost_in_credits': ['mean', 'max', 'min', calculate_mode]
    })

    # Rename columns for better readability
    stats_df.columns = ['_'.join(col).strip() for col in stats_df.columns.values]
    stats_df.rename(columns={
        'hyperdrive_rating_calculate_mode': 'hyperdrive_rating_mode',
        'MGLT_calculate_mode': 'MGLT_mode',
        'max_atmosphering_speed_calculate_mode': 'max_atmosphering_speed_mode',
        'cost_in_credits_calculate_mode': 'cost_in_credits_mode'
    }, inplace=True)

    # Display the table
    print(stats_df)




