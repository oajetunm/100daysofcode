def birthdayCakeCandles(ar):
    max_n = max(ar)
    g = 0
    for x in range(len(ar)):
        if ar[x] == max_n:
            g+=1
    print(g)
a = [3, 2, 1, 3]
birthdayCakeCandles(a)


