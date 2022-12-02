print("input command(0->float)(1->int): ")
cmnd = int(input())

if cmnd == 0:
    print("Input undercommand (0=> 2->10)(1=> 10->2) -> "); undercommand = int(input())
    print("input your number (after '.' -> "); N = input(); N = N.upper(); N = str(N)
    if undercommand == 0:
        fin = 0; degr = -1
        print("Now you're turning fraction to smth another.")
        lst = []; numlist = []
        for i in N:
            if (i == "1"  ): i = "1"
            elif (i == "2"): i = "2"
            elif (i == "3"): i = "3"
            elif (i == "4"): i = "4"
            elif (i == "5"): i = "5"
            elif (i == "6"): i = "6"
            elif (i == "7"): i = "7"
            elif (i == "8"): i = "8"
            elif (i == "9"): i = "9"
            elif (i == "0"): i = "0"
            elif ("A" == i): i = " 10"
            elif ("B" == i): i = " 11"
            elif ("C" == i): i = " 12"
            elif ("D" == i): i = " 13"
            elif ("E" == i): i = " 14"
            elif ("F" == i): i = " 15"
            numlist.append(i)
        while (len(numlist) > 0):
            fin = fin + int(numlist[0]) * (pow(2, degr))
            degr = degr - 1
            print(fin)
            numlist.pop(0)
    if undercommand == 1:
        numb = N
        print("Now you're turning 10th to 2nd.")
        print("Please, input length of required base -> ");
        listlen = int(input())
        lst = []
        while (len(lst) < listlen) or (numb != 0):
            if numb == 0: break
            if numb * 2 < 1:
                lst.append('0')
            elif numb * 2 > 1:
                lst.append('1')
            numb = numb * 2
            if numb > 1: numb = numb - 1
            if len(lst) == listlen:
                print(*lst)
                break

if cmnd == 1:
    fin = 0; degr = 0; n = []
    print("input number -> "); N = input(); N = str(N); N = N.upper()
    print("input your mantiss"); mantiss = int(input())
    print("Input required base: "); dl = int(input())
    #separating
    for i in N:
        if   ("A" == i): i = "10"
        elif ("B" == i): i = "11"
        elif ("C" == i): i = "12"
        elif ("D" == i): i = "13"
        elif ("E" == i): i = "14"
        elif ("F" == i): i = "15"
        n.append(i)
    #turn into 10
    while len(n) > 0:
        fin = fin + int(n[-1]) * ((mantiss ** degr))
        del n[-1]
        degr += 1
    print("10 ->", fin)
    #turn into another system
    lst = []
    while fin > 0:
        n = fin
        if n % dl < 10: lst.append(n % dl)
        elif n % dl == 10: lst.append("A")
        elif n % dl == 11: lst.append("B")
        elif n % dl == 12: lst.append("C")
        elif n % dl == 13: lst.append("D")
        elif n % dl == 14: lst.append("E")
        elif n % dl == 15: lst.append("F")
        fin = fin // dl
    lst.reverse()
    print(*lst)
    print("============================")