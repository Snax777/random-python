def counter():
    start = int(input("What's the starting value?" ))
    end = int(input("What's the ending value?" ))
    step = int(input("What's the step? "))
    count = 0
    for i in range(start, end+1, step):
        print(i)
        count += 1
    print("The toatl number of multiples of {0} are {1}.".format(step, count-1))

counter()