def palindrom_check1():
    userinput = str(input("Write a palindrom: "))

    word = userinput.lower()
    palindrom = word[::-1].lower()

    if word == palindrom:
        return "{} is a palindrom!".format(userinput)
    else:
        return "{} is not a palindrom".format(userinput)

def palindrom_check2():
    userinput = str(input("Write something:\n"))
    if userinput.lower() == userinput[::-1].lower():
        return "palindrom!"
    else:
        return "not a palindrom!"

print(palindrom_check1())
print(palindrom_check2())
