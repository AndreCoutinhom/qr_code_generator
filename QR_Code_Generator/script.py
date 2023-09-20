import pyqrcode

url = pyqrcode.create('https://bio.link/andrecoutinhom')
url.svg('andre_portfolio_qr.svg', scale=5)

