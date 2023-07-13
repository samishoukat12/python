import json
arr=[
    {
    'name':'sami',
    'age':25
},
{
    'name':'sami',
    'age':25
},
{
    'name':'sami',
    'age':25
}
]
with open('test.json','w') as f:
    json.dump(arr,f)

with open('test.json','r') as f:
    print(json.load(f))