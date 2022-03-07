from email import charset
import sqlite3
import sys

def main(): 
  fileName = sys.argv[1];
  file = open(fileName, "r")
  sql = file.read()

  conn = sqlite3.connect("MOCdb.db")
  cursor = conn.cursor()
  cursor.executescript(sql)
  conn.commit()
  conn.close()
  return "Successfully Ran %s" %(fileName)

if __name__ == "__main__":

  print(main())