
import sys
import os
import pickle

def main():

    if os.path.exists("sectors.p"):
        fin = open("sectors.p", "rb")
        sectors = pickle.load(fin)
        fin.close()
    else:
        print("Sectors does not exist")
        sectors = {}

    print(sectors)

main()
