#emdereçamento em 2 niveis
import random #importe o random
Memoria_logica=["P0","P1","P2","P3","P4"]#tabela de memória lógica
tabela_de_pag=[4,2,1,0,3]#tabela de páginas
Memoria_fisica=["P3","P2","P1","P0","P4"]#Memofia fisica
pg=random.choice(tabela_de_pag)#sorteando um dos items da tabela de páginas
o=random.choice(Memoria_logica)#sorteando um dos items da tabela de memória lógica
for i in tabela_de_pag:#aqui vai mostrar os valores da tabela de pag
    if(pg==i):#quando a o valor de pag for igual ao que tem na lista
        Memoria_fisica.insert(i,o)#adiciona o item na pag
        print(Memoria_fisica)#printa a pag
