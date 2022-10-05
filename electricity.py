import loadData as ld
import computeStats as cs
import sys
import time

def main():
    
    if len(sys.argv) < 4:
        print("Usage: python electricity.py stat path interval\n")
        print("\t stat=0: computeStats=False, stat=1: computeStats=True")
        print("\t path is a string used to load datas")
        print("\t interval: number of minutes between two data readings")
        print(" exemple: python3 electricity.py 1 ~/Documents/IFT799/Projet/LD2011_2014.txt 15\n")
        return
    
    computeStats = int(sys.argv[1]) > 0.5
    path = sys.argv[2]
    interval = int(sys.argv[3])

    data = ld.loadData(path,interval)

    if computeStats:
        stats = cs.computeStats(data)

if __name__ == "__main__":
    main()