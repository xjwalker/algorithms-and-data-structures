n = 1200

def recursion(num, count =0):
    if num % 10 != 0:
        return count
    count += 1
    return recursion(num/10, count)

print(recursion(n))