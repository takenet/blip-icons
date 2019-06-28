import sys
import re
import ntpath
import os

clean='icon'

iconPath='1-raw/icon/'
logoPath='1-raw/logo/'

pathToSave='2-clean/'

def create_save_dir(dirName):
  try:
    os.mkdir(pathToSave + dirName)
    print('Directory ' + dirName + ' created!')
  except:
    print('Directory ' + dirName + ' icon already exists!')

def remove_all(substr, str):
  index = 0
  length = len(substr)
  while str.find(substr) != -1:
    index = str.find(substr)
    str = str[0:index] + str[(index+length):]
  return str

def remove_all_array(array, str):
  for substr in array:
    str = remove_all(substr, str)
  return str

create_save_dir('icon')
for root, dirs, files in os.walk(iconPath):
  for svgFile in files:
    if svgFile.endswith(".svg"):
      svgFilePath = os.path.join(root, svgFile)
      with open(svgFilePath) as svg:
        fullSvg = svg.read()

        fileName = ntpath.basename(svgFile)
        cleanedFilePath = pathToSave + 'icon/' + str(fileName)
        cleanedFile = open(cleanedFilePath, "w")

        cleanedSvg = remove_all_array([
          ' fill="none"',
          ' fill-rule="evenodd"',
          ' clip-rule="evenodd"',
          ' fill="black"'
        ], fullSvg)

        cleanedFile.write(cleanedSvg)
        cleanedFile.close()

create_save_dir('logo')
for root, dirs, files in os.walk(logoPath):
  for svgFile in files:
    print(svgFile)
    if svgFile.endswith(".svg"):
      svgFilePath = os.path.join(root, svgFile)
      with open(svgFilePath) as svg:
        fullSvg = svg.read()

        fileName = ntpath.basename(svgFile)
        cleanedFilePath = pathToSave + 'logo/' + str(fileName)
        cleanedFile = open(cleanedFilePath, "w")

        cleanedFile.write(fullSvg)
        cleanedFile.close()
