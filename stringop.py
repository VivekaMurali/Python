def StrRev(s):
    r=s[::-1]
    return r
def UppCount(s):
    count=0
    for i in s:
        if i.isupper():
            count+=1
    return count
def LowCount(s):
    lc=0
    for i in s:
        if i.islower():
            lc+=1
    return lc

def Palindrome(s):
    if s==s[::-1]:
        return 'True'
    else:
         return 'False'
        
def Pangram(s):
    a='abcdefghijklmnoprstuvwxyz'
    for i in a:
        if i not in s.lower():
            return 'False'
    return 'True'
