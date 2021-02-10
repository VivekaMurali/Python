try:
    a=open('append.txt','a')
    x=input('Enter a text:')
    while x:
        a.write('\n'+x)
        x=input('Enter a text:')
    a.close()
except IOError as io:
    print(io)
