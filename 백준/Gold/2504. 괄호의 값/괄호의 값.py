
# # 문자열 입력
# input_str = list(input())

# stack_2 = 0
# stack_3 = 0
# fluc = 0
# result = 0

# for i in range(len(input_str)):
#     if input_str[i] == '(':
#         stack_2 += 1
#         fluc = 1
#     elif input_str[i] == ')':
#         if fluc == 1:
#             result += (2 ** stack_2) * (3 ** stack_3)
#         stack_2 -= 1    
#         fluc = -1    
#     elif input_str[i] == '[':
#         stack_3 += 1
#         fluc = 1
#     elif input_str[i] == ']':
#         if fluc == 1:
#             result += (2 ** stack_2) * (3 ** stack_3)
#         stack_3 -= 1    
#         fluc = -1 
#     else: pass
    
#     if stack_2 < 0 or stack_3 < 0 :
#         result = 0
#         break
# if stack_2 != 0 or stack_3 != 0:
#     result = 0
# print(result)


input_str = list(input())

stack = []
fluc = 0
result = 0

for i in range(len(input_str)):
    if input_str[i] == '(':
        stack.append(2)
        fluc = 1
    elif input_str[i] == ')':
        if input_str[i - 1] == '[':
            result = 0
            break
        if fluc == 1:
            result += (2 ** stack.count(2)) * (3 ** stack.count(3))
        if len(stack) > 0 and stack[-1] == 2:
            del stack[-1]
        else:
            result = 0
            break
        fluc = -1    
    elif input_str[i] == '[':
        stack.append(3)
        fluc = 1
    elif input_str[i] == ']':
        if input_str[i - 1] == '(':
            result = 0
            break
        if fluc == 1:
            result += (2 ** stack.count(2)) * (3 ** stack.count(3))
        if len(stack) > 0 and stack[-1] == 3:
            del stack[-1]
        else:
            result = 0
            break
        fluc = -1 
        
    else: pass
    #print(f'{stack.count(2)} {stack.count(3)} {result} {stack} ')
    
    if stack.count(2) < 0 or stack.count(3) < 0 :
        result = 0
        break
if len(stack) != 0:
    result = 0
print(result)

