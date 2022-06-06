from interpreter import draw
from chessPictures import *

# Programa que dibuja recuadros de un tablero de ajedrez
# Este programa junta un cuadro oscuro con uno claro, y lo repite 4 veces
draw(square.negative().join(square).horizontalRepeat(4))
