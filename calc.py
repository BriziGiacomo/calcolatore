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
    choose=10
    while(choose!=0)
        choose=input(int("Choose the operation: 1 somma, 2 sottrazione, 3 motliplicazione, 4 divisione"))
        num1=input(float("Inserisci il primo numero"))
        num2=input(float("Inserisci il secondo numero"))
        if choose==1:
            print(calc.somma(num1.num2))
        else if choose==2:
            print(calc.sottrazione(num1.num2))
        else if choose==3:
            print(calc.moltiplicazione(num1.num2))
        else if choose==4:
            print(calc.divisione(num1.num2))