test = {'first': 1, 'second': 2}
test['first'] = 3
test['third'] = 3
test['fourth'] = 50

del test['second']
test['second'] = 45

print(test)
for x, t in enumerate(test):
    print (x)
    print (t)

