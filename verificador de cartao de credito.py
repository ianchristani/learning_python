#pode estar em um arquivo externo
clientes=[['ian',123456789,987,5000], ['eric',456789,321,5000],['marina',789456,654,5000]]

class Analise:
    
    def __init__(self,nome,cartao,dv,credito):
        self.nome=nome
        self.cartao=cartao
        self.dv=dv
        self.credito=credito
        print('iniciando averificacao...')
        print()
        
        
    def verificacao(self,quantia,digito):
#checa cada numero de cartao
            for n in clientes:
                if self.cartao==n[1] and digito==n[2]:
                    if quantia<=self.credito:
                        print()
                        print('operacao APROVADA')
                        self.credito=self.credito-quantia
#se clientes estivessem em um arquivo externo, aqui teria que ter uma ref externa com opcao 'w'
                        n[3]=self.credito
                        print(f'Cliente {self.nome}, seu credito remanescente e {self.credito}')
                    else:
                        print('credito insuficiente')

#fazendo test com a marina
pessoa=Analise(clientes[2][0],clientes[2][1],clientes[2][2],clientes[2][3])
quantia=int(input('valor da compra: '))
digito=int(input('digito verificador: '))
pessoa.verificacao(quantia,digito)
