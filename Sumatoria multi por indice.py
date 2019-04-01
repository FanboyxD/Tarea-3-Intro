def sumatoria_indice(lista):
    if isinstance(lista,list):
        return mul_aux(lista,1)
def mul_aux(lista,cond):
    if lista==[]:
        return 0
    elif isinstance(lista[0],list):
        return mul_aux(lista[0]+lista[1:],cond)
    else:
        return lista[0]**cond+mul_aux(lista[1:],cond+1)
