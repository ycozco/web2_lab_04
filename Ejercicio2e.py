from interpreter import draw
from chessPictures import *

#Image es una linea de cuadros de ajedrez vertical
image = Picture(square.negative().img+square.img).verticalRepeat(2)

#Esta parte junta la parte negativa de image con image y la repite cuatro veces 
draw(image.join(image.negative()).horizontalRepeat(4))