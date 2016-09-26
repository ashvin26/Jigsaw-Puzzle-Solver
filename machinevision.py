#Ashvin Venkatesan
#2/9/15
#Machine Vision

import math
neighbors = []
edges = []
graypixels = []
Gvalues = []
Gxvalues = []
Gyvalues = []
current = 0
#hardcoded width and length(height) of the image
w = 620
l = 585
def grayScale():
  global data  
  with open('jigsawtemplate.ppm', 'r') as ppm:
    data = ppm.read()
  encoding, height, width, maxColorValue, *values = data.split()
  y = 0
  y2 = 0
  y3 = 0
  y4 = 0
  y5 = 0
  for x in range(w):
    row = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    while y < l * 3 * (x + 1):
      row.append(values[y])
      row2.append(0)
      row3.append(0)
      row4.append(0)
      row5.append(0)
      y += 3
      y2 += 3
      y3 += 3
      y4 += 3
      y5 += 3
    graypixels.append(row)
    edges.append(row2)
    Gvalues.append(row3)
    Gxvalues.append(row4)
    Gyvalues.append(row5)

  f = open('gray.ppm', 'w')
  f.write(encoding + '\n')
  f.write(height + " " + width + '\n')
  f.write(maxColorValue + '\n')

  for x in range(0, len(values), 3):
    red = int(values[x])
    green = int(values[x + 1])
    blue = int(values[x + 2])
    gray = int(0.30 * red + 0.59 * green + 0.11 * blue)
    for y in range(3):
      f.write(str(gray) + "\n")

def blur(arr):
  encoding, height, width, maxColorValue, *values = data.split()
  f = open('blur.ppm', 'w')
  f.write(encoding + '\n')
  f.write(height + " " + width + '\n')
  f.write(maxColorValue + '\n')
  
  for r in range(w):
    for c in range(l):
      if c == 0:
        for y in range(3):
          f.write(str(arr[r][0]) + '\n')
      elif c == l - 1:
        for y in range(3):
          f.write(str(arr[r][l - 1]) + '\n')
      elif r == 0:
        for y in range(3):
          f.write(str(arr[0][c]) + '\n')
      elif r == w - 1:
        for y in range(3):
          f.write(str(arr[w - 1][c]) + '\n')
      else:
        neighbors.append(int(arr[r + 1][c]))
        neighbors.append(int(arr[r - 1][c]))
        neighbors.append(int(arr[r][c + 1]))
        neighbors.append(int(arr[r][c - 1]))
        neighbors.append(int(arr[r + 1][c + 1]))
        neighbors.append(int(arr[r + 1][c - 1]))
        neighbors.append(int(arr[r - 1][c + 1]))
        neighbors.append(int(arr[r - 1][c - 1]))
        current = int((neighbors[0] + neighbors[1] + neighbors[2] + neighbors[3] + neighbors[4] + neighbors[5] + neighbors[6] + neighbors[7])/ 8)
        arr[r][c] = current
        for y in range(3):
          f.write(str(current) + '\n')
        del neighbors[:]
def edgeDetection(arr, edges):
  Gx = []
  Gxr1 = [-1, 0, 1]
  Gxr2 = [-2, 0, 2]
  Gxr3 = [-1, 0, 1]
  Gx.append(Gxr1)
  Gx.append(Gxr2)
  Gx.append(Gxr3)
  
  Gy = []
  Gyr1 = [1, 2, 1]
  Gyr2 = [0, 0, 0]
  Gyr3 = [-1, -2, -1]
  Gy.append(Gyr1)
  Gy.append(Gyr2)
  Gy.append(Gyr3)
  
  
  encoding, height, width, maxColorValue, *values = data.split()
  f = open('edges.ppm', 'w')
  f.write(encoding + '\n')
  f.write(height + " " + width + '\n')
  f.write(maxColorValue + '\n')
  for r in range(w):
    for c in range(l):
      if c == 0:
        for y in range(3):
          f.write(str(arr[r][0]) + '\n')
      elif c == l - 1:
        for y in range(3):
          f.write(str(arr[r][l - 1]) + '\n')
      elif r == 0:
        for y in range(3):
          f.write(str(arr[0][c]) + '\n')
      elif r == w - 1:
        for y in range(3):
          f.write(str(arr[w - 1][c]) + '\n')
      else:
        
        neighbors.append((int(arr[r - 1][c - 1]) * Gx[0][0]))
        neighbors.append((int(arr[r - 1][c]) * Gx[0][1]))
        neighbors.append((int(arr[r - 1][c + 1]) * Gx[0][2]))
        neighbors.append((int(arr[r][c - 1]) * Gx[1][0]))
        neighbors.append((int(arr[r][c + 1]) * Gx[1][2]))
        neighbors.append((int(arr[r + 1][c - 1]) * Gx[2][0]))
        neighbors.append((int(arr[r + 1][c]) * Gx[2][1]))    
        neighbors.append((int(arr[r + 1][c + 1]) * Gx[2][2]))        
        
        gxvalue = int((neighbors[0] + neighbors[1] + neighbors[2] + neighbors[3] + neighbors[4] + neighbors[5] + neighbors[6] + neighbors[7])/ 8)
        gxvalueabs = math.fabs(int((neighbors[0] + neighbors[1] + neighbors[2] + neighbors[3] + neighbors[4] + neighbors[5] + neighbors[6] + neighbors[7])/ 8))
        del neighbors[:]
        
        neighbors.append((int(arr[r - 1][c - 1]) * Gy[0][0]))
        neighbors.append((int(arr[r - 1][c]) * Gy[0][1]))
        neighbors.append((int(arr[r - 1][c + 1]) * Gy[0][2]))
        neighbors.append((int(arr[r][c - 1]) * Gy[1][0]))
        neighbors.append((int(arr[r][c + 1]) * Gy[1][2]))
        neighbors.append((int(arr[r + 1][c - 1]) * Gy[2][0]))
        neighbors.append((int(arr[r + 1][c]) * Gy[2][1]))    
        neighbors.append((int(arr[r + 1][c + 1]) * Gy[2][2]))        
        
        gyvalue = int((neighbors[0] + neighbors[1] + neighbors[2] + neighbors[3] + neighbors[4] + neighbors[5] + neighbors[6] + neighbors[7])/ 8)
        gyvalueabs = math.fabs(int((neighbors[0] + neighbors[1] + neighbors[2] + neighbors[3] + neighbors[4] + neighbors[5] + neighbors[6] + neighbors[7])/ 8))
        del neighbors[:]    
        
        Gxvalues[r][c] = gxvalue
        Gyvalues[r][c] = gyvalue
        G = gxvalueabs + gyvalueabs
        Gvalues[r][c] = G
        if G > 18:
          edges[r][c] = 1
          f.write('255 ' + '0 ' + '0' + '\n')
        else:
          f.write('255 ' + '255 ' + '255' + '\n')
def thinning(arr, edges):
  encoding, height, width, maxColorValue, *values = data.split()
  f = open('thinned.ppm', 'w')
  f.write(encoding + '\n')
  f.write(height + " " + width + '\n')
  f.write(maxColorValue + '\n')
  for r in range(w):
    for c in range(l):
      if edges[r][c] == 0:
        f.write('255 ' + '255 ' + '255' + '\n')
      if edges[r][c] == 1:
        if edges[r + 1][c - 1] == 1 and edges[r + 1][c] == 1 and edges[r + 1][c + 1] == 1 and edges[r - 1][c - 1] == 0 and edges[r - 1][c] == 0 and edges[r - 1][c + 1] == 0:
          f.write('255 ' + '0 ' + '0' + '\n')
        elif edges[r][c - 1] == 1 and edges[r + 1][c] == 1 and edges[r][c + 1] == 0 and edges[r - 1][c] == 0 and edges[r - 1][c + 1] == 0:
          f.write('255 ' + '0 ' + '0' + '\n')
        elif edges[r + 1][c + 1] == 1 and edges[r + 1][c] == 1 and edges[r + 1][c - 1] == 1 and edges[r][c - 1] == 1 and edges[r][c + 1] == 1 and edges[r - 1][c - 1] == 1 and edges[r - 1][c] == 1 and edges[r - 1][c + 1] == 1:
          f.write('255 ' + '0 ' + '0' + '\n')
        elif edges[r + 1][c] == 1 and edges[r][c - 1] == 1 and edges[r][c + 1] == 1 and edges[r + 1][c] == 1:
          f.write('255 ' + '0 ' + '0' + '\n')
        elif edges[r - 1][c - 1] == 0 and edges[r - 1][c] == 0 and edges[r - 1][c + 1] == 0 and edges[r][c - 1] == 0 and edges[r][c + 1] == 0 and edges[r + 1][c - 1] == 0:
          f.write('255 ' + '0 ' + '0' + '\n')
        elif edges[r - 1][c - 1] == 0 and edges[r - 1][c] == 0 and edges[r - 1][c + 1] == 0 and edges[r][c - 1] == 0 and edges[r][c + 1] == 0 and edges[r + 1][c + 1] == 0:
          f.write('255 ' + '0 ' + '0' + '\n')
        else:
          f.write('255 ' + '255 ' + '255' + '\n')
def thinning2(arr, edges, Gvalues, Gxvalues, Gyvalues):
  encoding, height, width, maxColorValue, *values = data.split()
  f = open('thinned2.ppm', 'w')
  f.write(encoding + '\n')
  f.write(height + " " + width + '\n')
  f.write(maxColorValue + '\n')
  for r in range(w):
    for c in range(l):
      if edges[r][c] == 1:
        theta = float(math.atan2(Gyvalues[r][c], Gxvalues[r][c]))
        theta = theta * (180/math.pi)
        if theta == 0 or theta == 180 or theta == -180 or theta == -0:
          if Gvalues[r][c] > Gvalues[r][c + 1] and Gvalues[r][c] > Gvalues[r][c - 1]:
            f.write('255 ' + '0 ' + '0' + '\n')
          else:
            f.write('255 ' + '255 ' + '255' + '\n')
        elif theta > 0 and theta < 90 or theta > 180 and theta < 270 or theta < -90 and theta > -180:
          if Gvalues[r][c] > Gvalues[r - 1][c + 1] and Gvalues[r][c] > Gvalues[r + 1][c - 1]:
            f.write('255 ' + '0 ' + '0' + '\n')
          else:
            f.write('255 ' + '255 ' + '255' + '\n')
        elif theta == 90 or theta == -270 or theta == 270 or theta == -90:
          if Gvalues[r][c] > Gvalues[r + 1][c] and Gvalues[r][c] > Gvalues[r - 1][c]:
            f.write('255 ' + '0 ' + '0' + '\n')
          else:
            f.write('255 ' + '255 ' + '255' + '\n')
        elif theta > 90 and theta < 180 or theta > 270 and theta < 360 or theta < 0 and theta > -90:
          if Gvalues[r][c] > Gvalues[r - 1][c - 1] and Gvalues[r][c] > Gvalues[r + 1][c + 1]:
            f.write('255 ' + '0 ' + '0 ' + '\n')
          else:
            f.write('255 ' + '255 ' + '255' + '\n')
      else:
        f.write('255 ' + '255 ' + '255' + '\n')
#def lineDetection(arr, edges):
  
  
def voting(arr, edges, Gvalues, Gxvalues, Gyvalues):
  votingmatrix = [[0 for x in range(700)] for x in range(700)]
  encoding, height, width, maxColorValue, *values = data.split()
  f = open('votes.ppm', 'w')
  f.write(encoding + '\n')
  f.write(height + " " + width + '\n')
  f.write(maxColorValue + '\n')
  for r in range(w):
    for c in range(l):
      if edges[r][c] == 1:
        theta = float(math.atan2(Gyvalues[r][c], Gxvalues[r][c]))
        theta = theta * (180/math.pi)
        if theta == 0 or theta == 180 or theta == -180 or theta == -0:
          x = r
          y = c
          while y + 1 != l:
            votingmatrix[x][y] += 1
            y += 1
          y = c - 1
          while y - 1 != 0:
            votingmatrix[x][y] += 1
            y -= 1
        elif theta > 0 and theta < 90 or theta > 180 and theta < 270 or theta < -90 and theta > -180:
          x = r
          y = c
          while y <= l and x >= 0:
            votingmatrix[x][y] += 1
            x -= 1
            y += 1
          x = r - 1
          y = c - 1
          while y >= 0 and x <= w:
            votingmatrix[x][y] += 1
            x += 1
            y -= 1            
        elif theta == 90 or theta == -270 or theta == 270 or theta == -90:
          x = r
          y = c
          while x + 1 != w:
            votingmatrix[x][y] += 1
            x += 1
          x = r - 1
          while x - 1 != 0:
            votingmatrix[x][y] += 1
            x -= 1
        elif theta > 90 and theta < 180 or theta > 270 and theta < 360 or theta < 0 and theta > -90:
          x = r
          y = c
          while y <= l and x <= w:
            votingmatrix[x][y] += 1
            x += 1
            y += 1
          x = r - 1
          y = c - 1
          while y >= 0 and x >= 0:
            votingmatrix[x][y] += 1
            x -= 1
            y -= 1
  print(votingmatrix)    
grayScale()
num = input('Enter number of times for picture to be blurred: ')
if int(num) == 0:
  print("Done.")
else:
  for i in range(int(num)):
    blur(graypixels)
    print("Done.")
b = input("Edge Detection? (Y or N) ")
if b == 'y' or b == 'Y':
  edgeDetection(graypixels, edges)
  print("Done.")
else:
  print("Done.")
c = input("Thinning? (Y or N) ")
if c == 'y' or c == 'Y':
  #thinning(graypixels, edges)
  thinning2(graypixels, edges, Gvalues, Gxvalues, Gyvalues)
  print("Done.")
#if c == 'y' or c == 'Y':
  #lineDetection(graypixels, edges)
#c = input("Circle Detection? (Y or N) ")
#if c == 'y' or c == 'Y':
  #voting(graypixels, edges, Gvalues, Gxvalues, Gyvalues)

    
    
    
    
    
    
