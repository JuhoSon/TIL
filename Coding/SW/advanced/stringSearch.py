'''5252 공통단어검색
A와 B는 각자 만든 영어 단어장에 같은 단어가 얼마나 있는지 확인하려고 한다.
두 사람이 만든 단어장에 공통으로 들어있는 단어의 개수를 알아내는 프로그램을 만드시오. 단, 모든 단어는 소문자로 되어 있다.
[입력]
첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 A의 단어 개수 N과 B의 단어개수 M이 주어진다.
다음 줄부터 N개의 단어와 M개의 단어가 주어진다.(1<=T<=50, 3<=N, M<=3000)
단어의 길이는 20글자 이내이다.
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
'''
test_case = int(input())
for _ in range(test_case):
    n, m = map(int, input().split(' '))
    n_list = [input() for _ in range(n)]
    m_list = [input() for _ in range(m)]
    common_cnt = sum([1 for _ in n_list if _ in m_list])
    print('#{} {}'.format(_+1, common_cnt))
'''5253 접두어 검색
문자열 about에서 첫 글자부터 이어지는 a, ab, abo, abou, about은 접두어이다.
단, abu 같이 첫 글자부터 계속 이어지는 경우가 아니면 접두어가 아니다.
문자열 그룹 A와 B가 주어질 때, B에 속한 문자열 중 A의 접두어인 문자열의 개수를 알아내는 프로그램을 만드시오. 모든 단어는 소문자로 이루어져 있다.
[입력]
첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 A의 단어 개수 N과 B의 단어개수 M이 주어진다.
다음 줄부터 N개의 단어와 M개의 단어가 주어진다.( 1<=T<=50, 3<=N, M<=3000 )
단어의 길이는 20글자 이내이다.
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
'''
test_case = int(input())
for _ in range(test_case):
    n, m = map(int, input().split(' '))
    n_list = [input() for _ in range(n)]
    m_list = [input() for _ in range(m)]
    prefix_cnt = sum([sum(set(1 for nn in n_list if nn[:len(mm)] == mm)) for mm in m_list])
    print('#{} {}'.format(_+1, prefix_cnt))
'''5254부분 문자열
길이가 K인 문자열 S가 있을 때, S의 연속된 일부분을 부분 문자열이라고 한다.
부분 문자열은 원래의 순서가 바뀌거나 중간에 있는 글자가 빠져서는 안된다.
주어진 문자열의 부분 문자열을 사전순으로 정렬한 후, N번째 부분 문자열의 첫 글자와 글자 수를 출력하는 프로그램을 완성하시오.
예를 들어 abac의 부분 문자열은 사전순으로 정렬하면 다음과 같다.
a ab aba abac ac b ba bac c
3번째 부분 문자열은 aba가 된다.
[입력]
첫 줄에 테스트 케이스의 개수 T가 주어지고, 다음 줄부터 각 줄에 N과 문자열이 주어진다.
문자열의 길이는 4글자 이상 1000글자 이내이고, N은 문자열의 길이 이내이다. ( 1<=T<=50 )
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
'''
test_case = int(input())
for _ in range(test_case):

n, s = input().split(' ')
n = int(n) -1
sub_list = list(set([s[start:end] for start in range(len(s)) for end in range(start+1, len(s)+1)]))
t = Trie()
for w in sub_list:
    t.insert(w)
t.starts_with_num(5)
print('#{} {} {}'.format(_+1, sub_list[n][0], len(sub_list[n])))






class Node(object):
    """
    A single node of a trie.

    Children of nodes are defined in a dictionary
    where each (key, value) pair is in the form of
    (Node.key, Node() object).
    """
    def __init__(self, key, data=None):
        self.key = key
        self.data = data # data is set to None if node is not the final char of string
        self.idx = 0
        self.children = {}

class Trie(object):
    """
    A simple Trie with insert, search, and starts_with methods.
    """
    def __init__(self):
        self.head = Node(None)

    """
    Inserts string in the trie.
    """
    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        # When we have reached the end of the string, set the curr_node's data to string.
        # This also denotes that curr_node represents the final character of string.
        curr_node.data = string
        curr_node.idx += 1


    """
    Returns if string exists in the trie
    """
    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # Reached the end of string,
        # If curr_node has data (i.e. curr_node is not None), string exists in the trie
        if (curr_node.data != None):
            return True

    """
    Returns a list of words in the trie
    that starts with the given prefix.
    """
    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None

        # Locate the prefix in the trie,
        # and make subtrie point to prefix's last character Node
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None

        # Using BFS, traverse through the prefix subtrie,
        # and look for nodes with non-null data fields.
        queue = list(subtrie.children.values())

        while queue:
            curr = queue.pop()
            if curr.data != None:
                result.append(curr.data)

            queue += list(curr.children.values())

        return result

    def starts_with_num(self, num):
        curr_node = self.head
        result = None

        for _ in range(num):
            curr_node = curr_node.children
        result = curr_node.data
        return result
