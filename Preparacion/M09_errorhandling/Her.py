class Herramientas:
    def __init__(self,lista):
        if (type(lista)!= list):
            raise TypeError('El elemento no es una lista')
        else:
            self.lista = lista
        count = 0
        for i in self.lista:
            if (type(i) != int):
                raise TypeError("El elemento",count,"de la lista no es un numero entero:",i)
            if i < 0:
                raise TypeError("El elemento",count,"es un numero negativo:",i)
            count +=1

    def verificar_primo(self):
        lista_resultado = []
        for i in self.lista:
            if (self.primo(i)):
                lista_resultado.append(True)
            else:
                lista_resultado.append(False)
        return lista_resultado

    def temperaturas(self,origen,destino):
        valor_ok = 0
        for i in ("C","K","F"):
            if (i == origen) ^ (i == destino):
                valor_ok +=1
        if valor_ok == 2:
            for i in self.lista:
                print(i,"grados",origen,"equivalen a",self.conversor_temperaturas(i,origen,destino),"grados",destino)
        else:
            raise ValueError("Las unidades seleccionadas no son validas")

    def factoriales(self):
        for i in self.lista:
            print("El factorial del numero",i,"es",self.fact(i))

    def primo(self,pri):
        r = 1
        for i in range(2,pri):
            r *= pri%i
        if r ==0:
            return False
        else:
            return True
    
    def moda(self):
        dic = {}
        for i in self.lista:
            amount = 0
            for j in self.lista:
                if j == i:
                    amount +=1
            dic[i] = amount
        max = 0
        for i in dic:
            if dic[i] > max:
                max = dic[i]
                ind_max = i
        return [ind_max,max]

    def conversor_temperaturas(self,valor, origen, destino):
        if origen == "C":
            if destino == "K":
                valor_final = valor + 273.15
            else:
                valor_final = valor*9/5 + 32
        elif origen == "K":
            if destino == "C":
                valor_final = valor - 273.15
            else:
                valor_final = (valor - 273.15)*(9/5) +32
        elif origen == 'F':
            if destino =="C":
                valor_final = (valor - 32)/(9/5)
            else:
                valor_final = (valor - 32)/(9/5) + 273.15
        else:
            raise ValueError('No se puede interpretar la unidad de origen')
        return valor_final
    
    def fact(self,x):
        if not(type(x) == int):
            print("El valor no es factorizable")
        elif x == 1:
            return 1
        elif x < 1:
            print("El numero debe ser positivo")
        else:
            x = x * self.fact(x - 1)
        return x