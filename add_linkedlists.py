#!/usr/bin/python2.7

from LinkedList import LinkedList

#lets create two linked list objects
list1 = LinkedList()
list2 = LinkedList()

#add elements in first linked list. Please make sure you are inserting unit place first followed by 10th place and then 100th place. Below I'm inserting number 287
list1.insert(7)
list1.insert(8)
list1.insert(2)

#add elements in second linked list. Below I'm inserting number 813
list2.insert(3)
list2.insert(1)
list2.insert(8)

print "== Initial list1 =="
list1.printlist()

print "== Initial list2 =="
list2.printlist()

#compare total elements in lists and accordingly add zeros to make them of same size
if list1.size() > list2.size():
    diff = list1.size() - list2.size()
    for i in range(0, diff):
        list2.insert(0)
elif list1.size() < list2.size():
    diff = list2.size() - list1.size()
    for i in range(0, diff):
        list1.insert(0)

print "After making same size..."
print "== list1 =="
list1.printlist()

print "== list2 =="
list2.printlist()

print "lets add two linked lists..."
#create new linked list to store results
res = LinkedList()

sum = 0
carry = 0

for i in range(0,list1.size()):
    sum = list1.last().get_data() + list2.last().get_data() + carry
    if sum >= 10:
        res.insert(sum-10)
        carry = 1
    else:
        res.insert(sum)
        carry = 0
    list1.delete(list1.last().get_data())
    list2.delete(list2.last().get_data())

if carry == 1:
  res.insert(1)

res.printlist()
