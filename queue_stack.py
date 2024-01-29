class myQueue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self,x):
        self.s1.append(x)

        return self.s1

    def remove(self):
        while(len(self.s1) != 0):
            self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self):
        return self.s2[-1]

    def empty(self):
        return not self.s2

if __name__ == '__main__':
    q = myQueue()
    print(q.push(1) )
    print(q.push(2)) 
    print(q.push(3))
    print(q.remove())
    print(q.peek())
    print(q.empty())

    
 

