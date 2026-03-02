my_list = [8,5,7,2,6,3,4,8,9,1,4,0]

print('lista original:', my_list)

list_count = len(my_list) 

lastN = list_count - 1
firstN = 0

print('primer numero:', my_list[firstN])
print('ultimo nunero:', my_list[lastN])

new_firstN = my_list.pop(lastN)
new_lastN = my_list.pop(firstN)

my_list.insert(0, new_firstN)
my_list.append(new_lastN)

print('lista cambiada: ', my_list)

