import pandas as pd 
import numpy as np 

pokemon = pd.DataFrame({
	'exolution':['lvysaur','Charmeleon','Wartortle','Metapod'],
	'hp':['45','39','44','45'],
	'name':['Bulbasaur','Charmander','Squirtle','Caterpie'],
	'pokedex':['yes','no','yes','no'],
	'type':['grass','fire','water','bug']
	},
	index = [0,1,2,3])
print pokemon

print pokemon.set_index(['name','type','hp','exolution','pokedex'])

# Place the order of the columns as name, type, hp, evolution, pokedex
pokemon = pokemon[['name','type','hp','exolution','pokedex']]
print pokemon

# Add another column called place, and insert what you have in mind
pokemon['place'] = ['park','pool','tree','forest']
print pokemon

# Present the type of each column
print pokemon.dtypes

print pokemon.head(1)

print pokemon.info()import pandas as pd 
import numpy as np 

pokemon = pd.DataFrame({
	'exolution':['lvysaur','Charmeleon','Wartortle','Metapod'],
	'hp':['45','39','44','45'],
	'name':['Bulbasaur','Charmander','Squirtle','Caterpie'],
	'pokedex':['yes','no','yes','no'],
	'type':['grass','fire','water','bug']
	},
	index = [0,1,2,3])
print pokemon

print pokemon.set_index(['name','type','hp','exolution','pokedex'])

# Place the order of the columns as name, type, hp, evolution, pokedex
pokemon = pokemon[['name','type','hp','exolution','pokedex']]
print pokemon

# Add another column called place, and insert what you have in mind
pokemon['place'] = ['park','pool','tree','forest']
print pokemon

# Present the type of each column
print pokemon.dtypes

print pokemon.head(1)

print pokemon.info()
