class HASH:
    def __init__(self, size, _max, threshold):
        self.size = size
        self.max = _max
        self.element = [None] * self.size
        self.member = []
        self.thr = threshold

    def next_prime(self, n):
        return self.find_prime_in_range(n, 2 * n)

    def find_prime_in_range(self, a, b):
        for c in range(a, b):
            for i in range(2, c):
                if c % i == 0:
                    break
            else:
                #print(c)
                return c
        return None

    def rehash(self):
        self.size = self.next_prime(self.size * 2)
        self.element = [None] * self.size
        #print(self.size)
        #print(self.member)
        for x in self.member:
            _try = 0
            org_idx = x % self.size
            while _try < self.max:
                idx = (org_idx + _try**2) % self.size
                if self.is_empty(idx):
                    self.element[idx] = x
                    break
                _try += 1
                print(f'collision number {_try} at {idx}')

    def is_empty(self, idx):
        return self.element[idx] == None

    def insert(self, value):
        print("Add :", value)
        self.member.append(value)  #temp data for rehash
        _try = 0
        org_idx = value % self.size
        while _try < self.max:
            idx = (org_idx + _try**2) % self.size
            if self.is_empty(idx):
                if (len(self.member)) * 100 / self.size > self.thr:
                    print("****** Data over threshold - Rehash !!! ******")
                    self.rehash()
                    return
                else:
                    self.element[idx] = value
                    return
            _try += 1
            print(f'collision number {_try} at {idx}')
        #self.size += 1
        print("****** Max collision - Rehash !!! ******")
        self.rehash()

    def _print(self):
        for i in range(self.size):
            print("#" + str(i + 1) + "	" + str(self.element[i]))
        print("----------------------------------------")


if __name__ == "__main__":
    #inp_ = "19 2 49/8741 4874 787842 77 8789 7542 751213 978458".split("/")
    inp_ = input(" ***** Rehashing *****\nEnter Input : ").split("/")
    table_size, Max_collision, threshold = int(inp_[0].split()[0]), int(
        inp_[0].split()[1]), int(inp_[0].split()[2])
    member = list(map(int, inp_[1].split()))
    h = HASH(table_size, Max_collision, threshold)
    print("Initial Table :")
    h._print()
    for x in member:
        h.insert(x)
        h._print()
