import math


def bottom_up_cut_rod(price, n): 
    result = [0 for x in range(n+1)] # Løsnings-tabell, 0..n+1
    result[0] = 0 # Verdien til en stav med lenge 0 = 0
  
    for i in range(1, n+1): # For hver lenge av staven
        max_val = -1
        for j in range(i): # Finn den optimale løsningen
             max_val = max(max_val, price[j] + result[i-j-1]) # her brukes del-løsningen i løsnings-tabellen
        result[i] = max_val # Lagre del-løsning til løsnings-tabellen
  
    return result[n] # Returner optimal løsning for en stav av lenge n.



def main():
    p = [1,5,8,9,10,17,17,20,24,30];    n = 9

    print("Maksimal fortjeneste med n = "+str(n)+" er: ", end="")
    print(bottom_up_cut_rod(p,n))

main()
