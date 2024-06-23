from escpos import printer

p = printer.Usb(0x0DD4, 0x0286, in_ep=0x81, out_ep=0x02)

p.barcode("4006381333931", "EAN13", 64, 2, "", "")
p.text("Hello World!")
p.cut()
p._raw(b"\x1c\x50\x00\x00")
