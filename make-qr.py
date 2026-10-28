from reportlab.graphics.barcode.qrencoder import QRCode, QRErrorCorrectLevel
from PIL import Image, ImageDraw
from pathlib import Path
root=Path(__file__).parent/'dist'/'assets'
url='https://meemansak.github.io/business-card/'
qr=QRCode(None,QRErrorCorrectLevel.M)
qr.addData(url)
qr.make()
n=qr.getModuleCount(); scale=12; border=4
im=Image.new('RGB',((n+border*2)*scale,)*2,'#f6f3e9');d=ImageDraw.Draw(im)
for y in range(n):
 for x in range(n):
  if qr.isDark(y,x):d.rectangle(((x+border)*scale,(y+border)*scale,(x+border+1)*scale-1,(y+border+1)*scale-1),fill='#111210')
im.save(root/'connect-qr.png')
print('QR generated:',n,'modules;',url)

