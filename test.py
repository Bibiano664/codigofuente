import qrcode
from faker  import Faker

#variables  y contastentes
fake = Faker ()


for _ in range(10):
    name = fake.name()
    img = qrcode.make (name)
    img.save (name + ".png")
    print (f"QR code for {name} generated and save as {name}.png")