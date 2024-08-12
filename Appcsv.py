import pandas as pd
import matplotlib.pyplot as plt

# Load character data from CSV
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


