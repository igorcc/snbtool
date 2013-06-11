from zipfile import ZipFile
import xml.etree.ElementTree as ET
import sys

class snbfile:
    # requires a file name to create a class
    # otherwise raises an exception
    def __init__(self, filename):
        self.__unzip(filename)

    # unzips given file and reads snote.xml
    def __unzip(self, file):
        z = ZipFile(file, 'r')
        contents = z.read("snote/snote.xml")
        z.close()
        self.__strip_text_from_contents(contents)

    # made for test purposes
    # lists file parts
    def __strip_text_from_contents(self, contents):
        tree = ET.fromstring(contents)
        # read every element
        for el in tree.iter():
           self.__analyze_element(el)

    def __analyze_element(self, el):
        if el.text != None:
            print el.text


def main(file):
    s = snbfile(file)

if __name__ == "__main__":
    main(sys.argv[1])
