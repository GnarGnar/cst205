"""
Abstract: Goes through 9 images finding the median value of its pixels and putting it in a new images
Author: Kieran Burke
Date:9/3/16

Takes a while to run but it works
"""

from PIL import Image
import statistics

myimage1= Image.open("1.png")
px1 = myimage1.load()
myimage2= Image.open("2.png")
px2 = myimage2.load()
myimage3= Image.open("3.png")
px3 = myimage3.load()
myimage4= Image.open("4.png")
px4 = myimage4.load()
myimage5= Image.open("5.png")
px5 = myimage5.load()
myimage6= Image.open("6.png")
px6 = myimage6.load()
myimage7= Image.open("7.png")
px7 = myimage7.load()
myimage8= Image.open("8.png")
px8 = myimage8.load()
myimage9= Image.open("9.png")
px9 = myimage9.load()
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
	newImagePixels.append(pixels[4])
	pixels.pop()
	pixels.pop()
	pixels.pop()
	pixels.pop()
	pixels.pop()
	pixels.pop()
	pixels.pop()
	pixels.pop()
	pixels.pop()
	print("Working on it")
	
	

	


myimage10.putdata(newImagePixels)
myimage10.show()