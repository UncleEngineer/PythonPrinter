import os
path = os.getcwd()
# os.startfile('08_prototype_deployment.pdf','print')

import win32print
import subprocess
import time
pdf_file  = os.path.join(path,'08_prototype_deployment.pdf')
acrobat = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
name = win32print.GetDefaultPrinter()
cmd = '"{}" /n /o /t "{}" "{}"'.format(acrobat, pdf_file, name)

proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)