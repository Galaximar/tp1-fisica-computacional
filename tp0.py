# Ejercicio 1


original_e = 2.7182818284590


def exp1():
    n = 50
    factorial = 1
    e = 0
    for i in range(n):
        factorial *= i or 1
        e += 1**i/(factorial or 1)
    return e


def exp2():
    e = 0
    n = 1
    # Compruebo con el valor real de e y itero hasta que la diferencia sea menor a 1e-14
    while abs(e - original_e) > 1e-14:
        e = (1 + 1 / n) ** n
        n *= 2
    return e


def denominador(x=2):
    if x == 300:
        return 0.9
    return 1+x-x/denominador(x+1)


def exp3():
    return 1+1/(1-1/denominador())


print("1_a", exp1())
print("1_b", exp2())
print("1_c", exp3())

# Ejercicio 2


def int_to_base3(n):
    if n == 0:
        return "0"

    base3 = ""
    while n > 0:
        remainder = n % 3
        base3 = str(remainder) + base3
        n //= 3
    return base3


def base3_to_int(base3_num):
    decimal = 0
    base3_str = str(base3_num)[::-1]

    for i in range(len(base3_str)):
        digit = int(base3_str[i])
        decimal += digit * (3 ** i)

    return decimal


print("2_a", "Número en base 10: 170141183460469231731687303715884105728",
      "Número convertido en base 3:", int_to_base3(170141183460469231731687303715884105728))
print("2_b", "Número en base 3: 101100201022001010121000102002120122110122221010202000122201220121120010200022002", "Número convertido en base 10:", base3_to_int(
    101100201022001010121000102002120122110122221010202000122201220121120010200022002))

# Ejercicio 4


def isPrime(num):
    n = 2
    while n < num:
        if num < 4:
            return True
        if num % n == 0:
            return False
        n += 1
    return True


def findTwinPrimes(n):
    twin_primes = []
    num = 2
    while len(twin_primes) < n:
        if isPrime(num) and isPrime(num + 2):
            twin_primes.append((num, num + 2))
        num += 1
    return twin_primes


print("4_a", "31 es Primo:", isPrime(31))
print("4_a", "6 es Primo:", isPrime(6))
print("4_b", "Primeros 100 primos gemelos:", findTwinPrimes(100))
