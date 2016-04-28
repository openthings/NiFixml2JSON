from src.xml2json import conversion
import os
import sys

if __name__ == "__main__":
    for file_name in os.listdir("{0}".format(sys.argv[1])):
        a = open("{0}/{1}".format(sys.argv[1], file_name), 'r').read()
        b = conversion.Conversion(a)
        c = b.xml_to_json()
        d = c.replace(sys.argv[2], '')
        print d
        os.remove("{0}/{1}".format(sys.argv[1], file_name))

