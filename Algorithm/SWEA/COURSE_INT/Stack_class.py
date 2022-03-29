# stack 구현

class Stack:                    # ADT -> 실제 코드의 형태로 작성
    my_list = []
    # 생성자 -> 인스턴스가 생성될 떄 자동으로 호출!
    def __init__(self, size):
        # self -> 인스턴스 자신
        self.items = []     # 요소를 담을 배열
        self.size = size    # 만들 배열의 크기
        self.top = -1       # 파이썬에서는 음수 인덱싱을 지원 하지만 c와 같은 언어에서는 지원 x -> 어떤 요소의 초깃값을 표현할 때 많이 활용

    def is_empty(self):
        # return False if len(self.items) else True
        if len(self.items):
            return False
        return True

    def is_full(self):
        # return True if len(self.items) == self.size else False
        if len(self.items) == self.size:
            return True
        return False

    def push(self, item):
        if self.is_full():
            raise Exception('Stack is full!!')
        else:
            # append 통해서 넣을 수 있음!
            self.items.append(item)
            self.top += 1

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty!')
        else:
            return self.items[self.top]

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty!')
        else:
            value = self.items[self.top]
            self.items = self.items[:self.top]
            self.top -= 1
            return value

    def __str__(self):
        result = '\n-----'
        for d in self.items:
            result = f'\n| {d} |' + result
        for _ in range(self.size - len(self.items)):
            result = f'\n|   |' + result
        return result

my_stack = Stack(6)
print(my_stack)
# print(my_stack.is_full())
# print(my_stack.is_empty())

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
# my_stack.push(7)
print(my_stack)
print(my_stack.peek())
print(my_stack)
print(my_stack.is_full())

print(my_stack.pop())
print(my_stack)

print(my_stack.is_full())
print(my_stack.is_empty())
# print(my_stack.top)

# stack을 Python list로 구현하면?
my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print(my_list)
print(len(my_list))

print(my_list.pop())
print(my_list.pop())
print(my_list.pop())
print(my_list.pop())
print(my_list)
