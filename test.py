# Some f string tests...

'''
print('test1...') # f string 'width' specifier -> {value:width} - no spaces between brackets
for x in range(1, 10):
    print(f'{x:2}{x*x:3}{x*x*x:4}')
print('\n')

print('test2...') # f string 'width' specifier -> {value:width} - one space between brackets
for x in range(1, 10):
    print(f'{x:2} {x*x:3} {x*x*x:4}')
print('\n')

print('test3...') # f string 'width' specifier -> {value:width} - zero prefix short numbers
for x in range(1, 10):
    print(f'{x:02} {x*x:03} {x*x*x:04}')
print('\n')

print('test4...') # f string 'width' specifier -> {value:width} - right justify - '>' - left justify - '<' (default)
for x in range(1, 10):
    print(f'{x:>2} {x*x:>3} {x*x*x:>4}')
print('\n')

print('test5...') # f string 'width' specifier -> {value:width} - center justify - '^'
for x in range(1, 10):
    print(f'{x:^10} {x*x:^10} {x*x*x:^10}')
print('\n')
'''

HEADER = 5

msg = "Welcome to yoda!"
print(msg[:10])
print(msg[:11])
print(msg[:12])

print(msg[10:])
print(msg[11:])
print(msg[12:])

print(f'{len(msg):<{HEADER}}' + msg)
