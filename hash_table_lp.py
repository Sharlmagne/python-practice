class HashTableLP:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h]:
            if self.arr[h][0] == key:
                return self.arr[h][1]

        for i in range(self.MAX):
            step = (h + i) % self.MAX
            if self.arr[step] is None:
                pass
            elif self.arr[step][0] == key:
                return self.arr[step][1]

    def new_index(self, h):
        count = 0
        is_full = False
        step = h
        while self.arr[step] is not None:
            step = (h + count) % self.MAX
            if count < self.MAX-1:
                count += 1
            else:
                is_full = True
                break
        if is_full:
            return None
        else:
            return step

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
            return

        step = self.new_index(h)
        if step is None:
            print("Hash table is full")
        else:
            self.arr[step] = (key, value)

    def __delitem__(self, key):
        h = self.get_hash(key)

        if self.arr[h]:
            if self.arr[h][0] == key:
                self.arr[h] = None
                return

        for i in range(self.MAX):
            step = (h + i) % self.MAX
            if self.arr[step] is None:
                pass
            elif self.arr[step][0] == key:
                self.arr[step] = None
                break


if __name__ == "__main__":
    table = HashTableLP()
    table['march 6'] = 54
    table['march 17'] = 67
    table['march 1'] = 89
    table['march 3'] = 83
    table['march 5'] = 83
    table['march 8'] = 83
    table['march 9'] = 83
    table['march 10'] = 83
    table['march 12'] = 83
    table['march 13'] = 83
    table['march 14'] = 83
    print(table.arr)
    print(table['march 6'])
    print(table['march 19'])
    print(table['march 10'])
    del table['march 6']
    del table['march 17']
    del table['march 13']
    print(table.arr)
