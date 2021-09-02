#emdereçamento em 2 niveis
Memoria_logica=["P0","P1","P2","P3",]
tabela_de_pag=[6,2,1,0,]
Memoria_fisica=["P3","P2","P1","P0"]
pg=int(input('escreva o numero da pagina:'))
o=str(input('escreva o deslocamento:'))
for i in tabela_de_pag:
    if(pg==i):
        fr=int(tabela_de_pag.index(i)) 
        Memoria_fisica.append(o)#falta o index
        print(Memoria_fisica)
else:
    print('ERRO')


