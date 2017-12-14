import qrcode
import argparse
from PIL import ImageColor

parser = argparse.ArgumentParser()
color_choices = ImageColor.colormap.keys()
parser.add_argument("url", help = "The URL for which the user wants to generate the QR code.")
parser.add_argument("--background_color", help = "The background color in the generated QR code.")
parser.add_argument("--fill_color",help = "The URL for which the user wants to generate the QR code.")
args = parser.parse_args()

if args.background_color and args.background_color not in color_choices :
	print "Error: invalid color choice for background color.\nThe available choices are \n"+ "\t".join(color_choices)
if args.fill_color and args.fill_color not in color_choices :
	print "Error: invalid color choice for fill color.\nThe available choices are \n"+ "\t".join(color_choices)
link = args.url
print link


"""
#generating the QR code according to doc at https://github.com/lincolnloop/python-qrcode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color = "black", back_color = "white")
img.show()

"""
