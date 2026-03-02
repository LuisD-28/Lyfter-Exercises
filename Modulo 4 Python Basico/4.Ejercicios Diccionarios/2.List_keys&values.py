
key_list = [
            'first_name',
            'last_name',
            'age',
            'role'
            ]
values_list = [
                'Luis',
                'Dorantes',
                29,
                'unemployed'
            ]


dictionary = dict(zip(key_list, values_list))
print(dictionary)

pairs = list(zip(key_list, values_list))

print(pairs)