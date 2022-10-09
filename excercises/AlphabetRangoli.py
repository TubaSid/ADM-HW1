import string
def print_rangoli(size):

        

    alpha = string.ascii_lowercase

    num = size

    def srange(N):
        return list(range(N))+list(range(N-2,-1,-1))

    for i in srange(num):
        print('-'.join([alpha[num-j-1] for j in srange(i+1)]).center(4*(num-1)+1,'-'))
