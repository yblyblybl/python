def compare(_list_=[]):
    list1=[]
    for v1 in _list_:
        length=len(list1)
        for t1 in range(len(list1)):
            if v1>list1[t1]:
                list1.insert(t1,v1)
                break
        if len(list1)==length:
            list1.append(v1)
    return list1
print(compare([0,3,8,10,3849,38]))
from turtle import*
pu()
write('vkgkg')
