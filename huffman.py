

import heapq

class huffman:

    def __init__(self):
        self.text =None
        self.heap = []
        self.huffcode ={}
        self.reverse_mapping = {}


    def frequency(self):
        d = dict(map(lambda x: (x, self.text.count(x)), set(self.text)))
        return d
        frequency = {}



    def compress(self, text):

        self.text = text
        freq = self.frequency()
        #print(freq)
        self.create_heap(freq)
        #print(self.heap)
        self.merge_nodes()

        self.generate_code()
        encoded = self.encode()

        pad = self.pad_text(encoded)

        return pad



    def create_heap(self, freq):
        for key in freq:
            node = self.HNode(key, freq[key])
            heapq.heappush(self.heap, node)

#innerclass
    class HNode:
        def __init__(self, char, frequency):
            self.char = char
            self.frequency = frequency
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.frequency < other.frequency

    def encode(self):
        encoded = ""

        for char in self.text:
            encoded += self.huffcode[char]
        return encoded

    def generate_code(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.helper(root,current_code)

    def helper(self, root, current_code):
        if(root ==None):
            return

        if(root.char != None):
            self.huffcode[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.helper(root.left, current_code + "0")
        self.helper(root.right, current_code + "1")



    def merge_nodes(self):
        while (len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HNode(None, node1.frequency + node2.frequency)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)




    def pad_text(self, encoded):
        pad = 8 - len(encoded) % 8
        for i in range(pad):
            encoded +="0"
        pad_info = "{0:08b}".format(pad)
        encoded = pad_info + encoded
        return encoded

    def get_array(self, padded):
        if(len(padded)%8 !=0):
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0,len(padded),8):
            byte = padded[i:i+8]
            b.append(int(byte,2))
        return b




    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if (current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def decompress(self, text2):
        encoded_text = self.remove_padding(text2)

        decompressed_text = self.decode_text(encoded_text)
        return decompressed_text

    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1 * extra_padding]

        return encoded_text