from feature_extractor import *
from script import *


def main():

    swtr = '-CH2-CH2-O-CH2-'
    str1 = list(swtr)
    str2 = [swtr]
    print (str2)
    p = feature_extractor(str2)
    q = ValuePredictor(p)
    print (q)

    return


if __name__ == "__main__":
    main()
