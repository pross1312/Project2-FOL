class Postfix:
    def __init__(self, len) -> None:
        self.len = len
        self.top = -1
        self.stack = []
        self.postfix = []
        self.priority = {';': 1, ',': 2}

    def isEmpty(self):
        return True if self.top == -1 else False

    def pop_top(self):
        return self.stack[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.stack.append(op)

    def isOperand(self, ch):
        if (ch == ',' or ch == ';' or ch == '(' or ch == ')') and len(ch) == 1:
            return False
        return True
    
    def notGreater(self, i):
        try:
            a = self.priority[i]
            b = self.priority[self.pop_top()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):

        for i in exp:

            if self.isOperand(i):
                self.postfix.append(i)

            elif i == '(':
                self.push(i)

            elif i == ')':
                while ((not self.isEmpty()) and self.pop_top() != '('):
                    a = self.pop()
                    self.postfix.append(a)
                if (not self.isEmpty() and self.pop_top() != '('):
                    return -1
                else:
                    self.pop()

            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    self.postfix.append(self.pop())
                self.push(i)

        while not self.isEmpty():
            self.postfix.append(self.pop())
