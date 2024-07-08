# module_2_4.py  Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    a_prime_number = True
    for j in range(1, numbers[i]):
        if j == 1 or j == numbers[i]:
            continue
        if numbers[i]%j == 0:
            a_prime_number = False
            break
    if a_prime_number == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print('Primes:', primes)
print('Not Primes:', not_primes)
