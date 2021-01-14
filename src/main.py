def mergeSort(array):
    lenght = len(array)
    #print(array)
    if lenght == 1:
        return array
    if lenght == 2:
        if array[0] > array[1]:
            temporary = array[1]
            array[1] = array[0]
            array[0] = temporary
    else:
        mid = lenght/2
        rightArray = array[int(mid):]
        leftArray = array[:int(mid)]
        rightArray = mergeSort(rightArray)
        leftArray = mergeSort(leftArray)
        rightCounter = 0
        leftCounter = 0
        leftLenght = len(leftArray)
        rightLenght = len(rightArray)
        while rightCounter + leftCounter < lenght:
            if leftCounter == leftLenght:
                array[rightCounter + leftCounter] = rightArray[rightCounter]
                rightCounter += 1
            elif rightCounter == rightLenght:
                array[rightCounter + leftCounter] = leftArray[leftCounter]
                leftCounter += 1
            elif rightArray[rightCounter] > leftArray[leftCounter]:
                array[rightCounter + leftCounter] = leftArray[leftCounter]
                leftCounter += 1
            elif leftArray[leftCounter] > rightArray[rightCounter]:
                array[rightCounter + leftCounter] = rightArray[rightCounter]
                rightCounter += 1
            elif leftArray[leftCounter] == rightArray[rightCounter]:
                array[rightCounter + leftCounter] = rightArray[rightCounter]
                rightCounter += 1
                array[rightCounter + leftCounter] = leftArray[leftCounter]
                leftCounter += 1
            else:
                print ("illegal state")
                exit(-1)
            #print ("lenght = " + str(lenght) + "left counter = " + str(leftCounter) +  "right counter = " + str(rightCounter))
    return array

array = [63, 35, 4, 61, 81, 69, 92, 28, 8, 100, 3, 52, 60, 45, 76, 20, 83, 83, 34, 76, 3, 60, 94, 19, 45, 19, 54, 41, 25, 76, 29, 55, 51, 51, 21, 86, 39, 66, 45, 85, 44, 17, 84, 20, 99, 62, 57, 97, 25, 1, 90, 66, 69, 88, 80, 22, 35, 77, 60, 57, 43, 7, 74, 73, 24, 63, 48, 53, 9, 4, 31, 42, 92, 86, 12, 78, 63, 87, 50, 10, 57, 70, 33, 28, 45, 37, 42, 73, 14, 61, 81, 76, 3, 64, 88, 1, 57, 61, 45, 30, 48, 40, 64, 76, 90, 70, 97, 85, 93, 64, 12, 22, 36, 95, 12, 32, 66, 29, 85, 19, 49, 93, 63, 79, 3, 7, 12, 100, 84, 45, 63, 18, 17, 74, 80, 60, 22, 20, 85, 94, 41, 4, 14, 55, 36, 40, 66, 95, 20, 19, 25, 16, 46, 100, 32, 98, 40, 66, 38, 59, 67, 68, 16, 81, 37, 10, 10, 74, 22, 60, 16, 73, 89, 92, 96, 38, 91, 91, 39, 99, 84, 83, 84, 20, 66, 65, 96, 46, 71, 30, 1, 72, 21, 72, 36, 85, 64, 99, 36, 46]
print(array)
array = mergeSort(array)
print(array)