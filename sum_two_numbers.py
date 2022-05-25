def pairwisesum(lst, n, total):
    for i in range(len(lst)-1):
        for a,j in enumerate(lst):
            sum = lst[i] +lst[ i + 1]
        if (sum == total):
            print(f"[{i},{i +1}]")
lst=[10,2,3,4,4,8,5,5,]
size=len(lst)
total=  12
pairwisesum(lst,size,total)
