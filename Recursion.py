## Reverse String with Recursion:

###
def reverse(string):
    if len(string) == 1:
      return string
    else:
      return reverse(string[1:]) + string[0]
###

##	Check for Palindrome:

###
def Palindrome(string):
    if reverse(string) == string:
        return True
###

##	Decimal to Binary:

###
def toBin(n):
    if n//2 == 0:
        return str(n%2)
    else:
         return toBin(n//2) + str(n%2)
###

##	Sum of Natural Numbers:

###
def sumAll(n):
    if n == 1:
        return n
    else:
        return sumAll(n-1) + n
###

##	Binary Search:

###
def binaryS(array, value, start, end):
    res = int((end + start)/2)
    if array[res] > v:
        return binaryS(array, value, start, res)
    if array[res] < v:
        return binaryS(array, value, res, end)
    if array[res] == v:
        return res
###

##	Fibonacci (Non-Optimized)

###
def Fibonacci(v):
    if v == 1 or v == 0:
        return v
    else:
        return Fibonacci(v-1) + Fibonacci(v-2)
###

##	Merge Sort
  
###
def merge(data0, data1):

    dataA = data0.copy()
    dataB = data1.copy()

    dataR = []
    run = True
    while run:
        if dataA[0] <= dataB[0]:
            dataR.append(dataA[0])
            del dataA[0]

        if not dataA:
            break

        if dataB[0] <= dataA[0]:
            dataR.append(dataB[0])
            del dataB[0]

        if not dataB:
            break

    dataR.reverse()

    if dataA:
        for x in dataA:
            for y in range(len(dataR)):
                if x >= dataR[y]:
                    dataR.insert(y, x)
                    break
    if dataB:
        for x in dataB:
            for y in range(len(dataR)):
                if x >= dataR[y]:
                    dataR.insert(y, x)
                    break
                
    dataR.reverse()
    return dataR

def mergeSort(data):
    if len(data) <= 1:
        return data
    else:
        mid = int(len(data)/2)
        data2 = mergeSort(data[:mid])
        data3 = mergeSort(data[mid:])

    return merge(data2, data3)    
###
