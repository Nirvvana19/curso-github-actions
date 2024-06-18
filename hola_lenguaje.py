import os

username = os.getenv('USERNAME')
language = os.getenv('LANGUAGE')

print(f'Hola {username}, tu lenguaje favorito es {language}!')

