import sys
import re
import ntpath
import os

def create_save_dir(dirName):
  try:
    os.mkdir(pathToSave + dirName)
    print('Directory ' + dirName + ' created!')
  except:
    print('Directory ' + dirName + ' icon already exists!')

def justify_string(string):
  string_length = len(string)+1
  string_revised = string.rjust(string_length)
  return string_revised

def routine():
  iconPath='clean/icon/'
  logoPath='clean/logo/'
  defs = open("defs.svg", "w")

  defs.write('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')
  defs.write('\t<defs>\n')

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

          path = ''.join(['\t\t<symbol id="', fileName, '" viewBox="0 0 72 72">', svgPath, '</symbol>\n'])
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
          widthString = ''
          heightString = ''
          viewboxString = ''
          print(width)
          print(height)
          print(viewbox)
          if width is not None and len(width.group(0)) >= 1:
            widthString = justify_string(width.group(0))
          else:
            widthString = ""

          if height is not None and len(height.group(0)) >= 1:
            heightString = justify_string(height.group(0))
          else:
            heightString = ""

          if viewbox is not None and len(viewbox.group(0)) >= 1:
            viewboxString = justify_string(viewbox.group(0))
          else:
            viewboxString = ""



          svgPath = fullSvg[pathStart : pathEnd]

          path = ''.join(['\t\t<symbol id="', fileName, '"', widthString, heightString, viewboxString, ">", svgPath, '</symbol>\n'])
          defs.write(path)

  defs.write('\t</defs>\n')
  defs.write('</svg>\n')

  defs.close()
