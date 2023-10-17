from blabel import LabelWriter
from beverage import Beverage
import os
import subprocess


bev = Beverage("Espresso", size="M")
bev.extrashot = False

label_writer = LabelWriter("blabel-test/coffeelabel_template.html", default_stylesheets=("blabel-test/style.css",))
label_writer.write_labels(bev.record, target="bb_qrcode_and_date.pdf")

fn = 'bb_qrcode_and_date.pdf'
printer = 'Brother_QL_1110NWB'
print_cmd = 'lpr -P %s %s'
os.system(print_cmd % (printer, fn))