#A = [input("")]
A = "кот уше гул иll еть"
a = A.split()
print (a)
max_string = max(a, key=len)
print (max_string)
import collections
B = collections.Counter(a)
most_common, occurance = B.most_common()[0]
print (most_common)