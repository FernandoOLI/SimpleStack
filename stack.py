#Declaração da classe Stack(pilha)
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s=Stack()
print("------------pilha vazia---------")
print(s.isEmpty())
print("---------------------------------")
s.push(4)
print("------------pilha push 4---------")
print(s.items)
print("---------------------------------")
s.push('dog')
print("------------pilha push dog---------")
print(s.items)
print("---------------------------------")
print("------------pilha topo---------")
print(s.peek())
print("---------------------------------")
s.push(True)
print("------------pilha push True---------")
print(s.items)
print("---------------------------------")
print("------------pilha tamanho--------")
print(s.size())
print("---------------------------------")
print("------------pilha vazia---------")
print(s.isEmpty())
print("---------------------------------")
s.push(8.4)
print("------------pilha push 8,4---------")
print(s.items)
print("---------------------------------")
print("------------pilha pop---------")
print(s.pop())
print("---------------------------------")
print("------------pilha pop---------")
print(s.pop())
print("---------------------------------")
print("------------pilha tamanho--------")
print(s.size())
print("---------------------------------")
print("------------pilha final---------")
print(s.items)
print("---------------------------------")
