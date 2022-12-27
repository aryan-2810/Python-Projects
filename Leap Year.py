start = int(input("Enter start year: "))
end = int(input("Enter end year: "))
while start < end:
    if start % 4 == 0:
        if start % 100 == 0:
            if start % 400 == 0:
                print("{} is a leap year".format(start))
            else:
                print("{} is not a leap year".format(start))
        else:
            print("{} is a leap year".format(start))
    else:
        print("{} is not a leap year".format(start))
    start += 1
