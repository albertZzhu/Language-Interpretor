from Scanner import Scanner
from Core import Core
import sys
from ParseTree.Program import Program

def main():
  # Initialize the scanner with the input file sys.argv[1]
  for i in range(1, 27):
    S = Scanner("Error/10.code")

  new = Program(S)
  new.parse()


if __name__ == "__main__":
    main()