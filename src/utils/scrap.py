from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np

df = pd.read_csv('data\lastfm.csv')
df.columns=['artista', 'album', 'cancion', 'fecha']

#DATAFRAME CON TODAS LAS BANDAS
webs = df.artista.value_counts(dropna=False).to_frame().head(200)

#CREAMOS UNA LISTA DONDE INDEXAMOS TODAS LAS BANDAS
bandas = list(webs.index.values)
for banda in bandas:
       banda.replace(" ", "+")
       url = "https://www.last.fm/music/" + str(banda)
       response = requests.get(url)
       html = response.content
       soup = bs(html, "lxml")
       print(soup.h1.get_text().lower(), end=",")  #Aqui sacamos el nombre de la banda
       all_a = soup.find_all(class_="tag")
       for tag in all_a:
              print(tag.get_text(), end=",")   #Aqui sacamos todos los tags asociados.
       print()