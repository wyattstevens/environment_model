
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

    if os.path.exists("ships.p"):
        fin = open("ships.p", "rb")
        ships = pickle.load(fin)
        fin.close()
    else:
        print("Ships does not exist")
        ships = {}
    
    print("Sectors: ")
    print(sectors)
    print("Ships: ")
    print(ships)

main()
