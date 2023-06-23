
from difflib import SequenceMatcher

with open("data.txt") as file1, open("similar_Data.txt") as file2, open("Different.txt") as file3:
  file1_data = file1.read()
  file2_data = file2.read()
  file3_data = file3.read()

print(file1_data)

print(file2_data)

print(file3_data)

similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
  print(similarity_ratio*100)

similarity_ratio = SequenceMatcher(None,file1_data,file3_data).ratio()
print(similarity_ratio*100)