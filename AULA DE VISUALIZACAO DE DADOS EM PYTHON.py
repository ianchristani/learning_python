#importanto a biblioteca para visualizacao de dados em Python
import matplotlib.pyplot as plt

#pontos do grafico
x=[1,2,5]
y=[2,3,7]

#tracando o grafico de linha
plt.plot(x,y)
#colocando titulo no grafico
plt.title('meu primeiro grafico')
plt.xlabel('label do eixo X')
plt.ylabel('label do eixo Y')
plt.show()




#pontos do grafico
x1=[1,3,5,7,9]
y1=[2,3,7,1,5]

x2=[2,4,6,8,10]
y2=[3,5,10,1,0]

#tracando o grafico de barra com legenda
plt.bar(x1,y1,label='dados1')
plt.bar(x2,y2,label='dados2')
plt.legend()

#colocando titulo no grafico
plt.title('meu primeiro grafico')
plt.xlabel('label do eixo X')
plt.ylabel('label do eixo Y')
plt.show()




#pontos do grafico
x1=[1,3,5,7,9]
y1=[2,3,7,1,5]

#tracando o grafico de dispersao (scatterplot) com pontos em vermelho
plt.scatter(x1,y1,label='dados1',color='r')
plt.legend()

#se quiser ligar os pontos com reta
plt.plot(x1,y1,label='dados1')

#colocando titulo no grafico
plt.title('meu primeiro grafico')
plt.xlabel('label do eixo X')
plt.ylabel('label do eixo Y')
plt.show()




#pontos do grafico
x1=[1,3,5,7,9]
y1=[2,3,7,1,5]

#tracando o grafico de dispersao (scatterplot) com triangulos (marker), em vermelho, tamanho (s)
plt.scatter(x1,y1,label='dados1',color='g',marker='^',s=100)
plt.legend()

#se quiser ligar os pontos com reta na cor preta, estilo pontilhado
plt.plot(x1,y1,label='dados1',color='k',linestyle=':')

#colocando titulo no grafico
plt.title('meu primeiro grafico')
plt.xlabel('label do eixo X')
plt.ylabel('label do eixo Y')
plt.show()




#pontos do grafico
x=[1,3,5,7,9]
y=[2,3,7,1,5]
z=[400,200,600,800,1000]

#tracando o grafico de dispersao (scatterplot) com triangulos (marker), em vermelho e tamanho (s) para cada ponto
plt.scatter(x1,y1,label='dados1',color='g',marker='^',s=z)
plt.legend()

#se quiser ligar os pontos com reta na cor preta, estilo pontilhado
plt.plot(x,y,label='dados1',color='k',linestyle=':')

#colocando titulo no grafico
plt.title('meu primeiro grafico')
plt.xlabel('label do eixo X')
plt.ylabel('label do eixo Y')
plt.show()
#salvando com o nome figura1.png com tamanho 300
plt.savefig('figura1.png',dpi=300)
#salvando com o nome figura1.pdf
plt.savefig('figura1.pdf')



#estudo de caso
import matplotlib.pyplot as plt

#lembrar que devemos fornecer o endereco de onde esta o arquivo aqui
dados=open('populacao_brasileira.csv').readlines()
x=[]
y=[]
for i in range(len(dados)):
  #ignorando as linhas vazias
  if i!=0:
  #vamos separar os dados de cada linha por ;
    linha=dados[i].split(';')
  #como quebramos os dados em 2 valores, vamos add no X separado do Y
    x.append(int(linha[0]))
    y.append(int(linha[1]))

plt.bar(x,y)
plt.title('crescimento da pop brasileira 1980-2016')
plt.xlabel('ano')
plt.ylabel('pop x 100.000.000')
plt.show()
plt.savefig('populacao_brasileira.png',dpi=300)



#fazendo grafico BOXPLOT (usado para ver o quao disperso estao os dados)
#sendo que o retangulo principal armazena 50% dos dados, a linha que o corta e a MEDIANA
import matplotlib.pyplot as plt
import random

vetor=[]

for i in range(100):
  numero=random.randint(0,100)
  vetor.append(numero)

plt.boxplot(vetor)
plt.show()



