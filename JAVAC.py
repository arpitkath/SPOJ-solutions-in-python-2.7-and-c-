# cook your code here
def javac():
    #s=s.split()
    s=raw_input()
    s=list(s)
    un=False
    count=0
    if s[0].isupper() or s[0]=="_":
        return "Error!"
    if s[-1]=="_":
        return "Error!"
    if "_" in s:
        un=True
    for i in range(len(s)):
        if s[i]=="_" and s[i+1]=="_":
            return "Error!"
        if un and s[i].isupper():
            return "Error!"
    if un:
        """for i in range(len(s)):
            if i==len(s)-count:
                break
            if s[i]=="_":
                s[i+1]=s[i+1].upper()
                del s[i]
                count+=1
            ##if i==len(s)-count:
                ##break"""
        while count!=len(s):
            if s[count]=="_":
                s[count+1]=s[count+1].upper()
                del s[count]
            count+=1
    else:
        """for i in range(len(s)+count):
            if s[i].isupper():
                s[i]=s[i].lower()
                s.insert(i,"_")
                count+=1"""
        while count!=len(s):
            if s[count].isupper():
                s[count]=s[count].lower()
                s.insert(count,"_")
            count+=1
            
    return "".join(str(i) for i in s)
while True:
    try:
        print javac()
    except EOFError:
        break