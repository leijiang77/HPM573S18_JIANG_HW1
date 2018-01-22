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
print (yours)
print (ours1)
print (ours2)

#Using '+' produced a new list resulting from the concatenation of the two lists and 'append' just appends another element to an existing list.
#As a result, changing the original list doesn't change "Ours1" as it's a new list and "Ours2" will be changed if the original list changed.


