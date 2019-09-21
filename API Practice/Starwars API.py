#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import pandas as pd
import numpy as np


# In[63]:


starwars = requests.get('https://swapi.co/api/')
sw_people = requests.get('https://swapi.co/api/people/')
sw_planets = requests.get('https://swapi.co/api/planets/')
sw_films = requests.get('https://swapi.co/api/films/')
sw_species = requests.get('https://swapi.co/api/species/')
sw_vehicles = requests.get('https://swapi.co/api/vehicles/')
sw_starships = requests.get('https://swapi.co/api/starships/')


# In[66]:


sw_data = starwars.json()
people_data = sw_people.json()
planets_data = sw_planets.json()
films_data = sw_films.json()
species_data = sw_species.json()
vehicles_data = sw_vehicles.json()
starships_data = sw_ships.json()


# In[70]:


print(sw_data.keys())
print(people_data.keys())
print(planets_data.keys())
print(films_data.keys())
print(species_data.keys())
print(vehicles_data.keys())
print(starships_data.keys())


# In[72]:


people_df = pd.DataFrame(people_data['results'])
people_df


# In[ ]:




