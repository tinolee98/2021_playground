def sort_by_name(arr):
    # 리스트로 숫자를 받은 뒤에 이를 str형태로 나누어 다시 리스트에 저장.
    # memo에 각 숫자와 매칭되는 영어가 적혀있고 이를 효율적으로 짜보자
    # 영어로 바꾼 뒤 리스트를 sort하여 출력하면 끝.
    memo = [
        {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"},
        {0:"", 2:"twenty",3:"thirty",4:"fourty",5:"fifty",6:"sixty",7:"seventy", 8:"eighty",9:"ninty"},
        {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"},
    ]
    lst = []
    for num in arr:
        temp = list(str(num))
        lst.append(temp[::-1])
        #print(lst)
    for i in range(len(lst)):
        if len(lst[i]) == 1 and lst[i][0] == '0':
            lst[i][0] = "zero"
        else:
            for j in range(len(lst[i])):
                if j == 1 and lst[i][j] == '1':
                    lst[i] = memo[2][arr[i]]
                elif j == 2:
                    lst[i].insert(2,"hundred")
                    pass
                elif lst[i][j].isdigit():
                    lst[i][j] = memo[j][int(lst[i][j])]
            if len(lst[i]) == 4:
        #        print(lst[i])
                lst[i][3] = memo[0][int(lst[i][3])]
        #    print(lst)
    temp = []
    for num in lst:
        if num in ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']:
            temp.append(num)
            continue
        temp.append(num[::-1])
        #print(temp)
    lst = []
    for i in temp:
        if i in ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']:
            lst.append(i)
        else:
            lst.append('-'.join(i[j] for j in range(len(i))))
        #print(lst)
    memo2 = {}
    for i in range(len(lst)):
        memo2[lst[i]] = arr[i]
        print(memo2)
    
    lst.sort()
    print(lst)
    for i in range(len(lst)):
        lst[i] = memo2[lst[i]]
    print(lst)
    return lst
        