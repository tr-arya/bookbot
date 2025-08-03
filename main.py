import sys

from stats import get_num_words
from stats import get_char_freq
from stats import sort_char_freq

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()

  return file_contents

def main():
  # Exit if there is no path to book
  if len(sys.argv) == 1:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

  # Get text
  file_path = sys.argv[1]
  frankenstein = get_book_text(file_path)

  # Run stats
  num_words = get_num_words(frankenstein)
  char_freq = get_char_freq(frankenstein)
  sorted_char_freq = sort_char_freq(char_freq)

  # Format output
  print('============ BOOKBOT ============') 
  print(f'Analyzing book found at {file_path}...')
  print('----------- Word Count ----------')
  print(f'Found {num_words} total words')
  print('--------- Character Count -------')
  for data in sorted_char_freq:
    if data['char'].isalpha():
      print(f'{data['char']}: {data['num']}')
  print('============= END ===============')

main()