largeIndex = 3
smallIndex = 0
isFound = False
with open('input.txt') as f:
    for i in f:
        while(largeIndex < len(i)):
            temparr1 = []
            temparr1.extend(i[smallIndex:(largeIndex+1)])
            temp1 = smallIndex
            temp2 = largeIndex
            while(temp1 <= temp2):
                first_element = temparr1.pop(0)
                if len(temparr1) > 0:
                    if first_element in temparr1:
                        break
                temp1 += 1
            if len(temparr1) == 0:
                print(largeIndex+1)
                isFound = True
                break    
      

            largeIndex += 1
            smallIndex += 1
        if(isFound):
            break
#####
####End of part 1