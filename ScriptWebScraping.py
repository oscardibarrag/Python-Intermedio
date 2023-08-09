# %% [markdown]
# # Scripts

# %%
import requests
from bs4 import BeautifulSoup

# %%
def obtener_conteido_pagina(url):
    response = requests.get(url)
    return response.text

# %%
def analizar_contenido_html(html):
    return BeautifulSoup(html, 'html.parser')

# %%
data =[]
def procesar_pagina(soup):
    titulos = []
    precios_originales = []
    precios_descuento = []
    precios_envio = []
    skus = []
    stocks = []
    
    titulo_items = soup.find_all('div','emproduct_right')
    
    for item in titulo_items:
        titulo = item.a.text.strip()
        titulos.append(titulo)
        
    precio_original_items = soup.find_all('span', class_ = 'oldPrice')
    
    for item in precio_original_items:
        precio_original = item.text.strip()
        precios_originales.append(precio_original)
        
    precio_descuento_items = soup.find_all('div', class_ = 'emproduct_right_price_left')
    
    for item in precio_descuento_items:
        precio_descuento = item.label.text.strip()
        precios_descuento.append(precio_descuento)
        
    sku_items = soup.find_all('div', class_='emproduct_right_artnum')
    
    for item in sku_items:
        sku = item.text.strip()
        skus.append(sku.lstrip('SKU: '))
        
    precio_envio_items = soup.find_all('span', class_={'deliveryvalue', 'deliverytextfree'})
    
    for item in precio_envio_items:
        precio_envio = item.text
        precios_envio.append(precio_envio)
    
    stock_items = soup.find_all('div', class_='emstock')
    
    for item in stock_items:
        stock = item.text.split()
        stocks.append(stock[1])
    
    min_length = min(len(titulos), len(skus), len(precios_originales), len(precios_descuento), len(precios_envio), len(stocks))
    for i in range(min_length):
        data.append({
            "Titulo": titulos[i] if i < len(titulos) else None,
            "Sku": skus[i] if i < len(skus) else None,
            "Precio original": precios_originales[i] if i < len(precios_originales) else None,
            "Precio Descuento": precios_descuento[i] if i < len(precios_descuento) else None,
            "Precio Envio": precios_envio[i] if i < len(precios_envio) else None,
            "Stock": stocks[i] if i < len(stocks) else None
        })
   
    
            
            


# %%
def manegar_paginacion(url_base, num_paginas):
    for i in range(1, num_paginas + 1):
            url = url_base + str(i)+'/'
            contenido_pagina = obtener_conteido_pagina(url)
            soup = analizar_contenido_html(contenido_pagina)
            procesar_pagina(soup)

# %%
url_base = "https://www.cyberpuerta.mx/Promociones/"
num_paginas = 10

manegar_paginacion(url_base, num_paginas)

# %%
data

# %%
import pandas as pd
df = pd.DataFrame(data)

# %%

import datetime

fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
df.to_csv(f"dataset/web scraping/promociones-cuberpuerta-{fecha_actual}.csv", index=False)


