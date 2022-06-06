# web2_lab_04
<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AUGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
                  </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía del Estudiante / Talleres / Centros de Simulación</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DEL ESTUDIANTE</span><br />
<span>(formato del estudiante)</span>
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Practica 03</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA INICIO::</td><td>MAY-2022</td><td>FECHA FIN:</td><td>05-Jun-2022</td><td>DURACIÓN:</td><td>04 horas</td>
</tr>
<tr><td colspan="6">INTEGRANTES:
<ul>
<li>Cozco Mauri Yoset --------------------ycozco@unsa.edu.pe</li>
<li>César Alejandro Garay Bedregal--------cgarayb@unsa.edu.pe</li>
<li>Vladimir Sulla Quispe-----------------vsullaq@unsa.edu.pe</li>
</ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTES:
<ul>
<li>Richart Smith Escobedo Quispe (rescobedoq@unsa.edu.pe)</li>
</ul>
</td>
</<tr>
</tdbody>
</table>




<table>
<theader>
<tr><th colspan="6">SOLUCIÓN Y RESULTADOS</th></tr>
</theader>
<tbody>
</tr>
<tr><td colspan="6">
<tr>
#I. SOLUCIÓN DE EJERCICIOS PROBLEMAS:
A. <br><br>
-   verticalMirror: Devuelve el espejo vertical de la imagen.
    
```python
    def verticalMirror(self):
        vertical = []
        for value in self.img:
            # recorremos self y agregamos en vertical desde el ultimo valor hacia el inicial
            vertical.append(value[::-1])
        #retornamos el arreglo como Picture
        return Picture(vertical)
```
</tr>
<tr>
-   horizontalMirror: Devuelve el espejo horizontal de la imagen.

```python
  def horizontalMirror(self):
    horizontal = []
    for tmp  in self.img:
      horizontal.insert(0,tmp)
    #igualmente se devuelve de la forma Picture(horizontal) para que se figura(Picture)   
    return Picture(horizontal)
```
</tr><tr>
-   negative: Devuelve un negativo de la imagen.

```python
  def negative(self):
    negative = []
    iteration = '';
    for value in self.img:
      for char in value:
        iteration += self._invColor(char)
      negative.append(iteration)
      iteration = ''
    return Picture(negative)
```
</tr><tr>
-   join: Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual.

```python
  def join(self, p):
    joined = []
    position = 0
    for tmp in self.img:
      joined.append(tmp + " " +p.img[position])
      position += 1
    return Picture(joined)
```
</tr><tr>
-   up: Devuelve una nueva figura poniendo la figura recibida como argumento, encima de la figura actual.

```python
  def up(self, p):
    image = self.img
    image.extend(p.img)
    return Picture(image)
```
</tr><tr>
-   under: Devuelve una nueva figura poniendo la figura recibida como argumento, sobre la figura actual.

```python
  def under(self, p):
    image = []
    for i in range(0, len(p.img)):
      line = ""
      for j in range(0, len(p.img[i])):
        if (p.img[i][j] == " "):
          line += self.img[i][j]
        else:
          line += p.img[i][j]
      image.append(line)
    return Picture(image)
```
</tr><tr>
-   horizontalRepeat, Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n.

```python
  def horizontalRepeat(self, n):
    image = []	
    for i in range(0, len(self.img)):
      image.append(self.img[i] * n)
    return Picture(image)
```
</tr><tr>
-   verticalRepeat Devuelve una nueva figura repitiendo la figura actual debajo, la cantidad de veces que indique el valor de n

```python
  def verticalRepeat(self, n):
    VRepeat = []
    i = 0
    while i < n:
      i += 1
      for value in self.img:
        VRepeat.append(value)
    return Picture(VRepeat)
```
</tr><tr>
-   #Extra: Sólo para realmente viciosos 

```python
  def rotate(self):
    rotate = []
    i = 0
    for value in self.img:
      rotate.append(value[0]) # Este bucle hará que nuestro arreglo tenga el tamaño del arreglo de la figura
    while i < len(rotate):
      for value in self.img:
        rotate[i] += value[i]
      i += 1
    return Picture(rotate)
```
</tr>

## B. Usando únicamente los métodos de los objetos de la clase Picture dibuje las siguientes figuras (invoque a draw):<br>
</td><tr>

## Ejercicio2 a)

```python
from interpreter import draw
from chessPictures import *
#Creo un Picture de la imagen del caballo negro
negativeK= knight.negative()
#Creo en un Picture la primera linea incluyendo un caballo y el caballo(negativo)
firstLine = knight.join(negativeK)
#Creo en un Picture la segunda liena incluyenda el caballo(negativo) y el caballo
secondLine = negativeK.join(knight)
#Usando la funcion up de Picture, creo un Picture con la primera linea y la segunda linea
result = firstLine.up(secondLine)
draw(result)
```
![Ejercicio2_a](results/ejercicio2_a.png)
</tr><tr><br>

## Ejercicio2 b)

```python
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
```
![Ejercicio2_b](results/ejercicio2_b.png)
</tr><tr><br>

## Ejercicio2 c)

```python
from interpreter import draw
from chessPictures import *
# Ejercicio 2c 
# Se hace una concatenacion usando la funcion join de la Clase Picture
# 4 veces concatenamos queen
result = queen.join(queen.join(queen.join(queen)))
draw(result)
```

![Ejercicio2_c](results/ejercicio2_c.png)
</tr><tr><br>

## Ejercicio2 d)

```python
from interpreter import draw
from chessPictures import *
# Este programa dibuja una linea de recuadros de ajedrez
draw(square.join(square.negative()).horizontalRepeat(4))
```

![Ejercicio2_d](results/ejercicio2_d.png)
</tr><tr><br>

## Ejercicio2 e)

```python
from interpreter import draw
from chessPictures import *

# Programa que dibuja recuadros de un tablero de ajedrez
# A diferencia de Ejercicio2c este cambia los colores
draw(square.negative().join(square).horizontalRepeat(4))
```

![Ejercicio2_e](results/ejercicio2_e.png)
</tr><tr><br>

## Ejercicio2 f)

```python
from interpreter import draw
from chessPictures import *

from interpreter import draw
from chessPictures import *

#Image es una linea de cuadros de ajedrez vertical
image = Picture(square.negative().img+square.img).verticalRepeat(2)

#Esta parte junta la parte negativa de image con image y la repite cuatro veces 
draw(image.join(image.negative()).horizontalRepeat(4))

```

![Ejercicio2_f](results/ejercicio2_f.png)
</tr><tr><br>

## Ejercicio2 g)

```python
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
```

![Ejercicio2_g](results/ejercicio2_g.png)
</tr>


<tr><td colspan="6">II. SOLUCIÓN DE CUESTIONARIO: <br>

-   ¿Qué son los archivos *.pyc?
    Los archivos .pyc son creados por el intérprete de Python cuando se importa un archivo .py. Contienen el "código de bytes compilado" del módulo/programa importado para que la "traducción" del código fuente al código de bytes (que solo debe hacerse una vez) se pueda omitir en importaciones posteriores si el .pyc es más nuevo que el .py correspondiente archivo.Una vez que se genera el archivo *.pyc, no es necesario el archivo *.py, a menos que lo edite.Este archivo contiene el código de bytes para que importarlo más tarde sea más fácil (y rápido)

-   ¿Para qué sirve el directorio __pycache__?

-   ¿Cuáles son los usos y lo que representa el subguión en Python?


</tr>
 
</tr>
<tr><td colspan="6">III. CONCLUSIONES:

-   
-   
-   
</tr>

</tdbody>
</table>


<table>
<theader>
<tr><th colspan="6">RETROALIMENTACIÓN GENERAL</th></tr>
</theader>
<tbody>
</tr>
<tr><td colspan="6">
<ul>
<li><a </a></li>
<li><a </a></li>
<li><a </a></li>
</ul>
</td>
</<tr>
</tdbody>
</table>


<table>
<theader>
<tr><th colspan="6">REFERENCIAS BIBLIOGRÁFICAS</th></tr>
</theader>
<tbody>
</tr>
<tr><td colspan="6">
<ul>
<li>https://www.tutorialspoint.com/What-are-pyc-files-in-Python#:~:text=pyc%20files%20are%20created%20by,is%20newer%20than%20the%20corresponding%20.</li>
<li>https://stackoverflow.com/questions/8822335/what-do-the-python-file-extensions-pyc-pyd-pyo-stand-for#:~:text=you've%20written.-,.,later%20easier%20(and%20faster).
</li>
<li>https://web.archive.org/web/20160130165632/http://www.network-theory.co.uk/docs/pytut/CompiledPythonfiles.html
</li>

<li></li>
</ul>
</td>
</<tr>
</tdbody>
</table>

