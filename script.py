import string
CHAR = string.ascii_letters + string.punctuation + " "

class OctoCript:
    def __init__(self, text, key):
        self.text = self._changeStringNumber(text)
        self.key = self._changeStringNumber((key * len(text))[0: len(text)])

    def _changeStringNumber(self, txt):
        return [CHAR.index(i)+1 for i in txt]

    def _changeNumberString(self, num: list):
        return [CHAR[i-1] for i in num]

    def cript(self):
        rCode = [self.text[x] + self.key[x] for x in range(len(self.text))]
        for i, value in enumerate(rCode):
            if value > len(CHAR) - 1:
                rCode[i] = value - 85
        return "".join(self._changeNumberString(rCode))

    def decrypt(self):
        rCode = [self.text[x] - self.key[x] for x in range(len(self.text))]
        for i, value in enumerate(rCode):
            if value > len(CHAR) - 1:
                rCode[i] = 84 - value
        return "".join(self._changeNumberString(rCode))


while True:
    txt = input("/message/~$ ")
    key = input("/key/~$ ")
    choice = input('/utils/~$ ')
    octo = OctoCript(txt, key)

    if choice in ['c', 'cript']:
        print(f"{octo.cript()}")
    elif choice in ['d', 'decript']:
        print(f"{octo.decrypt()}")
        
        
        
