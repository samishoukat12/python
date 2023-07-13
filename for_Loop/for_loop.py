array=["santa fe","great falls","honolulu"]
cleanest_city="santa fe"
i=0
for city in array:
    if cleanest_city==city:
        i=1
        break
if i==1:
    print("clean city")  
elif i==0:
    print('no city found')