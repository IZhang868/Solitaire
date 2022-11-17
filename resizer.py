from PIL import Image
import glob
import os

root_dir = 'H:/AP COMP SCI P/New folder/PNG/'

lst_imgs = [i for i in glob.glob(root_dir + '*.png', recursive=True)]

if not "ltl" in os.listdir():
    os.mkdir("ltl")
    
print(lst_imgs)
for i in lst_imgs:
    img = Image.open(i)
    imgL = img.resize((200, 306), Image.Resampling.LANCZOS)
    
    imgL.save(i[:-4] + "_ltl.png", 'PNG', quality=90)
    
    
print("Done")
os.startfile("ltl")