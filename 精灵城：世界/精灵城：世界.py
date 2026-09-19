from turtle import*
from random import*
from time import*
import keyboard as key
#------------------------------------------------#
def boolint(_object_):
    return bool(int(_object_))
def g_dot(x,y,size,___color___='black'):
    color(___color___)
    pu()
    goto(19*x,19*y)
    pd()
    dot(size)
def ng_square(_color_='black'):
    color(_color_)
    begin_fill()
    for t1 in range(4):
        fd(18)
        rt(90)
    end_fill()
def square(x,y,__color__='black'):
    pu()
    goto(19*x-9,19*y+9)
    pd()
    ng_square(_color_=__color__)
def readtxt(listwhat='',time=1,mode=str):
    turnout=[]
    for t1 in range(time):
        turnout.append(listwhat)
    readin=list(next(name_file))
    t1=0
    for v1 in readin:
        try:
            int(v1)
            turnout[t1]+=v1
        except:
            if v1==',':
                t1+=1
            elif v1=='n' or v1=='\\':
                pass
            elif v1=='.':
                turnout[t1]+=v1
    for t1 in range(time):
        turnout[t1]=mode(turnout[t1])
    return turnout
def clean(x,y):
    square(x,y,'white')
#------------------------------------------------#
def petpoint(x,y,n=False):
    if n:
        square(x,y,__color__='green')
    else:
        square(x,y,__color__='gray')
def player(x,y):
    color('black')
    g_dot(x,y+1,7)
    goto(19*x,19*y-5)
    pu()
    goto(19*x-7,19*y+10)
    pd()
    goto(19*x+7,19*y+10)
def cat_0(x,y,level,_mutate_=False):#凯特
    square(x,y,__color__='orange')
    goto(19*x,19*y+9)
    if y==15:
        color('white')
    else:
        color('black')
    write(str(level),align='center',font=('Arial',10,'bold'))
    color('black')
    if _mutate_:
        goto(19*x,19*y-9)
        write('tb',align='center',font=('Arial',10,'bold'))
def army_1(x,y,level,_mutate_=False):#阿尔米
    square(x,y,__color__='red')
    goto(19*x,19*y+9)
    if y==15:
        color('white')
    else:
        color('black')
    write(str(level),align='center',font=('Arial',10,'bold'))
    color('black')
    if _mutate_:
        goto(19*x,19*y-9)
        write('tb',align='center',font=('Arial',10,'bold'))
def water_2(x,y,level,_mutate_=False):#一
    square(x,y,__color__='blue')
    goto(19*x,19*y+9)
    if y==15:
        color('white')
    else:
        color('black')
    write(str(level),align='center',font=('Arial',10,'bold'))
    color('black')
    if _mutate_:
        goto(19*x,19*y-9)
        write('tb',align='center',font=('Arial',10,'bold'))
def e_2_718(x,y,level,_mutate_=False):#一
    square(x,y,__color__='brown')
    goto(19*x,19*y+9)
    if y==15:
        color('white')
    else:
        color('black')
    write(str(level),align='center',font=('Arial',10,'bold'))
    color('black')
    if _mutate_:
        goto(19*x,19*y-9)
        write('tb',align='center',font=('Arial',10,'bold'))
def import_3(x,y,level,_mutate_=False):#因珀尔特
    square(x,y,__color__='purple')
    goto(19*x,19*y+9)
    if y==15:
        color('white')
    else:
        color('black')
    write(str(level),align='center',font=('Arial',10,'bold'))
    color('black')
    if _mutate_:
        goto(19*x,19*y-9)
        write('tb',align='center',font=('Arial',10,'bold'))
def π_3_141(x,y,level,_mutate_=False):#派
    if _mutate_:
        g_dot(x,y,19,___color___='red')
        g_dot(x,y,16,___color___='orange')
        g_dot(x,y,13,___color___='yellow')
        g_dot(x,y,10,___color___='green')
        g_dot(x,y,7,___color___='light blue')
        g_dot(x,y,4,___color___='blue')
        g_dot(x,y,1,___color___='purple')
    else:
        g_dot(x,y,19,___color___='gray')
    goto(19*x,19*y+9)
    if y==15:
        color('white')
    else:
        color('black')
    write(str(level),align='center',font=('Arial',10,'bold'))
def choosepet(x,y,_pet_='0',_level_=0,_mutate_=False):
    if _pet_=='0':
        cat_0(x,y,_level_,_mutate_)
    elif _pet_=='1':
        army_1(x,y,_level_,_mutate_)
    elif _pet_=='2':
        water_2(x,y,_level_,_mutate_)
    elif _pet_=='2.718':
        e_2_718(x,y,_level_,_mutate_)
    elif _pet_=='3':
        import_3(x,y,_level_,_mutate_)
    elif _pet_=='3.141':
        π_3_141(x,y,_level_,_mutate_)
def q_process(x,y):
    clean(x,y)
    clean(x,y+1)
    g_dot(x,y,19,'black')
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
#------------------------------------------------#
#try:
for v0 in range(1):
    name=input('输入你的名字:')
    with open("C:\\Users\\ziyun\\Desktop\精灵城：世界\\player's name\\"+name+'.txt','r') as name_file:
        money=int(next(name_file))
        playerx=int(next(name_file))
        playery=int(next(name_file))
        lowball=int(next(name_file))
        print(lowball)
        commonball=int(next(name_file))
        primaryball=int(next(name_file))
        middleball=int(next(name_file))
        primeball=int(next(name_file))
        s0ball=int(next(name_file))
        precious‌ball=int(next(name_file))
        s0preciousbal=int(next(name_file))
        balllist=[lowball,commonball,primaryball,middleball,primeball,s0ball,precious‌ball,s0preciousbal]
        level=int(next(name_file))
        area1=bool(int(next(name_file)))
        box1=bool(int(next(name_file)))
        box2=bool(int(next(name_file)))
        box3=bool(int(next(name_file)))
        box4=bool(int(next(name_file)))
        box5=bool(int(next(name_file)))
        pet1=readtxt('',40,str)
        pet2=readtxt('',40,str)
        pet3=readtxt('',40,str)
        pet4=readtxt('',40,str)
        pet5=readtxt('',40,str)
        petmutate1=readtxt(0,40,boolint)
        petmutate2=readtxt(0,40,boolint)
        petmutate3=readtxt(0,40,boolint)
        petmutate4=readtxt(0,40,boolint)
        petmutate5=readtxt(0,40,boolint)
        petlevel1=readtxt(0,40,int)
        petlevel2=readtxt(0,40,int)
        petlevel3=readtxt(0,40,int)
        petlevel4=readtxt(0,40,int)
        petlevel5=readtxt(0,40,int)
    setup(1.0,1.0)
    ht()
    speed(0)
    g_dot(-2,0,10)
    pu()
    tracer(0)
    for t1 in range(2):
        fd(38)
        pd()
        dot(10)
        pu()
    tracer(1)
    tracer(0)
    clear()
    square(-16,16)
    for t2 in range(4):
        for t3 in range(32):
            fd(19)
            ng_square()
        fd(18)
        rt(90)
    worldpet=[['',False],['',False],['',False],['',False],['',False],['',False],['',False],['',False],['',False],['',False]]
    worldpetlevel=[0,0,0,0,0,0,0,0,0,0]
    worldpetxy=[['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['','']]
    for t1 in range(10):
        while 1:
            worldpetlv=randint(1,50)
            if worldpetlv in worldpetlevel:
                pass
            else:
                worldpetlevel[t1]=randint(1,50)
                break
        mutate=not(bool(randint(0,999)))
        v1=randint(1,1000)
        if v1<=300:
            worldpet[t1]='1'
        elif v1<=600:
            worldpet[t1]='2'
        elif v1<=900:
            worldpet[t1]='3'
        elif v1<=990:
            worldpet[t1]='0'
        elif v1<=999:
            worldpet[t1]='2.718'
        elif v1<=1000:
            worldpet[t1]='3.141'
        while 1:
            worldpetx=randint(-15,15)
            worldpety=randint(-15,14)
            if (worldpetx==4 and worldpety==11) or (worldpetx==playerx and worldpety==playery) or (worldpetx==playerx and worldpety==playery+1) or [worldpetx,worldpety] in worldpetxy:
                pass
            else:
                worldpetxy[t1][0]=worldpetx
                worldpetxy[t1][1]=worldpety
                break
        choosepet(worldpetxy[t1][0],worldpetxy[t1][1],worldpet[t1],worldpetlevel[t1])
    petpoint(4,11,area1)
    player(playerx,playery)
    pu()
    goto(-313,313)
    write('lv.'+str(level)+'精灵代币:'+str(money)+'精灵:x战斗:f捕捉:q激活精灵站:e在精灵战旁回复状态:r',font=('Arial',15,'bold'))
    tracer(1)
#except:
#    print('程序在运行中出错')
#------------------------------------------------#
while 1:
#    global playerx,playery,name
    key.read_key()
    keyworld=key.read_key()
    tracer(0)
    if keyworld=='w':
        if [playerx,playery+2] in worldpetxy or (playerx==4 and playery+2==11) or playery+2==16:
            pass
        else:
            clean(playerx,playery)
            clean(playerx,playery+1)
            playery+=1
            player(playerx,playery)
    if keyworld=='s':
        if [playerx,playery-2] in worldpetxy or (playerx==4 and playery-1==11) or playery-1==-16:
            pass
        else:
            clean(playerx,playery)
            clean(playerx,playery+1)
            playery-=1
            player(playerx,playery)
    if keyworld=='d':
        if ([playerx+1,playery] in worldpetxy or (playerx+1==4 and playery==11) or playerx+1==16) or ([playerx+1,playery+1] in worldpetxy or (playerx+1==4 and playery+1==11) or playerx+1==16) or ([playerx+1,playery-1] in worldpetxy or playerx+1==16):
            pass
        else:
            clean(playerx,playery)
            clean(playerx,playery+1)
            playerx+=1
            player(playerx,playery)
    if keyworld=='a':
        if ([playerx-1,playery] in worldpetxy or (playerx-1==4 and playery==11) or playerx-1==-16) or ([playerx-1,playery+1] in worldpetxy or (playerx-1==4 and playery+1==11) or playerx-1==-16) or ([playerx-1,playery-1] in worldpetxy or playerx-1==-16):
            pass
        else:
            clean(playerx,playery)
            clean(playerx,playery+1)
            playerx-=1
            player(playerx,playery)
    if keyworld=='q':
#        try:
        for tt in range(1):
            d1={}
            d2={}
            l1=[]
            l2=[]
            l3=[]
            for t1 in range(10):
                print(worldpetxy[t1][0]-playerx)
                print(worldpetxy[t1][0]-playery)
                if abs(worldpetxy[t1][0]-playerx)<2 and abs(worldpetxy[t1][1]-playery)<2:
                    d1[worldpetlevel[t1]]=worldpet[t1]
                    l1.append(worldpetlevel[t1])
                    d2[worldpetlevel[t1]]=t1
                print(1) 
            l1=compare(l1)
            print(12)
            for v1 in l1:
                l2.append(d1[v1])
            print(l2)
            print(123)
            if len(l2)>=1:
                for t1 in range(33):
                    clean(16-t1,-17)
                pu()
                goto(-313,-332)
                pd()
                color('black')
                write('有'+str(len(l1))+'个精灵，从大到小由0到n为序号，请选择',font=('Arial',10,'bold'))
                tracer(1)
                tracer(0)
                print(11111)
                key.read_key()
                keyword1=key.read_key()
                for t1 in range(33):
                    clean(16-t1,-17)
                color('black')
                pu()
                goto(-313,-332)
                pd()
                write('请选择球种类(0为最低级球,7为最高级球)',font=('Arial',10,'bold'))
                tracer(1)
                tracer(0)
                key.read_key()
                keyword2=key.read_key()
                for t1 in range(33):
                    clean(16-t1,-17)
                color('black')
                print(22222)
                if balllist[int(keyword2)]==0:
                    pu()
                    goto(-313,-332)
                    pd()
                    write('你没有这个球',font=('Arial',10,'bold'))
                    tracer(1)
                    tracer(0)
                    break
                tracer(1)
                tracer(0)
                q_process(worldpetxy[d2[l1[int(keyword1)]]][0],worldpetxy[d2[l1[int(keyword1)]]][1])
                tracer(1)
                tracer(0)
                sleep(0.5)
                clean(worldpetxy[d2[l1[int(keyword1)]]][0],worldpetxy[d2[l1[int(keyword1)]]][1])
                print(33333)
                if randint(1,100)<=20*int(keyword2)+30-l1[int(keyword1)]:
                    seccess=True
                else:
                    seccess=False
                if seccess:
                    while 1:
                        worldpetlv=randint(1,50)
                        if worldpetlv in worldpetlevel:
                            pass
                        else:
                            worldpetlevel[d2[l1[int(keyword1)]]]=randint(1,50)
                            break
                    print(4444)
                    mutate=not(bool(randint(0,999)))
                    v1=randint(1,1000)
                    print(55555)
                    if v1<=300:
                        worldpet[d2[l1[int(keyword1)]]]='1'
                    elif v1<=600:
                        worldpet[d2[l1[int(keyword1)]]]='2'
                    elif v1<=900:
                        worldpet[d2[l1[int(keyword1)]]]='3'
                    elif v1<=990:
                        worldpet[d2[l1[int(keyword1)]]]='0'
                    elif v1<=999:
                        worldpet[d2[l1[int(keyword1)]]]='2.718'
                    elif v1<=1000:
                        worldpet[d2[l1[int(keyword1)]]]='3.141'
                    while 1:
                        worldpetx=randint(-15,15)
                        worldpety=randint(-15,15)
                        if (worldpetx==4 and worldpety==11) or (worldpetx==playerx and worldpety==playery) or (worldpetx==playerx and worldpety==playery+1) or [worldpetx,worldpety] in worldpetxy:
                            pass
                        else:
                            worldpetxy[d2[l1[int(keyword1)]]][0]=worldpetx
                            worldpetxy[d2[l1[int(keyword1)]]][1]=worldpety
                            break
                    print(666666)
                choosepet(worldpetxy[d2[l1[int(keyword1)]]][0],worldpetxy[d2[l1[int(keyword1)]]][1],worldpet[d2[l1[int(keyword1)]]],worldpetlevel[d2[l1[int(keyword1)]]])
#        except:
#            pass
    if keyworld=='esc':
        break
    tracer(1)
#------------------------------------------------#
'''    if keyworld=='w':
        if [playerx,playery+2] in worldpetxy or (playerx==4 and playery+2==11) or playery+2==16:
            pass
        else:
            with open("C:\\Users\\ziyun\\Desktop\精灵城：世界\\player's name\\"+name+'.txt','r') as name_file:
                name_file.seek(0)
                allfile=name_file.readlines()
                allfile[2]=str(playery)+'\n'
            with open("C:\\Users\\ziyun\\Desktop\精灵城：世界\\"+name+'.txt','w+') as name_file:
                name_file.writelines(allfile)
    if keyworld=='s':
        if [playerx,playery-1] in worldpetxy or (playerx==4 and playery-1==11) or playery-1==-16:
            pass
        else:
            with open("C:\\Users\\ziyun\\Desktop\精灵城：世界\\player's name\\"+name+'.txt','r') as name_file:
                name_file.seek(0)
                allfile=name_file.readlines()
                allfile[2]=str(playery)+'\n'
            with open("C:\\Users\\ziyun\\Desktop\精灵城：世界\\player's name\\"+name+'.txt','w+') as name_file:
                name_file.writelines(allfile)
    if keyworld=='d':
        if ([playerx+1,playery] in worldpetxy or (playerx+1==4 and playery==11) or playerx+1==16) or ([playerx+1,playery+1] in worldpetxy or (playerx+1==4 and playery+1==11) or playerx+1==16):
            pass
        else:
            with open("C:\\Users\\ziyun\\Desktop\精灵城：世界\\player's name\\"+name+'.txt','r') as name_file:
                name_file.seek(0)
                allfile=name_file.readlines()
                allfile[2]=str(playerx)+'\n'
            with open("C:\\Users\\ziyun\\Desktop\精灵城：世界\\player's name\\"+name+'.txt','w+') as name_file:
                name_file.writelines(allfile)
                name_file.writelines(allfile)
    if keyworld=='a':
        if ([playerx-1,playery] in worldpetxy or (playerx-1==4 and playery==11) or playerx-1==-16) or ([playerx-1,playery+1] in worldpetxy or (playerx-1==4 and playery+1==11) or playerx-1==-16):
            pass
        else:
            with open("C:\\Users\\ziyun\\Desktop\精灵城：世界\\player's name\\"+name+'.txt','r') as name_file:
                name_file.seek(0)
                allfile=name_file.readlines()
                allfile[2]=str(playerx)+'\n'
            with open("C:\\Users\\ziyun\\Desktop\精灵城：世界\\player's name\\"+name+'.txt','w+') as name_file:
                name_file.writelines(allfile)'''
