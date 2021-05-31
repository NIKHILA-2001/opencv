from google.colab.patches import cv2_imshow
from PIL import Image,ImageEnhance,ImageFilter
img = Image.open("images/flower.JPG")
#image Resolution
print(img.size)
new_size = (300,300)
img_resize = img.resize(new_size)
img_resize.save("output/resize.jpg")
#brightness
enhancer = ImageEnhance.Brightness(img)
#bright
img_bright = enhancer.enhance(1.8)
img_bright.save("output/bright.jpg")
#dark
img_dark = enhancer.enhance(0.6)
img_dark.save("output/dark.jpg")
# b/w -->grayscale
img_gray = img.convert("L")
img_gray.save("output/gray.jpg")
# sharp
img_sharp = img.filter(ImageFilter.SHARPEN)
img_sharp.save("output/sharp.jpg")
# blur
img_blur = img.filter(ImageFilter.BLUR)
img_blur.save("output/blur.jpg")
#find edge
# blur
img_blur = img.filter(ImageFilter.FIND_EDGES)
img_blur.save("output/edge.jpg")
