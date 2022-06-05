from interpreter import draw
from chessPictures import *

# Preparamos todas las piezas en su versión negativa
torreNegra = rock.negative()
caballoNegro = knight.negative()
alfilNegro = bishop.negative()
reynaNegra = queen.negative()
reyNegro = king.negative()
peonNegro = pawn.negative()
cuadradoNegro = square.negative()

# Posicionamos todas las fichas negras en distintos cuadrados ; CO = Cuadro Oscuro - CC = Cuadro Claro
torreNegraCC = square.under(torreNegra)
caballoNegroCC = square.under(caballoNegro)
alfilNegroCC = square.under(alfilNegro)
peonNegroCC = square.under(peonNegro)
torreNegraCO = cuadradoNegro.under(torreNegra)
caballoNegroCO = cuadradoNegro.under(caballoNegro)
alfilNegroCO = cuadradoNegro.under(alfilNegro)
peonNegroCO = cuadradoNegro.under(peonNegro)

# Posicionamos todas las fichas blancas en distintos cuadrados ; CO = Cuadro Oscuro - CC = Cuadro Claro
torreCC = square.under(rock)
caballoCC = square.under(knight)
alfilCC = square.under(bishop)
peonCC = square.under(pawn)
torreCO = cuadradoNegro.under(rock)
caballoCO = cuadradoNegro.under(knight)
alfilCO = cuadradoNegro.under(bishop)
peonCO = cuadradoNegro.under(pawn)

# La reyna negra unicamente esta posicionada sobre un cuadrado oscuro
reynaNegra = cuadradoNegro.under(reynaNegra)

# El rey negro unicamente esta posicionado sobre un cuadrado claro
reyNegro = (square).under(reyNegro)

# La reyna blanca unicamente esta posicionada sobre un cuadrado claro
reyna = (square).under(queen)

# El rey blanco unicamente esta posicionado sobre un cuadrado oscuro
rey = cuadradoNegro.under(king)

# En las siguientes lineas de código se genera cada una de las filas del tablero
fila1 = torreNegraCC.join(caballoNegroCO).join(alfilNegroCC).join(reynaNegra).join(reyNegro).join(alfilNegroCO).join(caballoNegroCC).join(torreNegraCO)
fila2 = (peonNegroCO.join(peonNegroCC)).horizontalRepeat(4)
aux1 = (square.join(cuadradoNegro).horizontalRepeat(4))    # Los aux nos sirven para preparar lineas que se repetiran verticalmente
aux2 = aux1.verticalMirror()
fila3a6 = aux1.up(aux2).verticalRepeat(2)
fila7 = (peonCC.join(peonCO)).horizontalRepeat(4)
fila8 = torreCO.join(caballoCC).join(alfilCO).join(reyna).join(rey).join(alfilCC).join(caballoCO).join(torreCC)

# Este draw une todas las filas creadas anteriormente y se genera el tablero completo
draw(fila1.up(fila2.up(fila3a6.up(fila7.up(fila8)))))