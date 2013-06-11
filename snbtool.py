# Copyright Igor Koshkarov, 2013
# Licensed under GPLv3
# Feel free to use, change and distribute

#!/usr/bin/env python
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import sys

class snbfile:
    # requires a file name to create a class
    def __init__(self, filename):
        self.__unzip(filename)

    # unzips given file, reads snote.xml and passes it to the function  __strip_text_from_contents
    def __unzip(self, file):
        z = ZipFile(file, 'r')
        contents = z.read("snote/snote.xml")
        z.close()
        self.__strip_text_from_contents(contents)

    #  travels through elements
    def __strip_text_from_contents(self, contents):
        tree = ET.fromstring(contents)
        # read every element
        for el in tree.iter():
           self.__analyze_element(el)

    # outputs text only
    def __analyze_element(self, el):
        if el.text != None:
            print el.text


def main(file):
    s = snbfile(file)

if __name__ == "__main__":
    main(sys.argv[1])
