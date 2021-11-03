lista = [1,2,3,4,5]

liczba = None

for i in lista:
    
    if liczba == None or liczba > i: 
        liczba = i
        
print ("Najmniejsza liczba na liście to:", liczba)