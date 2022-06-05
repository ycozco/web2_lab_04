from interpreter import draw
from chessPictures import *

# Este programa dibuja una linea de recuadros de ajedrez
draw(square.join(square.negative()).horizontalRepeat(4))