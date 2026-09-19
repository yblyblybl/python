from time import*
tf1=input('是否创建玩家(0(no)/1(yes))?')
if tf1=='1':
    name=input('请输入玩家名(不能是空格或含有<>:?|\\/"*):')
    try:
        with open("C:\\python\\python3132\精灵城：世界\\player's name\\"+name+'.txt','r') as name_file:
            pass
        print('该用户已存在')
        sleep(1)
    except:
        try:
            if name=='':
                print('该用户名不合规')
                sleep(1)
            else:
                with open("C:\\Users\\ziyun\\Desktop\精灵城：世界\\player's name\\"+name+'.txt','w') as name_file:
                    name_file.write('0\n0\n0\n10\n5\n1\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0'+('\n'+'0,'*39+'0')*15)#('钱\n个人等级\nplayerx\nplayery\n低级球数量\n普通球数量\n初级球数量\n中级球数量\n高级球数量\n赛季球数量\n珍惜球数量\n赛季珍惜球数量\n区块1拥有状态\n精灵盒子1拥有状态\n精灵盒子2拥有状态\n精灵盒子3拥有状态\n精灵盒子4拥有状态\n精灵盒子5拥有状态\n盒子1的精灵（40个，以‘,’隔开\n盒子2的精灵（40个，以‘,’隔开）\n盒子3的精灵（40个，以‘,’隔开）\n盒子4的精灵（40个，以‘,’隔开）\n盒子5的精灵（40个，以‘,’隔开）\n盒子1的精灵等级（40个，以‘,’隔开）')
        except:
            print('该用户名不合规')
            sleep(1)
