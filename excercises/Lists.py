

if __name__ == '__main__':
    N = int(input())
    
    arr=[]
    array=[]
    for i in range(N):
        array.append(input())
    #for i in range(N):
        c=len(array[i].split())
        if c==1:
            func=(array[i].split())     
            if func==["pop"]:
                arr.pop()
                #print(arr)
            elif func==["print"]:
                print(arr)
            elif func==["reverse"]:
                arr.reverse()
                #print(arr)
            elif func==["sort"]:
                arr.sort()
                #print(arr)
        elif c==2:
            func, val=(array[i].split())
            if func=="append":
                arr.append(int(val))
                #print(arr)
            elif func=="remove":
                #print(val)
                arr.remove(int(val))
                #print(arr)
        elif c==3:
            func, idx, val=(array[i].split())
            if func=="insert":
                arr.insert(int(idx),int(val))
                #print(arr)


        
