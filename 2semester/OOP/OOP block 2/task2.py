class myString(str):
    def append(self, other):
        return self + other

    def pop(self, char=None):
        if len(self) == 0:
            return self
        if char == None:
            return self[:-1]
        else:
            return self.replace(char, '', 1)


test = myString('test1231')
new1 = test.append('123')
print(new1)
new2 = test.pop('1')
print(new2)
new3 = test.pop()
print(new3)
