from interpreter import draw
from chessPictures import *
negativeK= knight.negative()
firstLine = knight.join(negativeK)
secondLine = negativeK.join(knight)
result = secondLine.under(secondLine)
draw(result)