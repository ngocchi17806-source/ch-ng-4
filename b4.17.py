print('NGUYEN NGOC CHI 245752021610164')
def sum_of_divisors(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total
# nhap so nguyen duong n
n = int(input("nhap so nguyen duong n:"))

print(f"Cac so nguyen duong nho hon {n} co tong cac uoc so lon hon chinh no:")
for i in range(1, n):
    if sum_of_divisors(i) > i:
        print(i)
