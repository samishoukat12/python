obj = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}


# for values in obj.values():
#     print(values)


# for key,values in obj.items():
#     print(key,values)


# dictionary with list

obj2 = [
    {
        "id": 1,
        'name': 'John',
        'age': 30,
        'city': 'New York'
    },
    {
        "id": 2,
        'name': 'Ali',
        'age': 30,
        'city': 'New York'
    },
    {
        "id": 3,
        'name': 'Sami',
        'age': 30,
        'city': 'New York'
    }
]

i = 0
obj2.append({
    "id": 4,
    'name': 'Sami',
    'age': 30,
    'city': 'New York'
})


print(len(obj2))
while i < len(obj2):
    if(obj2[i]['id'] == 4):
        print(obj2[i]["age"])
    i += 1
