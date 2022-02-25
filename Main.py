from Scanner import Scanner
from Core import Core
import sys
from ParseTree.Program import Program

def main():
  # Initialize the scanner with the input file sys.argv[1]

  S1 = Scanner("Cases/Correct/22.code")
  S2 = Scanner("Cases/Correct/22.data")

  new = Program(S1, S2)
  new.parse()
  new.execute()


if __name__ == "__main__":
    main()