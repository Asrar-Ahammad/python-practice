def fibbo(n):
    if n<= 1:
        return n
    else:
        return(fibbo(n-1)+fibbo(n-2))
terms = int(input('Enter the range :'))
if terms<0:
    print('Enter positive range')
else:
    print('The fibbinacci series is')
    for i in range(terms+1):
        print(i,'th term ',fibbo(i))
        

