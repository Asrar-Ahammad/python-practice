try:
    file = open('tempCodeRunnerFile.txt','r')
    content=file.read()
    print(content)
    loc=file.tell()
    print(loc)
finally:
    file.close()
