from escpos import printer
from escpos.exceptions import DeviceNotFoundError

# Bixolon
print("Trying Bixolon")
try:
    p = printer.Usb(0x1504, 0x0103, in_ep=0x81, out_ep=0x02)
    print(p.is_online())
except DeviceNotFoundError:
    print("Device not found")

# Modus
print("Trying Modus")
try:
    p = printer.Usb(0x0DD4, 0x0286, in_ep=0x81, out_ep=0x02)
    print(p.is_online())
except DeviceNotFoundError:
    print("Device not found")
