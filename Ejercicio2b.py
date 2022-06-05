from interpreter import draw
from chessPictures import *
# Creo un caballo negativo
negativeK= knight.negative()
# creo la primera linea con el caballo normal y con join agrego el caballo Negativo
firstLine = knight.join(negativeK)
#creo el caballo negativo invertido verticalmente 
negativeInv = negativeK.verticalMirror()
#creo la segunda linea con el caballo negativativamente invertido y con join agrego 
#el caballo normal invertido verticalmente
secondLine = negativeInv.join(knight.verticalMirror())
#con la funcion up agrego la primera linea y la segunda linea
result = firstLine.up(secondLine)

draw(result)