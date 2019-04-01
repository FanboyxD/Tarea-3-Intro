def mult_indice(lista):
    if isinstance(lista,list):
        return multi_aux(lista,0)
def multi_aux(lista,cond):
    if lista==[]:
        return []
    else:
        return ([lista[0]*cond])+multi_aux(lista[1:],cond+1)
    
