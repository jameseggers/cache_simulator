from cache_line_set import *
from math import *

class Cache():
    def __init__(self, L, K, N):
        self.L = L
        self.K = K
        self.N = N
        self.lines = []
        self.num_offset_bits = int(ceil(log(self.L, 2)))
        self.num_set_bits = int(ceil(log(self.N, 2)))
        self.sets = []

        for setId in range(self.N):
            self.sets.append(CacheLineSet(self.K, self.L, setId))

        self.addresses = [0x0000, 0x0004, 0x000c, 0x2200, 0x00d0, 0x00e0, 0x1130, 0x0028, 0x113c, 0x2204, 0x0010, 0x0020, 0x0004, 0x0040, 0x2208, 0x0008, 0x00a0, 0x0004, 0x1104, 0x0028, 0x000c, 0x0084, 0x000c, 0x3390, 0x00b0, 0x1100, 0x0028, 0x0064, 0x0070, 0x00d0, 0x0008, 0x3394]

        hits = 0
        for address in self.addresses:
            splited = self.split_address(address)
            set_num = splited[1]
            offset = splited[2]
            tag = splited[0]

            print "("+str(hex(address))+") - Offset: " + str(offset) + ", Set: " + str(set_num)  + "set num " + str(set_num)

            hits += self.sets[set_num].addToSet(address, offset, hex(tag))

        print "Hits: " + str(hits) + ", Misses: " + str(32 - hits)

    def split_address(self, address):
        offset = address & self.gen_mask(self.num_offset_bits)
        set_number = (address >> self.num_offset_bits) & self.gen_mask(self.num_set_bits)
        tag = address >> (self.num_set_bits + self.num_offset_bits)
        return [tag, set_number, offset]

    def gen_mask(self, num_ones):
        mask = 0
        counter = num_ones
        while(counter > 0):
          mask = mask << 1
          mask = mask + 1
          counter -= 1
        return mask

Cache(16, 8, 1)
