import os

file = open(file="resources/LISTADOALUMNADO.csv",mode="r",encoding="utf-8")
contador = 150
contenido = file.readlines()
print(contenido)
# while(contenido!=None or contenido!=""):
#     print(contenido)
#     contador+=1
#     contenido = file.readline(contador)