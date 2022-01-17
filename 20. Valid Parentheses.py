
s = "()[]{}"

d = {
    "(" :")" ,
    "{" : "}" ,
    "[" : "]" ,
}
stack = []
print(not stack , len(stack))
for i in s:
    if i in d:
        stack.append(i)
    elif not stack or i!=d[stack.pop()]:
        print(False)
        break
print(not stack)
