import pandas as pd

# Leer el  dataset (CSV)
df = pd.read_csv('books.csv')

# Divide los valores en la columna 'book_authors' en una lista de autores, separando por  ';', ya que book_author inicialmente está como una cadena
df['book_authors'] = df['book_authors'].apply(lambda x: x.split(';') if pd.notnull(x) else x)

# Convertir el DataFrame a un formato JSON
json = df.to_json(orient='records', lines=True)

# Guardar el resultado en un archivo JSON
with open('data.json', 'w') as json_file:
    json_file.write(json)
