def counter():
    start = int(input("What's the starting value?" ))
    end = int(input("What's the ending value?" ))
    step = int(input("What's the step? "))

    count = 0

    for i in range(start, end+1, step):
        print(i)
        count += 1

    if start == 0:
        print("The total number of multiples of {0} between {1} and {2} is {3}. '0' is not counted".format(step, start, end, count-1))
    else:
        print("The total number of multiples of {0} between {1} and {2} is {3}.".format(step, start, end, count))

counter()