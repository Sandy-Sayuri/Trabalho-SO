#emdereçamento em 2 niveis
import random
Memoria_logica=["P0","P1","P2","P3","P4"]
tabela_de_pag=[4,2,1,0,3]
Memoria_fisica=["P3","P2","P1","P0","P4"]
pg=random.randrange(0,4)
o=random.choice(Memoria_logica)
for i in tabela_de_pag:
    if(pg==i):
        fr=int(tabela_de_pag.index(i)) 
        safe=tabela_de_pag[i]
        Memoria_fisica.insert(i,o)
        print(Memoria_fisica)