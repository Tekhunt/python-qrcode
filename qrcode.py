# importing dependencies
import pyqrcode
import  png
from pyqrcode import QRCode

url_for_code = input('input the url for code generation: ')
create_qrcode = pyqrcode.create(url_for_code)
png_format = create_qrcode.png('png_qrcode', scale=10)
sqg_format = create_qrcode.svg('svg_qrcode', scale=8)

# sample url used here is https://www.python.org 

