import datetime

from escpos import printer

machine_name = "Recycling Machine"
address = "1234 Elm St, Springfield, IL 62701"
currency = "£"
total_credit_str = "1.60"
custom_header1 = "CUSTOM HEADER 1"
custom_header2 = "CUSTOM HEADER 2"
custom_header3 = "CUSTOM HEADER 3"
serial_num1 = "123456789012"
plastic_count = 5
credit_plastic_str = "1.00"
metal_count = 3
credit_metal_str = "0.60"
machine_id = "Machine ID: 123456"
serial_num2 = "Serial Number: 123456789012"
session_end_time = datetime.datetime.now()
custom_footer1 = "CUSTOM FOOTER 1"
custom_footer2 = "CUSTOM FOOTER 2"
custom_footer3 = "CUSTOM FOOTER 3"

p = printer.Usb(0x0DD4, 0x0286, in_ep=0x81, out_ep=0x02)

p.set(align="center", bold=False, invert=False, normal_textsize=True)

p.textln(machine_name)
p.textln(address)

p.set(underline=1)
p.textln(" " * 32)
p.set(underline=0)
p.ln()

p.textln(custom_header1)
p.textln(custom_header2)
p.textln(custom_header3)
p.ln()

p.set(bold=True, invert=True, double_height=True, double_width=True)
p.ln()
p.textln(f"        {currency:2}{total_credit_str}       ")
p.ln()
p.set(bold=False, invert=False, normal_textsize=True)

p.barcode(serial_num1, "EAN13", 64, 2, "", "")

p.set(underline=1)
p.textln(" " * 32)
p.set(underline=0)
p.ln()

p.textln(f"{plastic_count}  PLASTIC BOTTLE          {credit_plastic_str}")
p.textln(f"{metal_count}  ALU CAN                 {credit_metal_str}")

p.set(underline=1)
p.textln(" " * 32)
p.set(underline=0)
p.ln()

p.textln(machine_id)
p.textln(serial_num2)
p.textln(session_end_time.strftime("%Y-%m-%d %H:%M:%S"))

p.set(underline=1)
p.textln(" " * 32)
p.set(underline=0)
p.ln()

p.textln("THANK YOU FOR RECYCLING")

p.set(underline=1)
p.textln(" " * 32)
p.set(underline=0)
p.ln()

p.textln(custom_footer1)
p.textln(custom_footer2)
p.text(custom_footer3)

p.cut()
p._raw(b"\x1c\x50\x00\x00")
