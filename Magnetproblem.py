import time

def Force(point,arr):

    force = 0
    for val in arr:
        if val == point:
            continue
        if val < point:
            force -= 1/abs(val-point) 
        else:
            force +=1/abs(val-point)
           
    return round(force,4)
    
    
def Find(arr,N):
    eq = [None]*100
    ind =0
    
    
    for p in range(N-1):
        #print('Equlibrium in between {} and {}'.format(arr[p],arr[p+1]))
        beg = arr[p]
        end = arr[p+1]
        #print('beg : {}, end : {}'.format(beg,end))

        
        while beg <= end:
             mid = beg+(end-beg)/2
             mid = round(mid,10)

             force = Force(mid,arr)

             #print('mid : {} , force : {}'.format(mid,force))
             
             if force == 0:
                 eq[ind]=round(mid,2)
                 ind +=1
                 break
             
             elif force > 0:
                 end = mid
                 
             elif force < 0:
                 beg = mid
     
    return eq[:ind]    

if __name__=='__main__':
    T = int(input())
    #first = time.time()

    for _ in range(T):
        N = int(input())
        arr= list(map(int,input().split()))
        #print(type(arr))
        print(Find(arr,N))
    #print('Program completed in {} secs'.format(time.time()-first))    
