monsterMap = {}

def rpg(list):
    exp = list[1]
    listMod = list[2:]
    count = 0
    for i in range(len(listMod) - 2):
        if i % 2:
            monsterMap[listMod[i]] = listMod[i + 2]
        else:
            monsterMap[listMod[i]] = listMod[i + 2]
    for key,value in monsterMap.items():
        if exp >= key:
            count += 1
            exp += value

    print(count)


list = [2,123,78,130,10,0]
list1 = [3,100,101,100,304,100,1,524]
rpg(list)
rpg(list1)
