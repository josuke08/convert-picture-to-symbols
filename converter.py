from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io
import numpy

symbols = [
"@",
"$",
"%",
"&",
"£",
"*",
";",
":",
",",
".",
" "]

def getSymbol(value):
    size = len(symbols)
    for i in range(0, size):
        if value <= int(255 / size) * (i + 1):
            return symbols[i]
    return symbols[size - 1]

image = Image.open('./input.png')
pixels = image.load()
print(pixels[0,0])

filtered = image.convert("L")
pixels = filtered.load()

print(image.size)

width, height = image.size
    
print("width: " + str(width))
print("length: " + str(height))

file = open("outpt.txt", "a")
lines = ""

i = 0
while i < height:
    line = ""

    j = 0
    while j < width:

        try:
            line = line + getSymbol(pixels[j, i])
        except:
            print(str(i) + " " + str(j))
            break
                
        j += 1
    i += 1

    lines = lines + line + "\n"

file.write(lines)
newImage = Image.new('L', (width*6, height*11), 255)
d = ImageDraw.Draw(newImage)
d.text((0,0), lines, fill=0, spacing=0)
newImage.show()

print("end")
