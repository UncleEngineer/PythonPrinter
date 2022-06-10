# pip install pypiwin32

import win32print

currentprinter = win32print.GetDefaultPrinter()
print(currentprinter)