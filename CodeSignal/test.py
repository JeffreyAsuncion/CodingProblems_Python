
sequence = [1,2,3,4,5]
preNum = -99999999999
for num in sequence:
    if not num > preNum:
        print(False)