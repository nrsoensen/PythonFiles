from PIL import Image
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    image = Image.open(filename)
    return image


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(img):
    img.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(img, filename):
    img.save(filename)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.

def obamicon(img):
    newdata = []
    data = list(img.getdata())
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)
    for i in range(len(data)):
        intensity = data[i][0] + data[i][1] + data[i][2]
        if intensity < 182:
            newdata.append(darkBlue)
        elif intensity < 364:
            newdata.append(red)
        elif intensity < 546:
            newdata.append(lightBlue)
        else:
            newdata.append(yellow)
    img.putdata(newdata)
    img.show()

def primary(img):
    newdata = []
    data = list(img.getdata())
    red = (255, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    for i in range(len(data)):
        intensity = data[i][0] + data[i][1] + data[i][2]
        if intensity < 255:
            newdata.append(blue)
        elif intensity < 510:
            newdata.append(red)
        else:
            newdata.append(yellow)
    img.putdata(newdata)
    img.show()

#def grayscale(img):
    #newdata = []
    #data = list(img.getdata())
    #for i in range(len(data)):
        #newdata.append((data[i][0] + data[i][1] + data[i][2] // 3, data[i][0] + data[i][1] + data[i][2] // 3, data[i][0] + data[i][1] + data[i][2] // 3)
    #img.putdata(newdata)
    #img.show()
