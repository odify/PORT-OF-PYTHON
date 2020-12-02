import pyqrcode
import png
from pyqrcode import QRCode


print("Enter text to convert")
s=input(": ")

# Name of QR code
print("Enter image name to save")
n=input(": ")
d=n+".png"

url=pyqrcode.create(s)
url.show()
url.png(d, scale =6)
