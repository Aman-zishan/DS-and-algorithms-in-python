#return the index starting from 1 of the first occurance od non duplicate letter from a string

def findletter(s):
    lettermap = {}
    for i in range(len(s)):
        if s[i] in lettermap:
            lettermap[s[i]] += 1
        else:
            lettermap[s[i]] = 1
    flag = 0
    keyFound = ""
    for key,value in lettermap.items():
        if value == 1:
            flag = 1
            keyFound = key
            break

    if(flag):
        print(s.index(keyFound)+1)
    else:
        print(-1)
            

# example input expected o/p : 2
findletter("statistics")
