from PIL import Image
from IPython.display import display
import random
import json
import os

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

face, ears, eyes, hair, mouth, nose = [],[],[],[],[],[]

face_amount = os.listdir("./sources/face/")
for i in range(len(face_amount)):
    face.append(("face" + str(i+1)))
ears_amount = os.listdir("./sources/ears/")
for i in range(len(ears_amount)):
    ears.append(("ears" + str(i+1)))
eyes_amount = os.listdir("./sources/eyes/")
for i in range(len(eyes_amount)):
    eyes.append(("eyes" + str(i+1)))
hair_amount = os.listdir("./sources/hair/")
for i in range(len(hair_amount)):
    hair.append(("hair" + str(i+1)))
mouth_amount = os.listdir("./sources/mouth/")
for i in range(len(mouth_amount)):
    mouth.append(("m" + str(i+1)))
nose_amount = os.listdir("./sources/nose/")
for i in range(len(nose_amount)):
    nose.append(("n" + str(i+1)))

print(face,ears,eyes,hair,mouth,nose)

## Generate Traits

TOTAL_IMAGES = 100 # Number of random unique images we want to generate

all_images = []

# A recursive function to generate unique image combinations
def create_new_image():

    new_image = {} #

    # For each trait category, select a random trait based on the weightings
    new_image["face"] = random.choices(face)[0]
    new_image["ears"] = random.choices(ears)[0]
    new_image["eyes"] = random.choices(eyes)[0]
    new_image["hair"] = random.choices(hair)[0]
    new_image["mouth"] = random.choices(mouth)[0]
    new_image["nose"] = random.choices(nose)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image

# Generate the unique combinations
for i in range(TOTAL_IMAGES):
    new_trait_image = create_new_image()
    all_images.append(new_trait_image)

#### Generate Images with custom tokenIDs
i = 0
os.mkdir(f'./images')
for item in all_images:

    item["tokenId"] = i
    i = i + 1

    im1 = Image.open(f'./sources/face/{item["face"]}.png').convert('RGBA')
    im2 = Image.open(f'./sources/eyes/{item["eyes"]}.png').convert('RGBA')
    im3 = Image.open(f'./sources/ears/{item["ears"]}.png').convert('RGBA')
    im4 = Image.open(f'./sources/hair/{item["hair"]}.png').convert('RGBA')
    im5 = Image.open(f'./sources/mouth/{item["mouth"]}.png').convert('RGBA')
    im6 = Image.open(f'./sources/nose/{item["nose"]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)

    #Convert to RGB
    rgb_im = com5.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)
