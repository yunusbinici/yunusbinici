import qrcode
data="https://github.com/yunusbinici/yunusbinici"
image=qrcode.make(data)
image.save("qrcode.png")
