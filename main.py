import qrcode
import image
from qrcode.main import make
myQR = qrcode.QRCode(version = 15,box_size=10, border=5)
data = "hello :D"
myQR.add_data(data)
myQR.make(fit= True)
qrImg = myQR.make_image(fill = 'black', back_color = 'white')
qrImg.save('test.png')