class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        integers = []
        for t in tokens: 
            if t == "+":
                integers.append(integers.pop()+integers.pop())
            elif t == "-":
                a,b = integers.pop(), integers.pop()
                integers.append(b-a)
            elif t == "*":
                integers.append(integers.pop()*integers.pop())
            elif t == "/":
                a,b = integers.pop(), integers.pop()
                integers.append(int(b/a))
            else:
                integers.append(int(t))
        return integers[-1]
                

