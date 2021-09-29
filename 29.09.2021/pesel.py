def kto(pesel):
    a = str(pesel)
    b = a[9]
    c = int(b)
    czy_parzysta = c
    def czy_parzysta(c):
      if pesel%2==0:
        return "K"
      else:
        return "M"
pesel = int(input("Podaj pesel: "))
kto(pesel)