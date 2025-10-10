#Encripta la clave del usuario (reversa + string extra si 'indice caracter' es par)
def hashClave(claveLimpia:str):
    claveEncriptada = ""
    for i in range(len(claveLimpia)-1, -1, -1):#Desde -1 y restando (reversa)
      claveEncriptada += claveLimpia[i] if i%2 else f"[{claveLimpia[i]}]3NCR1PT@D0"
    return claveEncriptada