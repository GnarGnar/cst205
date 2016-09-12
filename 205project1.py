"""
Abstract: Goes through 9 images finding the median value of its pixels and putting it in a new images
Author: Kieran Burke
Date:9/3/16
Github: https://github.com/GnarGnar/cst205

Takes a while to run but it works
"""

from PIL import Image
import statistics

myimage1= Image.open("1.png")
myimage2= Image.open("2.png")
myimage3= Image.open("3.png")
myimage4= Image.open("4.png")
myimage5= Image.open("5.png")
myimage6= Image.open("6.png")
myimage7= Image.open("7.png")
myimage8= Image.open("8.png")
myimage9= Image.open("9.png")
size = myimage1.size
width, height = myimage1.size
myimage10 = Image.new(myimage1.mode,myimage1.size);

 

pixels =[]
newImagePixels =[]


pixel_values1 = list(myimage1.getdata())
pixel_values2 = list(myimage2.getdata())
pixel_values3 = list(myimage3.getdata())
pixel_values4 = list(myimage4.getdata())
pixel_values5 = list(myimage5.getdata())
pixel_values6 = list(myimage6.getdata())
pixel_values7 = list(myimage7.getdata())
pixel_values8 = list(myimage8.getdata())
pixel_values9 = list(myimage9.getdata())



for x in range(0,len(pixel_values1)-1):
	pixels.append(pixel_values1[x])
	pixels.append(pixel_values2[x])
	pixels.append(pixel_values3[x])
	pixels.append(pixel_values4[x])
	pixels.append(pixel_values5[x])
	pixels.append(pixel_values6[x])
	pixels.append(pixel_values7[x])
	pixels.append(pixel_values8[x])
	pixels.append(pixel_values9[x])
	pixels.sort()
	newImagePixels.append(pixels[5])
	for x in range(0,9):
		pixels.pop()
	
myimage10.putdata(newImagePixels)
myimage10.show()