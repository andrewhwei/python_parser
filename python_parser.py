import fileinput
import sys

class PythonParser:
  def main():
    """This program reads a text file, parses it, and writes the word count to an output file."""
    OUTPUT_FILE = 'output.txt'
    file = open(OUTPUT_FILE, 'w')
    word_count = {}
    for line in fileinput.input():
      for word in line:
        if word in word_count:
          word_count[word] += 1
        else:
          word_count[word] = 1
    for key in word_count:
      file.write(key)
      file.write(" : ")
      file.write(str(word_count[key]))
      file.write("\n")
    file.close()
  def print_to_console():
    """Takes keyboard input and prints it to console."""
    contents = input('Type text here: ')
    print(contents)
  def std_in_std_out():
    """Takes keyboard input and writes response as std out."""
    contents = input('Type text here: ')
    sys.stdout.write(contents)

  main()