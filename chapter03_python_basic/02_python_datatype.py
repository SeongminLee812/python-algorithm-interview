import collections
# list
a = list()
a = [1, 2, 4, 5]

a.insert(2, 3)
print(a)
print(a[2:4])
print(a[1:4])

# del : 인덱스로 삭제하기
# remove : 값으로 삭제하기

del a[1]
a.remove(5)

print(a)

# dictionary
a = {'key1':'value1', 'key2':'value2'}
print(a)

print(a['key1'])
# print(a['key4'])
if 'key4' in a:
    print('존재하는 키')
else:
    print('존재하지 않는 키')


a.setdefault('key3', 'value3')
print(a)

b = collections.defaultdict(int)

b['A'] = 5
b['B'] = 4
b['C'] += 1

print(b)

a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)

print(b)
print(b.most_common(2))
