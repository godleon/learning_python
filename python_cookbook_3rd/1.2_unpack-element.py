#!/usr/bin/env python3

RECORD = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
NAME, EMAIL, *PHONE_NUMBER = RECORD
print(NAME)
print(EMAIL)
print(PHONE_NUMBER)


sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(trailing_avg)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    if tag == 'bar':
        do_bar(*args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
print(fields)


record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
    
items = [1, 10, 7, 4, 5, 9]
items2 = [3]
print(sum(items))
print(sum(items2))