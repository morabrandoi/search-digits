from collections import deque

def read_in_chunks(file_object, chunk_size=1):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

# ONLY HANDLES WHEN TEXT CONTAINS 10 UNIQUE LETTERS
def is_text(q, text):
  l_z = list(zip(text, "".join(list(q))))
  res = all((z1[0] == z2[0]) == (z1[1] == z2[1]) for z1 in l_z for z2 in l_z)

  return res

def print_mapping(text, digs):
  mapping = dict(zip(digs, text))
  sorted_items = list(sorted(mapping.items(), key=lambda x: x[0]))
  for item in sorted_items:
    print(f"{item[0]} -> {item[1]}")

TEXT = 'searchtext:)'

# info dump
print(f"'{TEXT}' has {len(TEXT)} total letters")
print(f"'{TEXT}' has {len(set(list(TEXT)))} unique letters")
print('\n')

# checking sanity of input
if (len(set(list(TEXT))) != 10):
  print(f"need 10 unique letters in text. You have {len(set(list(TEXT)))}")
  exit()
if len(TEXT) == 16:
    print("Roughly 30% \chance of finding the string") 
if len(TEXT) > 16:
    print("very low chance of finding string")

counter = 0
with open('pi-billion.txt') as inFile:
  
  first_eight = list(inFile.read(len(TEXT)))
  queue = deque(first_eight)

  if (len(queue) != len(TEXT)):
    print("Queue and Text length are different. Fix")
    exit()

  for piece in read_in_chunks(inFile):
    if is_text(queue, TEXT):
      dig_seq_str = ''.join(list(queue))
      print(f"At digit: {counter - 1} of pi, we find the sequence {dig_seq_str}.")
      print("When translated with the following key:")
      print_mapping(TEXT, dig_seq_str)
      print(f"it produces the text: '{TEXT}'")
      exit()

    queue.popleft()
    queue.append(piece)

    counter += 1
    if (counter % 100000 == 0):
      print(counter)

print("Did not find it in the given text file")