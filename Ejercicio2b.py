from interpreter import draw
from chessPictures import *
negativeK= knight.negative()
firstLine = knight.join(negativeK)
negativeInv = negativeK.verticalMirror()
secondLine = negativeInv.join(knight.verticalMirror())
result = firstLine.up(secondLine)

draw(result)