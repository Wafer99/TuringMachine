def reverter(string):
    Reversion = ""
    for number in string:
        if number in "1":
            Reversion = Reversion + "0"
        if number in "0":
            Reversion = Reversion + "1"
    return Reversion
print(reverter(input("Enter a String of 0 and 1 and it will be reverted! Everything else will be skipped: ")))