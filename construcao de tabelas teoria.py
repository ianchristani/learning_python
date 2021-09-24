#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:03:24 2020

@author: ian
"""

contruindo tabelas com bom visual
exemplo1:
'{:>13,.2f}'.format(100000)

Leia-se, então, {:>13,.2f} como: 
formate este número float com 2 casas decimais, utilizando a vírgula como separador dos milhares, 
alinhado à direita em um espaço de 13 caracteres. Sera entao:

   100,000.00


As chaves, {}, definem um grupo referente aos parâmetros de format;
Os dois pontos, :, iniciam as regras de formatação do valor;
O sinal de maior, >, define que o alinhamento à direita;
O número 13, 13 mesmo, define o espaço total da saída;
A vírgula, ,, representa o caractere separador dos milhares;
O ponto, ., inicia as regras de formatação da parte decimal;
O número 2, 2 mesmo, define que haverá apenas 2 casas decimais;
A letra f, f, define que a entrada será um tipo float;
o ^ centraliza


exemplo2:
    
tupla = [1, 100000.00, 9282.21, 8333.33, 948.88, 91666.67]
print('{:^6}   {:>13,.2f}   {:>9,.2f}   {:>11,.2f}   {:>9,.2f}   {:>11,.2f}'.format(*tupla))

sera:
  1         100,000.00    9,282.21      8,333.33      948.88     91,666.67 
'''