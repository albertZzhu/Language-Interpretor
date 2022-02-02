from Core import Core
import re

class Scanner:
  # Constructor should open the file and find the first token
  def __init__(self, filename):
    self.fileStream=open(filename)		#The file stream that opens the file
    self.current = ""				#The current string reading from file stream
    self.currentID = ""				#The ID of the current token if it is a ID
    self.outToken = Core.ERROR			#The token of the current string
    self.const = 0				#The value of the current token if it is a constant
    self.nextToken()				#advance to next token to get new token


  # nextToken should advance the scanner to the next token
  def nextToken(self):
    specials = [';', '(', ')', ',', '=', '!', '<', '+', '-', '*']	#the array that stores the special token
    while len(self.current) == 0:					#reading in the first string from file stream, stops when hit a space
      snew = self.fileStream.read(1)
      if len(snew) == 0:
        break
      while not len(snew) == 0 and not snew.isspace():
        self.current += snew
        snew = self.fileStream.read(1)

    self.current = self.current.strip()					#strip all the spaces inside the string


    indi = re.search(";|\)|\(|,|=|!|==|<|<=|\+|-|\*", self.current)	#using regular expression to see if any special characters in the string

    if len(self.current) == 0:						#if current string is empty, then it is at the end of the file
      self.outToken = Core.EOS
    elif indi:								#if there is special characters in the string, then it need to be handled one by one
      i = 0
      temp = ""								#the variable that hold the spring before any special character
      while self.current[i] not in specials:
        temp += self.current[i]
        i += 1
      self.current = self.current[i:]
      if i:
        self.normalDetection(temp)					#if there is string before the special character, then detect it normally
      else:
        self.specialDetection()						#if it is a special character, using special detection
    else:
        self.normalDetection(self.current)				#if the string contains no special character, then use normal detection
        self.current = ""
    return 0


  def specialDetection(self):						#Special detection for special characters like assign, equal, etc
    if self.current[0] == ';':
      self.outToken = Core.SEMICOLON
    elif self.current[0] ==',':
      self.outToken = Core.COMMA
    elif self.current[0] == '(':
      self.outToken = Core.LPAREN
    elif self.current[0] == ')':
      self.outToken = Core.RPAREN
    elif self.current[0] == '!':
      self.outToken = Core.NEGATION
    elif self.current[0] == '+':
      self.outToken = Core.ADD
    elif self.current[0] == '-':
      self.outToken = Core.SUB
    elif self.current[0] == '*':
      self.outToken = Core.MULT
    elif self.current[0] == '=':
      if len(self.current) > 1 and self.current[1] == '=':
        self.outToken = Core.EQUAL
        self.current = self.current[1:]
      else:
        self.outToken = Core.ASSIGN
    elif self.current[0] == '<':
      if len(self.current) > 1 and self.current[1] == '=':
        self.outToken = Core.LESSEQUAL
        self.current = self.current[1:]
      else:
        self.outToken = Core.LESS
    self.current = self.current[1:]

  def normalDetection(self, temp):					#Normal detection for alphabet and number characters
    '''print(temp)'''
    if temp.isdigit():
      if 1024 > int(temp) >= 0:
        self.outToken = Core.CONST
        self.const = int(temp)
      elif 1024 <= int(temp):
        self.outToken = Core.ERROR
        print("ERROR: Input value too large!")
      else:
        self.outToken = Core.ERROR
        print("ERROR: Input value too small!")
    else:
      if temp == "program":
        self.outToken = Core.PROGRAM
      elif temp == "begin":
        self.outToken = Core.BEGIN
      elif temp == "end":
        self.outToken = Core.END
      elif temp == "new":
        self.outToken = Core.NEW
      elif temp == "int":
        self.outToken = Core.INT
      elif temp == "define":
        self.outToken = Core.DEFINE
      elif temp == "endfunc":
        self.outToken = Core.ENDFUNC
      elif temp == "class":
        self.outToken = Core.CLASS
      elif temp == "extends":
        self.outToken = Core.EXTENDS
      elif temp == "endclass":
        self.outToken = Core.ENDCLASS
      elif temp == "if":
        self.outToken = Core.IF
      elif temp == "then":
        self.outToken = Core.THEN
      elif temp == "else":
        self.outToken = Core.ELSE
      elif temp == "endif":
        self.outToken = Core.ENDIF
      elif temp == "while":
        self.outToken = Core.WHILE
      elif temp == "endwhile":
        self.outToken = Core.ENDWHILE
      elif temp == "or":
        self.outToken = Core.OR
      elif temp == "input":
        self.outToken = Core.INPUT
      elif temp == "output":
        self.outToken = Core.OUTPUT
      elif temp == "ref":
        self.outToken = Core.REF
      elif temp == "share":
        self.outToken = Core.SHARE
      else:
        if re.match("^([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])*$", temp):
          self.outToken = Core.ID
          self.currentID = temp
        else:
          self.outToken = Core.ERROR
          print("ERROR:"+temp)

  # currentToken should return the current token
  def currentToken(self):
    return self.outToken

  # If the current token is ID, return the string value of the identifier
	# Otherwise, return value does not matter
  def getID(self):
    return self.currentID

  # If the current token is CONST, return the numerical value of the constant
	# Otherwise, return value does not matter
  def getCONST(self):
    return self.const
