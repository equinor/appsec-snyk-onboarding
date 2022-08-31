import qrcode
from PIL import Image

qr_face = Image.open('../content/images/scan.png')

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr.add_data('https://snykonboarding.app.radix.equinor.com/')
qr.make()

img_qr = qr.make_image().convert('RGB')

pos = ((img_qr.size[0] - qr_face.size[0]) // 2, (img_qr.size[1] - qr_face.size[1]) // 2)

img_qr.paste(qr_face, pos)
img_qr.save('../content/images/snykonboarding_qr.png')