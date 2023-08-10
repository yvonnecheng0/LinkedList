""""
This class supports arbitrarily large integers using linked lists which can add absolute values of integers. 
Yvonne Cheng 
csci 112
Winter, 2023
"""

class Bignum:
    #Initialized with number n and a base base (default 17).
    def __init__(self, n, base=17):
        self.base = base
        if n < 0:
            self.sign = -1
        else:
            self.sign = 1
        self.n = abs(n)
        self.next = None
        self.overflow ()

    #Overrides eq for unittest
    def __eq__(self, other):
        return self.base == other.base and self.sign == other.sign and self.n == other.n
    
    #Converts bignum int to python int
    def int(self):
        i = 0
        node = self
        multi = 1
        while node is not None:
            i += node.n * multi
            multi *= self.base
            node = node.next
        return i * self.sign

    #any cell that is larger than the base reduced and carried to the next cell
    def overflow(self):
        return self.base ** len(str(self.n))

    #Helps debug code with string representation of bignums 
    def __str__(self):
        values = []
        value = self.n
        sign = "-" if self.sign == -1 else "+"
        while value > 0:
            digit = value % self.base
            values.append(str(digit))
            value = value // self.base
        digits = ":".join(values)
        return f"Bignum base {self.base}: {digits}:{sign}"

    #Adds bignums together(currently only for absolute values of addition)
    def __add__(self, other):
        if self.base != other.base:
            raise ValueError("Bignums have different bases")
        
        move = 0
        node1 = self
        node2 = other
        result = None
        tail = None
        
        while True:
            if node1 is None and node2 is None and move == 0:
                break
            n1 = node1.n if node1 is not None else 0
            n2 = node2.n if node2 is not None else 0
            total = n1 + n2 + move
            move = total // self.base
            digit = total % self.base
            new_node = Bignum(digit)
            if result is None:
                result = new_node
            else:
                tail.next = new_node
            tail = new_node
            node1 = node1.next if node1 is not None else None
            node2 = node2.next if node2 is not None else None
        return result
        

if __name__ == "__main__":
    n = 2**100
    print(Bignum(n).int ())
    print(Bignum (20 ,8))
    print(Bignum ( -123 ,10))
    print(Bignum (20 ,2))
    print(Bignum (50 ,16))