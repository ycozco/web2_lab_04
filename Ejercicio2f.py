from interpreter import draw
from chessPictures import *

from interpreter import draw
from chessPictures import *

#Esta linea dibuja intercala cuadros blancos y negros para que haya 4 cuadrados verticales
image = Picture(square.negative().img+square.img).verticalRepeat(2)

#A continuacion, junta la linea image con su negativo y todo este conjunto lo repite 4 veces
draw(image.join(image.negative()).horizontalRepeat(4))
