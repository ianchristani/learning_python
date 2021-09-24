class Analisador:
    
    def __init__(self,frase):
        self.frase=frase
        print(self.frase)
        
    def vogal(self):
        lista=['a','e','i','o','u']
        for i in self.frase:
            if i in lista:
                print(i)
                
    def tamanho(self):
        print(len(self.frase))
        
    
        
            

frase=str(input('digite uma frase: '))
sentenca=Analisador(frase)
sentenca.vogal()
sentenca.tamanho()

