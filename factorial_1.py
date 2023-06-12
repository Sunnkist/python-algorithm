a = int(input())

def fec(n):
    if n <= 1:
        #print("end of fatorial")
        return 1
    return n * fec(n-1)

print(fec(a))