sales_info = [
    {
        'date': '27/02/23',
        'customer_email': 'joe@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {
                'name': 'Iron',
                'upc': 'ITEM-324',
                'unit_price': 32.45,
            },
            {
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 12.54,
            },

        ]
    },
    {
        'date': '27/02/23',
        'customer_email': 'david@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {				
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 5.42,
            },
        ],
    },
	{
        'date': '26/02/23',
        'customer_email': 'amanda@gmail.com',
        'items': [
            {
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 3.42,
            },			
            {   
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 17.54,
            },
        ],
    },
]

sales = []

for i in sales_info:
    for a in i['items']:
        if 'name' in a:
            a.pop('name')
            print(a)




# value = [item["unit_price"] for sale in sales_info for item in sale["items"]]

# sales_list = [i['upc'] for sale in sales_info for i in sale['items']]

# dictionary = dict(zip(sales_list, sale))
# print(dictionary)


# print(sales_list)
