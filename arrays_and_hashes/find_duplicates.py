def findDups(value):
    lkp = []

    for i in value:
        if i in lkp:
            return True
        lkp.append(i)

    return False


if __name__ == '__main__':
    print(findDups([1,1,2,2,1,1,3,3,2,2,6]))
    print(findDups([1, 2, 3, 6]))