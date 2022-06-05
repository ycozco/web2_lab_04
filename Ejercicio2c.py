from interpreter import draw
from chessPictures import *
# Ejercicio 2c 
# Se hace una concatenacion usando la funcion join de la Clase Picture
# 4 veces concatenamos queen
result = queen.join(queen.join(queen.join(queen)))

draw(result)