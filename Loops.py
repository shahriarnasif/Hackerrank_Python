if __name__ == '__main__':
    n = int(input())
    #1st solution
    [print(i**2) for i in range(n)]
    #2nd solution
    print(*[num**2 for num in range(n)],sep='\n')
    ## '*' used for unpacking list items