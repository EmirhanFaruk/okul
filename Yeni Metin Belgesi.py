
# Modification date: Mon Dec  7 09:42:10 2020

# Production date: Sun Sep  3 15:43:50 2023

from PIL import Image
im = Image.new("RGB" , (800 ,800),"white")

def carrenoir(x, y):
    for i in range(x, x + 100):
      for j in range(y, y + 100):
          im.putpixel((i, j), (0, 0, 0))


for i in range(0, 800, 200):
    for j in range(0, 700, 200):
        carrenoir(i, j)

for i in range(100, 800, 200):
    for j in range(100, 800, 200):
        carrenoir(i, j)


im.show()
im.save("chess.png", "png")
