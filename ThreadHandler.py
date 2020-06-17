class Queue:
    def __init__(self):
        self.Stack = []

    def __repr__(self):
        return "{}".format(self.Stack)

    def __str__(self):
        return "{}".format(self.Stack)

    def place(self,add):
        self.Stack.insert(0,add)
        return True

    def size(self):
        return len(self.Stack)

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    
    def cut(self):
        if self.size ==0:
            return None
        else:
            return self.Stack.pop()
