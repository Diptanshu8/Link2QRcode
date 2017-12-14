import qrcode
import argparse
import os
from PIL import ImageColor

def parameter_handler(args):
    global back_color,fill_color,link, location, output_name
    color_choices = ImageColor.colormap.keys()
    #setting the default back_color for QR code and checking the user specified param for validity.
    back_color = "white"
    if args.background_color: 
        back_color = args.background_color
        if args.background_color not in color_choices :
            print "Error: invalid color choice for background color.\nThe available choices are \n"+ "\t".join(color_choices)
            exit()

    #setting the default fill_color for QR code and checking the user specified param for validity.
    fill_color = "black"
    if args.fill_color: 
        fill_color = args.fill_color
        if args.fill_color not in color_choices :
            print "Error: invalid color choice for fill color.\nThe available choices are \n"+ "\t".join(color_choices)
            exit()

    #checking if the output image needs to be saved.
    #if QR code has to be saved then under what name, format and location.
    if args.save:
        if not args.location:
            print "Error: The user didn't specify the location to save the QR code."
            exit()
        else:
            if os.path.exists(args.location):
                location = args.location
            else:
                print "Error: The user specified location doesn't exist."
                exit()
        if not args.name:
            print "Error: The user didn't specify the name by which the the QR code will be saved."
            exit()
        else:
            output_name = args.name

    #retrieving the URL from argparse
    link = args.url


parser = argparse.ArgumentParser()
parser.add_argument("url", help = "The URL for which the user wants to generate the QR code.")

parser.add_argument("-bc","--background_color", help = "The background color in the generated QR code.")
parser.add_argument("-fc","--fill_color",help = "The URL for which the user wants to generate the QR code.")

parser.add_argument("--save",action = "store_true", help = "Bool flag if the user wants to save the generated QR code.")
parser.add_argument("--location",help = "The location(local) to save the QR code.")
parser.add_argument("--name",help = "The name by which the QR code be saved.")
args = parser.parse_args()

#parsing the parameters set by the user
parameter_handler(args)

#generating the QR code according to doc at https://github.com/lincolnloop/python-qrcode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color = fill_color, back_color = back_color)
output_name+=".png"
img.save(os.path.join(location,output_name))
