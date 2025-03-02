from pyDatalog import pyDatalog
pyDatalog.clear()

# Definir relaciones y variables
pyDatalog.create_terms('Usuario, Cancion, Genero, LeGusta, PerteneceA, Recomendar, NoHaEscuchado, X, Y, Z, G')

# Hechos: Usuarios
+ Usuario('juan')
+ Usuario('maria')

# Hechos: Canciones
+ Cancion('song1')
+ Cancion('song2')
+ Cancion('song3')

# Hechos: Géneros
+ Genero('vallenato')
+ Genero('salsa')
+ Genero('merengue')

# Hechos: Relación entre canciones y géneros
+ PerteneceA('song1', 'vallenato')
+ PerteneceA('song2', 'salsa')
+ PerteneceA('song3', 'merengue')

# Hechos: Preferencias de usuarios
+ LeGusta('juan', 'song1')
+ LeGusta('maria', 'song2')

# Definir qué canciones no ha escuchado un usuario
NoHaEscuchado(X, Y) <= Cancion(Y) & Usuario(X) & ~LeGusta(X, Y)

# Regla 1
Recomendar(X, Y) <= Usuario(X) & Cancion(Y) & Genero(G) & Cancion(Z) & LeGusta(X, Z) & PerteneceA(Z, G) & PerteneceA(Y, G) & (Y != Z) & NoHaEscuchado(X, Y)

print("\n--- Consultas del Sistema de Recomendación Musical ---")

# Consulta 1
print("\n¿Qué canciones se recomiendan a Juan?")
print(Recomendar('juan', X))

# Consulta 2
print("\n¿A Maria le gusta el salsa?")
print(LeGusta('maria', X) & PerteneceA(X, 'salsa'))

# Consulta 3
print("\n¿Qué canciones de merengue no ha escuchado Juan?")
print(NoHaEscuchado('juan', X) & PerteneceA(X, 'merengue'))

