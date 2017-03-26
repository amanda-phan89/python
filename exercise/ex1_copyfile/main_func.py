import sys
import os.path
from shutil import copy2, copytree

def main():
    src = ""
    dest = ""
    while len(src) <= 0:
        src = input('Please enter source name: ')

    while len(dest) <= 0:
        dest = input('Please enter destination name: ')

    canCopy = True
    filename = os.path.basename(src)
    if os.path.isfile(dest + '/' + filename):
        canCopy = False
        isYes = input(filename + ' is also in ' + dest + ', [Y/n]:')
        if isYes.lower() == 'y':
            canCopy = True

    if (canCopy == False):
        return

    try:
        copy2(src, dest)
    except FileNotFoundError as e:
        print(e)
    except IsADirectoryError as e:
        print(e)
    except:
        print("Unexpected error:", sys.exc_info()[0])

if __name__ == "__main__":
   main()
