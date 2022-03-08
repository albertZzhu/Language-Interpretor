from Scanner import Scanner
from Core import Core
import sys
from ParseTree.Program import Program

def main():
  # Initialize the scanner with the input file sys.argv[1]

  S1 = Scanner(sys.argv[1])
  S2 = Scanner(sys.argv[2])

  new = Program(S1, S2)
  new.parse()
  new.execute()


if __name__ == "__main__":
    main()