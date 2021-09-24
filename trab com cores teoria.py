#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:20:09 2020

@author: ian
"""
'''
imprime a cores sendo necessario para innicializacao, quebra ou finalizacao a sequencia \033[m
entre o [ e o m vao os cod separados por ponto e virgula:
tipo de fonte:
0 padrao
1 negrito
4 sublinhado
7 negativo
 cor do texto qua vai de 30 a 37
 backgroud que vai de 40 a 47
'''
print('\033[31mteste de cores\033[m!!!!!')
a=2
b=6
print('os numero coloridos sao \033[31m{}\033[m e \033[34m{}\033[m'.format(a,b))