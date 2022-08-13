def es_bisiesto(anio):
    if(anio % 4 == 0):
        return anio % 400 == 0 if anio % 100 == 0 else True
    return False