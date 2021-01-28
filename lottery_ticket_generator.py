from random import randint
import datetime as dt
import time

def gen_matr():
    range_nani = ((61,75), (46, 60), (31, 45), (16, 30), (1, 15), None)
    matr = []
    while True:
        try:
            for x, y in range_nani:
                row = []
                while len(row) < 5:
                    tmp = randint( x, y )
                    if tmp not in row:
                        row.append( tmp )
                    else:
                        continue        
                matr.append(row)
            print(matr)
        except TypeError:
            return matr
        
ticket_src = gen_matr()

f = 6 * 5 + 3

def printMatr(matr_in):
    for row in matr_in:
        for el in row:
            print(' {:4d}'.format(el), end=' ')
        print()
        print(str('-'*f))

print()
print( str( '='*f ))
bingo = list('БИНГО')
for h in bingo:
    print('  {:s} '.format(h), end="   ") 
print()
print( str( '—'*f ))
printMatr(tuple( zip(*ticket_src[::-1])))
print(" ",dt.datetime.now().strftime("%d/%m/%y")," @юзернэйм ", "ЛоТТо")
print( str( '='*f ))
print()
