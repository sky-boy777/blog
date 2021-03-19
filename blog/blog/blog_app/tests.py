from django.test import TestCase

# Create your tests here.

s = '2.00+0.46+0.25(285714)'
arr = s.split('+')
print(arr)
l = []
for i in arr:
    if i.split('.')[0] != '0':
        i = i.split('.')[0]
    l.append(i)

s = '+'.join(l)
print(s)

