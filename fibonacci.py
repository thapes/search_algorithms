def fib(n, value_dict = {}):
    if n == 0 or n == 1:
        return n
    if value_dict.get(n):
        return value_dict[n]
    else:
        value_dict[n] = fib(n-2, value_dict) + fib(n-1, value_dict)
        return value_dict[n]
    

if __name__ == '__main__':

    print(fib(50))