import time

class CacheLine(object):
    def __init__(self, L, setNumber):
        self.L = L
        self.words = [0,0,0,0]
        self.setNumber = setNumber
        self.last_access = time.time()
        self.initialized = False

    def is_in_line(self, address):
        for word in self.words:
            if (hex(address) == hex(word)):
                self.accessed()
                return True
        return False

    def addToLine(self, address, offset):
        self.accessed()
        self.initialized = True

        if offset is 0:
            self.words[0] = address
            self.words[1] = address + 0x4
            self.words[2] = address + 0x8
            self.words[3] = address + 0xc
        elif offset is 4:
            self.words[0] = address - 0x4
            self.words[1] = address
            self.words[2] = address + 0x4
            self.words[3] = address + 0x8
        elif offset is 8:
            self.words[0] = address - 0x8
            self.words[1] = address - 0x4
            self.words[2] = address
            self.words[3] = address + 0x4
        elif offset is 12:
            self.words[0] = address - 0xc
            self.words[1] = address - 0x8
            self.words[2] = address - 0x4
            self.words[3] = address

    def setNumber(self):
        return self.setNumber

    def last_access(self):
        return self.last_access

    def accessed(self):
        self.last_access = time.time()

    def words(self):
        return self.words

    def initialized(self):
        return self.initialized
