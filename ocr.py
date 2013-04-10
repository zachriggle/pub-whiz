import os
import subprocess
import tempfile

try:
  import Image
except:
  import sys
  print "You must install the Python Imaging Library"
  print "$ pip install PIL"
  sys.exit()

def ocr(filename):
    """Extracts information from the specified text file with tesseract
    """
    tempTifname  = tempfile.mktemp() + '.tif'
    tempTxtname  = tempfile.mktemp()

    subprocess.check_call(['convert', filename, '-type', 'Grayscale', tempTifname])
    subprocess.check_call(['tesseract', tempTifname, tempTxtname, 'tesseract_configuration'])

    data = file(tempTxtname + '.txt').read()

    os.remove(tempTifname)
    os.remove(tempTxtname + '.txt')

    return data
