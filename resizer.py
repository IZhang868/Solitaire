from PIL import Image
import glob
import os

lst_imgs = [i for i in glob.glob('*.png')]

if not "ltl" in os.listdir():
    os.mkdir("ltl")
    
print(lst_imgs)
for i in lst_imgs:
    img = Image.open(i)
    img = (img.resize(200, 306), Image.ANTIALIAS)
    img.save("ltl\\" + i[:-4] + "_ltl.png")
    
    
print("Done")
os.startfile("ltl")