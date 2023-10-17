from blabel import LabelWriter
import os
import subprocess

formsurl = "https://docs.google.com/forms/d/e/1FAIpQLScT8NE4mdcjGt9tQF9FcR4gVRf-W9iBJ0PisparvkjBKrdT7A/viewform?entry.448325822="
beverage_name = "Kaffee"
beverage_size = "small"
beverage_extrashot = "No"

label_writer = LabelWriter("blabel-test/item_template.html", default_stylesheets=("blabel-test/style.css",))
records = [
    dict(qr_data = formsurl + beverage_name, 
         beverage_name = beverage_name + "(" + beverage_size + ")",
         beverage_extrashot = beverage_extrashot),
]


label_writer.write_labels(records, target="bb_qrcode_and_date.pdf")

fn = 'bb_qrcode_and_date.pdf'
printer = 'Brother_QL_1110NWB'
print_cmd = 'lpr -P %s %s'
os.system(print_cmd % (printer, fn))

#printers = subprocess.getoutput("lpstat -a | awk '{print $1}'").split("\n")
#print(printers)