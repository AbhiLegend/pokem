import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Define a function to get the data from the Pokemon API
def get_pokemon_data():
    url = "https://pokeapi.co/api/v2/pokemon"
    data = requests.get(url).json()
    return data['results']


# Define the app layout
st.title("Pokemon API Visualization Dashboard")
st.write("Select a Pokemon to view its base stats:")

# Get the data from the Pokemon API
pokemon_data = get_pokemon_data()

# Add a dropdown menu for the user to select a Pokemon
selected_pokemon = st.selectbox("Select a Pokemon", [pokemon['name'].capitalize() for pokemon in pokemon_data])

# Get the base stats for the selected Pokemon
pokemon_url = [pokemon['url'] for pokemon in pokemon_data if pokemon['name'] == selected_pokemon.lower()][0]
pokemon_stats = requests.get(pokemon_url).json()['stats']

# Convert the base stats to a pandas DataFrame
stats_df = pd.DataFrame()
for stat in pokemon_stats:
    stat_name = stat['stat']['name']
    base_stat = stat['base_stat']
    stats_df = stats_df.append({'Stat': stat_name, 'Base Stat': base_stat}, ignore_index=True)

# Add a bar chart to visualize the base stats for the selected Pokemon
st.write("Base stats for {}".format(selected_pokemon))
fig, ax = plt.subplots()
ax.bar(stats_df['Stat'], stats_df['Base Stat'])
plt.xticks(rotation=45)
st.pyplot(fig)
