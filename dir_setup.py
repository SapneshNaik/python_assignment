#!/usr/bin/python

#create a directory for the problem and create a basic readme file with problem statement

import os
import sys

def main(argv):
    if len(argv) < 2 :
        print("PLease provide problem number and problem statement")
        sys.exit()

    directory = 'problem'+argv[0]
    if not os.path.exists(directory):
        os.mkdir(directory)


    readme_file = open(directory+"/README.md", "w")
    readme_file.write(argv[1])
    print("ALL SET")


if __name__=="__main__":
    #exclude script name from args
    main(sys.argv[1:])
