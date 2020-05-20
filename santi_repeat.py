list_numbers=[1, 2, 3, 3, 3, 4, 4, 4, 4]
dic={}
max_repeat=[]

for number in list_numbers:
    if number not in dic:
        dic[number]=1
    elif number in dic:
        dic[number]=dic[number]+1
print(dic)


for k,v in dic.items():
    if k == v :
        max_repeat.append(k)

print("El numero maximo que se repite a si mismo es {}".format(max(max_repeat)))
