'''
B
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
1 1 12
2 3 10
3 5 8
4 7 6
5 9 4
6 11 2
7 13 0
'''

h = 7
for string_ in range(1, h + 1):
    print(string_, end=' -> ')
    for space_ in range(0, h * 2 - string_ * 2):
        print('-', end='')
    for star in range(0, (string_ + (string_ - 1))):
        print('*', end=' ')
    print()

'''
A
            *
          *   *
        *       *
      *           *
    *               *
  *                   *
* * * * * * * * * * * * *
1 1 12
2 3 10
3 5 8
4 7 6
5 9 4
6 11 2
7 13 0
'''

for string_ in range(1, h + 1):
    print(string_, end=' -> ')
    for space_ in range(0, h * 2 - string_ * 2):
        print('-', end='')
    for star in range(string_ + (string_ - 1)):
        if star == 0 or star == string_ + (string_ - 1) - 1 or string_ == h:
            print('*', end=' ')
        else:
            print('-', end=' ')
    print()
'''
C
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *                   *
    *               *
      *           *
        *       *
          *   *
            *
1 1 12
2 3 10
3 5 8
4 7 6
5 9 4
6 11 2
7 13 0
8 11 2
9 9 4
10 7 6
11 5 8
12 3 10
13 1 11
'''
count = -1
for string_ in range(1, h * 2):
    print(string_, end=' ->\t')
    if string_ < h + 1:
        count += 2
    else:
        count -= 2
    for space_ in range(count, h * 2 - 1):
        print('-', end='')
    for star in range(count):
        if string_ <= h or star == 0 or star == count - 1:
            print('*', end=' ')
        else:
            print('-', end=' ')
    print()

'''
D
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *         *         *
    *       *       *
      *     *     *
        *   *   *
          * * *
            *
*
1 1 12
2 3 10
3 5 8
4 7 6
5 9 4
6 11 2
7 13 0
8 11 2
9 9 4
10 7 6
11 5 8
12 3 10
13 1 11
'''
count = -1
for string_ in range(1, h * 2):
    print(string_, end=' ->\t')
    if string_ < h + 1:
        count += 2
    else:
        count -= 2
    for space_ in range(count, h * 2 - 1):
        print('-', end='')
    for star in range(count):
        if string_ <= h or star == 0 or star == count - 1 or star == count // 2:
            print('*', end=' ')
        else:
            print('-', end=' ')
    print()
