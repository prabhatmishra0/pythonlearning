# import qrcode as qr
# img = qr.make("https://self-defence-taekwondo-academy.business.site")
# img.save("taekwondo.png")


import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="#F57D12", back_color="#A0E5F4")
img.save("taekwondo3.png")
