def print_formatted(number):
    # your code goes here
    

    n = number
    m = n
    w = 0
    while m > 0:
        m //= 2
        w += 1
    fom = "{0:" + str(w) + "d} " +"{0:" + str(w) + "o} " +"{0:" + str(w) + "X} " +"{0:" + str(w) + "b} "

    for i in range(1,n+1):
        print(fom.format(i))

