from collections import deque


TEXT = 'BM>EL@SET@1@15'
DIG_MARGIN = 4
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
  l_z = list(zip(text, "".join(list(q)[DIG_MARGIN: -1 * DIG_MARGIN])))
  res = all((z1[0] == z2[0]) == (z1[1] == z2[1]) for z1 in l_z for z2 in l_z)

  return res

def form_and_print_mapping(text, digs):
  mapping = dict(zip(digs, text))
  sorted_items = list(sorted(mapping.items(), key=lambda x: x[0]))
  for item in sorted_items:
    print(f"{item[0]} -> {item[1]}")
  return mapping

def translate(mapping, full_dig_str):
  return "".join(list(map(lambda c: mapping[c], list(full_dig_str))))

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
  
  first_set = list(inFile.read(len(TEXT) + (2 * DIG_MARGIN)))
  queue = deque(first_set)

  if (len(queue) - (2*DIG_MARGIN) != len(TEXT)):
    print("Queue and Text length are different. Fix")
    exit()

  for piece in read_in_chunks(inFile):
    if is_text(queue, TEXT):
      full_dig_str = ''.join(list(queue))
      dig_seq_str = full_dig_str[DIG_MARGIN: -1 * DIG_MARGIN]
      print(f"At digit: {counter} of pi, we find the sequence {full_dig_str}.")
      print("When translated with the following key:")
      mapping = form_and_print_mapping(TEXT, dig_seq_str)
      print(f"it produces the text: '...{translate(mapping, full_dig_str)}...'")
      exit()

    queue.popleft()
    queue.append(piece)

    counter += 1
    if (counter % 100000 == 0):
      print(counter)

print("Did not find it in the given text file")