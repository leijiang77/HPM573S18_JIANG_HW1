
#problem 1.1

x=17

print('Setting x = ',x)

#integer
y1 = x
print('y2 is a ',type(y1))
print(y1)

#float
y2 = float(x)
print('y2 is a ',type(y2))
print(y2)
#string

y3 = str(x)
print('y2 is a ',type(y3))
print(y3)
#boolean '17>1"

y4 = bool(x>1)
print('y4 is a ',type(y4))
print(y4)


#problem 2

text = "The "+ "Value " +"of " + "x " +"is "
print(text)

#problem3

#iterative
def sum_it(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum


print(sum_it(100))

#recursive

def sum_rec(n):
    if n==1:
        return 1
    else:
        return n+sum_rec(n-1)


print(sum_rec(100))


#problem4
yours = ['Yale','MIT','Berkeley']
mine = ['Yale','Harvard','Priceton']
ours1 = yours + mine

print(ours1)

ours2 = []
ours2.append(mine)
ours2.append(yours)

print(ours2)


yours[1] = 'Brown'
print(yours)
print(ours1)
print(ours2)


#problem5

monthnumbers = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,'July':7,
                'August':8, 'September':9, 'October':10, 'November':11, "December":12,
                1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July',
                8:'August', 9:'September', 10:'October', 11:'November', 12:"December"
                }

print('February is month',monthnumbers['February'])
print(monthnumbers[2])

