# 각 단어의 앞글자를 제일 뒤로 옮기고 'ay'를 붙여주어 출력하기. 다만 알파벳이 아니라면 변경 X
text = input(">> ")
lst = text.split()
print(lst)
result = []
for string in lst:
    if not string.isalpha():
        result.append(string)
    else:
        string = string[::-1]
        temp = list(string)
        temp_string = temp[-1]
        temp[-1] = ""
        temp = temp[::-1]
        string = ''.join(temp)+temp_string+"ay"
        print(string)
        result.append(string)
print(' '.join(result))

# 더 쉬운 풀이
text = input(">> ")
lst = text.split()
return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])