start = int(input("Set the start value: "))
end = int(input("Set the end value: "))
fir_mul = int(input("Set the value for 'Fizz': "))
sec_mul = int(input("Set the value for 'Buzz': "))

for i in range(start, end+1):
    if i % fir_mul == 0 and i % sec_mul == 0:
        print("FizzBuzz")
    elif i % fir_mul == 0:
        print("Fizz")
    elif i % sec_mul == 0:
        print("Buzz")
    else:
        print(i)
    
