from interpreter import draw
from chessPictures import *

# Este programa junta un cuadro de ajedrez con uno de color oscuro, y lo repite 4 veces
draw(square.join(square.negative()).horizontalRepeat(4))
