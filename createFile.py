import csv 
arr=[]
count={}
arr2=[]
with open('google_play_store_data.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
       arr.append(row)
with open('dublicate_google.csv','w') as f:
    writer=csv.writer(f,delimiter=',')
    writer.writerows([arr])
with open('google_play_store_data.csv','r')as f:
    reader=csv.reader(f,delimiter=',')
    for row in reader:
        if row[1] in count:
            count[row[1]]+=1
        else:
            count[row[1]]=1
dictt={**count}
print(dictt)