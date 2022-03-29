# LSb Encoding:

import numpy as np
import PIL.Image

message_to_hide = "This is my secret message mate!"

image = PIL.Image.open('psgcaslogo.png', 'r')
print(image)
width , height = image.size
print(width,height)

img_arr = np.array(list(image.getdata()))
print(img_arr)

if image.mode == "P":
    print("Not Supported File format")
    exit()

channels = 4 if image.mode == "RGBA" else 3

pixels = img_arr.size // channels

stop_indicator = "$Saro-End-File$"
stop_indicator_length = len(stop_indicator)

message_to_hide += stop_indicator
print(message_to_hide)

byte_message = ''.join(f"{ord(c):08b}" for c in message_to_hide )# c = character

print (byte_message)

bits = len(byte_message)

if bits > pixels:
    print("Not Enough space available to hide the data ")
    exit()
else:
    index = 0;
    for i in range(pixels):
        for j in range(0,3):
            if index < bits:
                img_arr[i][j] = int(bin(img_arr[i][j])[2:-1] + byte_message[index], 2) #0b1010101110
                index += 1

img_arr = img_arr.reshape((height,width,channels))
result = PIL.Image.fromarray(img_arr.astype('uint8'), image.mode)
result.save('encode.png')