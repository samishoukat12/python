arr = [
    {
        "name": "John",
    },
    {
        "name": "Jane",
    },
    {
        "name": "Jack",
    }
]

x = 0

for x in arr:
    if(x["name"][0]=='J'):
        print("found")
    else:
        print("not found")