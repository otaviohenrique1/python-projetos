def __degree(number):
    power = 1
    while number % (10**power) != number:
        power += 1
    return power
def __getDigits(number):
    digits = []
    degree = __degree(number)
    for x in range(0, degree):
        digits.append(int(((number % (10**(degree-x))) - (number % (10**(degree-x-1)))) / (10**(degree-x-1))))
    return digits

def binaryToDecimal(number):
    list = __getDigits(number)
    decimalValue = 0
    for x in range(0, len(list)):
        if (list[x] is 1):
            decimalValue += 2**(len(list) - x - 1)
    return decimalValue
binaryNum = int(input("Digite o numero binario: "))
print(binaryToDecimal(binaryNum))