# LinkedListAddition
This is python code is to add two linked lists and return the result in third linked list.
Example: 
ListOne 2->8->4 represents number 284
ListOne 8->1->3 represents number 813
To add it up and get the result like 1->0->9->7

The algorithm is like-
1. if size of two linked lists is not same, add 0's in the shorter list to make size same.
2. Recursively reach up to to the last element and then extract digits of the last node. (extract 4 and 3)
3. add the digits and pass the carry if any to sum the digits again in the next recursive cycle (for 8 and 1)
