import os
import subprocess
import sys
import win32print

# currentprinter = win32print.GetDefaultPrinter()
# print(currentprinter)

# args = '"C:\\\\Program Files\\\\gs\\\\gs9.56.1\\\\bin\\\\gswin64c" ' \
#        '-sDEVICE=mswinpr2 ' \
#        '-dBATCH ' \
#        '-dNOPAUSE ' \
#        '-dFitPage ' \
#        '-sOutputFile="%printer%myPrinterName" '
# ghostscript = args + os.path.join(os.getcwd(), '08_prototype_deployment.pdf.pdf')
# subprocess.call(ghostscript, shell=True)


import tempfile
import win32print
import locale
import ghostscript
# import render_to_pdf

# pdf = render_to_pdf('print/slip.html', context)
# temp1 = tempfile.mktemp('08_prototype_deployment.pdf')
# f1 = open(temp1, 'ab')
# f1.write(pdf)
# f1.close()

# args = [
#         "-dPrinted", "-dBATCH", "-dNOSAFER", "-dNOPAUSE", "-dNOPROMPT"
#         "-q",
#         "-dNumCopies#1",
#         "-sDEVICE#mswinpr2",
#         f'-sOutputFile#"%printer%{win32print.GetDefaultPrinter()}"',
#         f'"08_prototype_deployment.pdf"'
#     ]

# encoding = locale.getpreferredencoding()
# args = [a.encode(encoding) for a in args]

args = b"""gs -q -dNOPAUSE -sDEVICE=tiffg4 -sOutputFile=a.tif 08_prototype_deployment.pdf -c""".split()
ghostscript.Ghostscript(*args)

# ghostscript.Ghostscript(*args)