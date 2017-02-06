class Stack:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

def opposite(character):

    if character == ')':
        opp = '('
    elif character == ']':
        opp = '['
    elif character == '}':
        opp = '{'
    else:
        opp = None

    return opp

def checkBrackets(string):

    checkStack = Stack()

    for item in string:

        if checkStack.isEmpty():
            checkStack.push(item)
        elif opposite(item) == checkStack.top():
            checkStack.pop()
        else:
            checkStack.push(item)

        print item, checkStack, checkStack.isEmpty()

    if checkStack.isEmpty():
        return "Parenthesis is closed"

    return "Parenthesis is not closed"


if __name__ == "__main__":

    testString = '{()' # Not closed
    testString = '{{{[(]}}})' # Not closed
    testString = '{{{{{{{[[[[[[(()())]()]]]]]}}}}}}}' # Closed
    print checkBrackets(testString)
