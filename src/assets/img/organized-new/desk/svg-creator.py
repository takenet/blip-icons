import sys
import re
import ntpath
import os

iconPath='3-compressed/icon/'
logoPath='3-compressed/logo/'
defs = open("defs.svg", "w")

defs.write('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')
defs.write('\t<defs>\n')

def create_save_dir(dirName):
  try:
    os.mkdir(pathToSave + dirName)
    print('Directory ' + dirName + ' created!')
  except:
    print('Directory ' + dirName + ' icon already exists!')

create_save_dir('icon')
for root, dirs, files in os.walk(iconPath):
  for svgFile in files:
    print(svgFile)
    if svgFile.endswith(".svg"):
      svgFilePath = os.path.join(root, svgFile)
      with open(svgFilePath) as svg:
        fullSvg = svg.read()

        fileName = ntpath.basename(svgFile).split('.svg')[0]

        pathStart = fullSvg.find('>') + 1
        pathEnd = fullSvg.find('</svg>')

        svgPath = fullSvg[pathStart : pathEnd]

        path = ''.join(['\t\t<symbol id="', fileName, '" viewBox="0 0 24 24">', svgPath, '</symbol>\n'])
        defs.write(path)

create_save_dir('logo')
for root, dirs, files in os.walk(logoPath):
  for svgFile in files:
    print(svgFile)
    if svgFile.endswith(".svg"):
      svgFilePath = os.path.join(root, svgFile)
      with open(svgFilePath) as svg:
        fullSvg = svg.read()

        fileName = ntpath.basename(svgFile).split('.svg')[0]

        pathStart = fullSvg.find('>') + 1
        pathEnd = fullSvg.find('</svg>')

        svgAtributes = fullSvg[0 : pathStart]
        width = re.search("(width=\"[0-9]+\"){1}", svgAtributes)
        height = re.search("(height=\"[0-9]+\"){1}", svgAtributes)
        viewbox = re.search("(viewbox=\"[0-9]+\s+\"){1}", svgAtributes)
        print(width)
        print(height)
        print(viewbox)
        if width is not None and len(width) >= 1:
          width = " ".join(width)
        else:
          width = ""

        if height is not None and len(height) >= 1:
          height = " ".join(height)
        else:
          height = ""

        if viewbox is not None and len(viewbox) >= 1:
          viewbox = " ".join(viewbox)
        else:
          viewbox = ""



        svgPath = fullSvg[pathStart : pathEnd]

        path = ''.join(['\t\t<symbol id="', fileName, width, height, viewbox, ">", svgPath, '</symbol>\n'])
        defs.write(path)

defs.write('\t</defs>\n')
defs.write('</svg>\n')

defs.close()
