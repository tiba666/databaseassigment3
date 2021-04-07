
from huffman import huffman



text= "beebs beepps!!!!! their eerie ears hear pears"
text2 = "pete is here"
h = huffman()

result = h.compress(text)
print(result)

result2 = h.decompress(result)

print(result2)