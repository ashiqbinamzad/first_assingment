mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here


users = mobile_data["data"]
print(users)

for user in users:
    name = user.get('name')
    usd = user.get('price').replace(' USD','')
    made = user.get('made')

    exchnage_rate = mobile_data.get('exchnage_rate')
    taka = 100

    price = exchnage_rate * (float(usd))

    paragraph = f'This is {name} phone which price is {price} in BDT. It is made in {made} '
    print(usd)