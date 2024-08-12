import pandas as pd
import matplotlib.pyplot as plt

def graph_personajes_por_planeta():
    characters_df = pd.read_csv('starwars/csv/characters.csv')

    # Count the number of characters born on each planet
    planet_birth_counts = characters_df['homeworld'].value_counts()

    # Generate the bar graph
    plt.figure(figsize=(12, 8))
    planet_birth_counts.plot(kind='bar', color='skyblue')
    plt.title('Numero de personajes nacidos en cada planeta')
    plt.xlabel('Planeta')
    plt.ylabel('Numero de personajes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def graph_naves():
    # Load starship data from CSV
    starships_df = pd.read_csv('starwars/csv/starships.csv')

    # Plot ship length
    plt.figure(figsize=(12, 8))
    starships_df.set_index('name')['length'].plot(kind='bar', color='skyblue')
    plt.title('Ship Length Comparison')
    plt.xlabel('Starship')
    plt.ylabel('Length')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Plot cargo capacity
    plt.figure(figsize=(12, 8))
    starships_df.set_index('name')['cargo_capacity'].plot(kind='bar', color='lightgreen')
    plt.title('Cargo Capacity Comparison')
    plt.xlabel('Starship')
    plt.ylabel('Cargo Capacity')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Plot hyperdrive classification
    plt.figure(figsize=(12, 8))
    starships_df.set_index('name')['hyperdrive_rating'].plot(kind='bar', color='salmon')
    plt.title('Hyperdrive Classification Comparison')
    plt.xlabel('Starship')
    plt.ylabel('Hyperdrive Rating')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Plot MGLT
    plt.figure(figsize=(12, 8))
    starships_df.set_index('name')['MGLT'].plot(kind='bar', color='orange')
    plt.title('MGLT Comparison')
    plt.xlabel('Starship')
    plt.ylabel('MGLT')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

graph_naves()


