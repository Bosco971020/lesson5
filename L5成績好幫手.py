y=0
z=0
a=0
d=100000000000000000000000000000000000000
x=int(input('你需要輸入幾個成績?'))


score_list=list(range(x))
name_list=[]
print(score_list)
for i in range(x):         
    name=str(input('輸入新名字:'))
    y=int(input('輸入新成績:'))
    name_list.append(name)
    z=z+y
    print(name_list)
    if y>a:
        a=i
    if y<d:
        d=i
    score_list.insert(i,y)
    score_list.remove(i)
    print(score_list)
print('以上的成績平均是',z/x)
print('總成績為',z)
print('其中以',name_list[a],score_list[a],'分為最高分')
print('以',name_list[d],score_list[d],'分為最低分')