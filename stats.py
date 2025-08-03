def get_num_words(text):
  return len(text.split())

def get_char_freq(text):
  char_freq = {}

  # Count each character in the text
  for char in text:
    c = char.lower()
    if c not in char_freq:
      char_freq[c] = 1
    else:
      char_freq[c] += 1

  return char_freq

def sort_char_freq(freq):
  # Sort by frequency of characters
  def sort_on(items):
    return items['num']

  # Define data dictionary and sort
  sorted_freq = [{'char': c, 'num': freq[c]} for c in freq]
  sorted_freq.sort(reverse=True, key=sort_on)

  return sorted_freq