from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    horizontal = []
    for tmp  in self.img:
      horizontal.insert(0,tmp)
    return Picture(horizontal)

  def negative(self):
    negative = []
    iteration = '';
    for value in self.img:
      for char in value:
        iteration += self._invColor(char)
      negative.append(iteration)
      iteration = ''
    return Picture(negative)

  def join(self, p):
    joined = []
    position = 0
    for tmp in self.img:
      joined.append(tmp + " " +p.img[position])
      position += 1
    return Picture(joined)

  def up(self, p):
    
    image = self.img
    image.extend(p.img)
    return Picture(image)


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

  def horizontalRepeat(self, n):
    image = []	
    for i in range(0, len(self.img)):
      image.append(self.img[i] * n)
    return Picture(image)

  def verticalRepeat(self, n):
    VRepeat = []
    i = 0
    while i < n:
      i += 1
      for value in self.img:
        VRepeat.append(value)
    return Picture(VRepeat)

  #Extra: Sólo para realmente viciosos 
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

