import random

ra_usados = set()
id_usados = set()

def gerar_ra():
    while True:
        ra = random.randint(100000, 999999)
        
        if ra not in ra_usados:
            ra_usados.add(ra)
            return ra
        
def gerar_id():
    while True:
        id = random.randint(100000, 999999)
        
        if id not in id_usados:
            id_usados.add(id)
            return id
