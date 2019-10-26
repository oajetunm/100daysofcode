'''Compare the Triplets

'''


def compareTriplets(a, b):
    al = 0
    bo = 0
    # for i in range(len(a)):
    #     for j in range(len(b)):
    for i in range(len(a)):
        # for j in range(len(b)):
        if a[i] > b[i]:
            al +=1
        elif a[i] < b[i]:
            bo +=1
        elif a[i] == b[i]:
            pass
    return al,bo

a = [5, 6, 7]
b= [3,6,10]
print(compareTriplets(a,b))
