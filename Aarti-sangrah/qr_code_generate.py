#improting the module
import qrcode

# creating the variable for the QR code
qr = qrcode.QRCode(
    version = 1,
    box_size = 15,
    border = 4
    )

# adding a link for the QR code to open
data = 'https://bit.ly/qr-aarti-sangrah'
qr.add_data(data)
qr.make(fit=True)

# adding the color
img = qr.make_image(fill = 'black', back_color = 'white')
img.save('nitya_path_qr.png')