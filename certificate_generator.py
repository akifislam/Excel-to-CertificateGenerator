from PIL import ImageFont, ImageDraw, Image
import time

def spacing_calculator(length):
    space = 12

    if length<7:
        space =8
    elif length <=10:
        space = 9
    elif length <=15:
        space = 14
    elif length<=20:
        space = 18 # 17 chilo
    elif length>20:
        space = 15;
    if length>25:
        space = 20

    return space





def image_to_PDF(filename):
    rgba = Image.open(f"/Users/akifislam/PycharmProjects/RuhulBhai Certificate Generator/{filename}.png")
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
    rgb.paste(rgba, mask=rgba.split()[3])  # paste using alpha channel as mask
    rgb.save(f"/Users/akifislam/PycharmProjects/RuhulBhai Certificate Generator/{filename}.pdf",'PDF', resoultion=100.0)


def generate_certificate (participant_name):
    #Control Center
    text_to_write = participant_name
    font_size = 92
    center_x = 800
    center_y = 720
    text_length = len(participant_name)
    print("Text Length : ",text_length)
    text_spacing = spacing_calculator(text_length)
    # print("Spacing : ",text_spacing)

    #------
    image = Image.open("Beginner 3D.png")

    draw = ImageDraw.Draw(image)



    # use a truetype font
    # font = ImageFont.truetype("Palatino.ttc", font_size)
    # font = ImageFont.truetype("edwardian-script-itc-bold.ttf", font_size)
    font = ImageFont.truetype("Roboto-BlackItalic.ttf", font_size)

    # draw.text((center_x-(text_length*text_spacing), center_y), participant_name, font=font,fill=(0,0,255))
    draw.text((center_x-(text_length*text_spacing), center_y), participant_name, font=font,fill=(60,59,110))
    # Center == (993,860)

    image.save(f"/Users/akifislam/PycharmProjects/RuhulBhai Certificate Generator/{participant_name}.png")
    # image.save("Munem.pdf", "PDF", resoultion=100.0)
    time.sleep(2)
    image_to_PDF(participant_name)
    image.show()
    # print("Successfully created certificate for :",participant_name)
    time.sleep(2)




def testing() :

    list = ['Akif', 'Sakib', 'Nourin', 'Fatimaa','Moushumi', 'Md Tushar', 'Nur-E-Jannat Anika', 'Ekramul Haque Shaibal', 'Rifat Khan','Abrar Jawad','Shamima Akter  Bhuiyan ']


    for data in list:
        generate_certificate(data)

    # generate_certificate("Nu-E-Jaat Anika")


# testing()

# generate_certificate("Dewan Tamanna Wodud Dina")
# generate_certificate("Akif Islam")