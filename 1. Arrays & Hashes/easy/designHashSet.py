# https://leetcode.com/problems/design-hashset/

# Space-inefficient way:
# class MyHashSet:

#     def __init__(self):
#         self.keySpace = pow(10, 6) + 1
#         self.hashSet = [-1] * self.keySpace

#     def add(self, key: int) -> None:
#         hashKey = key % self.keySpace
#         self.hashSet[hashKey] = hashKey

#     def remove(self, key: int) -> None:
#         hashKey = key % self.keySpace
#         self.hashSet[hashKey] = -1

#     def contains(self, key: int) -> bool:
#         hashKey = key % self.keySpace
#         return self.hashSet[hashKey] >= 0

# Space efficient way:
class Bucket:
    def __init__(self, key):
        self.key = key
        self.next = None

    def add(self, key):
        self.curr = self
        while self.curr.next != None:
            self.curr = self.curr.next
        self.curr.next = Bucket(key)

    def remove(self, head, key):
        self.curr = head.next
        self.prev = head
        if head.key == key:
            head = self.next
            return head
        while self.curr != None:
            if self.curr.key == key:
                self.prev.next = self.curr.next
                return head
            self.prev = self.curr
            self.curr = self.curr.next
        return head

    def contains(self, key):
        self.curr = self
        while self.curr != None:
            if self.curr.key == key:
                return True
            self.curr = self.curr.next
        return False


class MyHashSet:
    def __init__(self):
        self.keySpace = pow(10, 1)
        self.hashSet = [None] * self.keySpace

    def add(self, key: int) -> None:
        hashKey = key % self.keySpace
        if self.contains(key):
            return
        if self.hashSet[hashKey] != None:
            self.hashSet[hashKey].add(key)
        else:
            self.hashSet[hashKey] = Bucket(key)

    def remove(self, key: int) -> None:
        hashKey = key % self.keySpace
        if self.hashSet[hashKey] != None:
            head = self.hashSet[hashKey]
            self.hashSet[hashKey] = self.hashSet[hashKey].remove(head, key)

    def contains(self, key: int) -> bool:
        hashKey = key % self.keySpace
        if self.hashSet[hashKey] != None:
            return self.hashSet[hashKey].contains(key)
        return False


# ["MyHashSet","add","remove","add","contains","add","remove","add","add","add","add"]
# [[], [6], [4], [17], [14], [14], [17], [14], [14], [18], [14]]
obj = MyHashSet()
obj.add(43907)
obj.add(6)
obj.add(6)
obj.add(16)
obj.add(13)
assert obj.contains(6) == True
assert obj.contains(16) == True
obj.remove(6)
assert obj.contains(16) == True
assert obj.contains(6) == False
obj.remove(6)
assert obj.contains(16) == True

obj.remove(16)
assert obj.contains(6) == False
assert obj.contains(16) == False
