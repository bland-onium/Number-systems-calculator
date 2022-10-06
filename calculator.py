print("input number: ")
n = input()
n = str(n); fin = 0; degr = 0
print("input your mantiss")
mantiss = int(input())
print("Input required base: ")
dl = int(input())
n = (n.replace("0", " 0"));n = (n.replace("1", " 1"));n = (n.replace("2", " 2"))
n = (n.replace("3", " 3"));n = (n.replace("4", " 4"));n = (n.replace("5", " 5"))
n = (n.replace("6", " 6"));n = (n.replace("7", " 7"));n = (n.replace("8", " 8"))
n = (n.replace("9", " 9"))
while ("A" in n) or ("B" in n) or ("C" in n) or ("D" in n) or ("E" in n) or ("F" in n):
    n = (n.replace("A", " 10"));n = (n.replace("B", " 11"));n = (n.replace("C", " 12"))
    n = (n.replace("D", " 13"));n = (n.replace("E", " 14"));n = (n.replace("F", " 15"))
n = n.split()
while len(n) > 0:
    fin = fin + int(n[-1]) * ((mantiss ** degr))
    del n[-1]
    degr += 1
print("10 ->", fin)
lst = []
while fin > 0:
    n = fin;
    if n % dl < 10: lst.append(n % dl)
    if n % dl == 10: lst.append("A")
    if n % dl == 11: lst.append("B")
    if n % dl == 12: lst.append("C")
    if n % dl == 13: lst.append("D")
    if n % dl == 14: lst.append("E")
    if n % dl == 15: lst.append("F")
    '''------------------------'''
    if n % dl == 16: lst.append("G")
    if n % dl == 17: lst.append("H")
    if n % dl == 18: lst.append("I")
    if n % dl == 19: lst.append("J")
    if n % dl == 20: lst.append("K")
    if n % dl == 21: lst.append("L")
    if n % dl == 22: lst.append("M")
    if n % dl == 23: lst.append("N")
    if n % dl == 24: lst.append("O")
    if n % dl == 25: lst.append("P")
    if n % dl == 26: lst.append("Q")
    if n % dl == 27: lst.append("R")
    if n % dl == 28: lst.append("S")
    if n % dl == 29: lst.append("T")
    if n % dl == 30: lst.append("U")
    if n % dl == 31: lst.append("V")
    if n % dl == 32: lst.append("W")
    if n % dl == 33: lst.append("X")
    if n % dl == 34: lst.append("Y")
    if n % dl == 35: lst.append("Z")
    fin = fin // dl
print(lst)
print("============================")
