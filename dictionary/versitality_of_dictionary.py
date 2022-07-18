ver_num={
    1:"sami",
    2:"sami",
    3:"ali",
}


print(ver_num[1])



new_dic={}

new_dic[0]=ver_num[2]
new_dic["name"]=ver_num[1]
print(new_dic)



# del new_dic["name"]
# del new_dic[0]
# print(new_dic)

ver_num[2]=new_dic["name"]
print(ver_num)


new_dic[2]="huston"
ver_num["city"]="winipeg"
print(ver_num, new_dic)