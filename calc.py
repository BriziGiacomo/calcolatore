class Calc:
    def somma(self,num1,num2):
        return num1+num2
    def sottrazione(self,num1,num2):
        return num1-num2
    def moltiplicazione(self,num1,num2):
        return num1*num2
    def divisione(self,num1,num2):
        return num1/num2
    
    
    
if __name__== "__main__":
    calc=Calc()
    while(True):
        ex=input("Inserisci ex o 0 per spegnere la calcolatrice(qualsiasi altro tasto la farà continuare): ")
        if ex=="ex" or ex=="0":
            break
        num1=float(input("Inserisci il primo numero: "))
        choose=input("Scegli l'operazione: + somma, - sottrazione,  motliplicazione, / divisione: ")
        num2=float(input("Inserisci il secondo numero: "))
        print("")
        if choose=="+":
            print(calc.somma(num1,num2))
        elif choose=="-":
            print(calc.sottrazione(num1,num2))
        elif choose=="*":
            print(calc.moltiplicazione(num1,num2))
        elif choose=="/":
            if num2!=0.0:
                print(calc.divisione(num1,num2))
            else:
                print("Impossibile dividere per 0")
        else :
            print("Operazione non valida")
        print("")    