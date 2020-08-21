def bubble(num):
    index = len(num) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index):
            if num[i] > num[i+1]:
                sorted = False
                num[i], num[i+1] = num[i+1], num[i]
    return num

print(bubble([4,5,1,2,7,8,4,5,6,9,31,45,5,8,6,4,3,8,2,8,6,4,7,2,7,45,7,57,4,8,7,4,8,4,7575758]))