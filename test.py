import sys
from huffman import huffman



text= "beebs beepps!!!!! their eerie ears hear pears"

h = huffman()

result = h.compress(text)
print(result)

result2 = h.decompress(result)

print(result2)