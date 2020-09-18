def draw_hospital():
    print('            +-----------+            ')
    print('            |    +-+    |            ')
    print('            |    | |    |            ')
    print('            | +--   --+ |            ')
    print('            | +--   --+ |            ')
    print('            |    | |    |            ')
    print('            |    +-+    |            ')
    print('            |           |            ')
    print('            | +--+ +--+ |            ')
    print('            | |  | |  | |            ')
    print('            | +--+ +--+ |            ')
    print('+-----------|           |-----------+')
    print('|           |           |           |')
    print('| +--+ +--+ | +--+ +--+ | +--+ +--+ |')
    print('| |  | |  | | |  | |  | | |  | |  | |')
    print('| +--+ +--+ | +--+ +--+ | +--+ +--+ |')
    print('|           |           |           |')
    print('|           |           |           |')
    print('| +--+ +--+ | +--+ +--+ | +--+ +--+ |')
    print('| |  | |  | | |  | |  | | |  | |  | |')
    print('| +--+ +--+ | +--+ +--+ | +--+ +--+ |')
    print('|           |           |           |')
    print('+-----------------------------------+')

def show_hospital(width):
    top(width)
    symbol1(width)
    symbol2(width)
    symbol3(width)
    symbol3(width)
    symbol2(width)
    symbol1(width)

def top(width):
    for i in range(width*10+2):
        print(' ', end='')
    print('+', end='')
    for i in range(width*10+1):
        print('-', end='')
    print('+',end='')
    for i in range(width*10+2):
        print(' ',end='')
    print('')

def symbol1(width):
    for i in range(width*10+2):
        print(' ', end='')
    print('|',end='')
    for i in range(width*5-1):
        print(' ', end='')
    print('+-+', end='')
    for i in range(width*5-1):
        print(' ', end='')
    print('|')

def symbol2(width):
    for i in range(width*10+2):
        print(' ', end='')
    print('|',end='')
    for i in range(width*5-1):
        print(' ', end='')
    print('| |', end='')
    for i in range(width*5-1):
        print(' ', end='')
    print('|')

def symbol3(width):
    for i in range(width*10+2):
        print(' ', end='')
    print('|',end='')
    for i in range(width*5-4):
        print(' ', end='')
    print('+--   --+', end='')
    for i in range(width*5-4):
        print(' ', end='')
    print('|')

show_hospital(4)