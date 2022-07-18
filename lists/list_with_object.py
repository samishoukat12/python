obj=[
    {
        "name":"sami"
    },
      {
        "name":"sami"
    },
      {
        "name":"sami"
    },
      {
        "name":"sami"
    },
]
new_obj={
    "name":"ali"
}
obj.append(new_obj)



obj.insert(0,{
    "name":"hamza"
})

print(obj)



# concept of slicing
new_slice_obj=obj[1:]
print(new_slice_obj)


new_slice1obj=obj[:5]
print(new_slice1obj)


new_slice2obj=obj[2:6]
print(new_slice2obj)



##Delete concept

del obj[5]
print(obj)

#without index


obj.remove({
    "name":"hamza"
})
print(obj)