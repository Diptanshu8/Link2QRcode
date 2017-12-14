import qrcode
#from PIL import Image
#taking the URL input from the user.
print "Please input the URL you want to convert to QR code.\n\n"
link = str(raw_input())

#generating the QR code according to doc at https://github.com/lincolnloop/python-qrcode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color = "black", back_color = "white")
img.show()

