from cache_line import *

class CacheLineSet():
    def __init__(self, K, L, setId):
        self.K = K
        self.setId = setId
        self.lines = []
        self.tags = []

        for line in range(K):
            self.lines.append(CacheLine(L, line))
            self.tags.append("-")

    def isInSet(self, address, tag):
        for line in self.lines:
            if (tag in self.tags) and line.is_in_line(address):
                return True
        return False

    def LRULine(self):
        lowest_order = self.lines[0].order
        lowest_index = 0
        for idx, line in enumerate(self.lines):
            if line.order < lowest_order:
                lowest_index = idx
        return lowest_index

    def addToSet(self, address, offset, tag):
        if (not self.isInSet(address, tag)):
            lowest_index = self.LRULine()
            self.lines[lowest_index].addToLine(address, offset)
            self.tags[lowest_index] = tag
            # print 'Cache Line ' + str(self.setId) + '('
            # for line in self.lines:
            #     print '[' + hex(line.words[0])+ ',' + hex(line.words[1])+ ',' + hex(line.words[2])+ ',' + hex(line.words[3])+ ']'
            # print ')'
            print "Miss"
        else:
            print "Hit!"

    def tags(self):
        return self.tags

    def lines(self):
        return self.lines

    def setId(self):
        return self.setId
