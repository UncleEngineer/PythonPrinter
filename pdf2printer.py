import os
import subprocess
import win32print

currentprinter = win32print.GetDefaultPrinter()
print(currentprinter)

path = os.getcwd()

file = '08_prototype_deployment.pdf'

command = "{} {}".format('PDFtoPrinter.exe',os.path.join(file))

subprocess.call(command,shell=True)

