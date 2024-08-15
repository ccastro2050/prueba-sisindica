from flask import session, render_template,redirect,request
import math

def obtenerDicPaginacion(arreglo,itemsxpagina):
    totalItems=len(arreglo)
    numPaginas=math.ceil(totalItems/itemsxpagina)
    paginaActiva = request.args.get('paginaActiva')
    if paginaActiva==None: paginaActiva='1'            
    posInicial=(int(paginaActiva)-1)*itemsxpagina
    posFinal=posInicial+itemsxpagina
    if posFinal>totalItems: posFinal=totalItems
    rango=range(posInicial,posFinal)
    itemsMostrados=len(rango)
    itemsCombo2=[5,10,20,30,50,100,200,1]
    paginacion={
        "itemsxpagina":itemsxpagina,
        "totalItems":totalItems,
        "numPaginas":numPaginas,
        "paginaActiva":paginaActiva,
        "posInicial":posInicial,
        "rango":rango,
        "itemsMostrados":itemsMostrados,
        "itemsCombo2":itemsCombo2
        }
    return paginacion