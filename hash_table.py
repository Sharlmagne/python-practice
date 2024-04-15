class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                return self.arr[h][idx]
                break

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


if __name__ == "__main__":
    table = HashTable()
    table['march 6'] = 54
    table['march 17'] = 67
    table['march 1'] = 89
    table['march 9'] = 83
    print(table.arr)
    print(table['march 6'])
    print(table['march 19'])
    print(table['march 17'])
    del table['march 17']
    del table['march 1']
    print(table.arr)


