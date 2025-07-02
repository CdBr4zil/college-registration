import random

ra_usados = set()

def gerar_ra():
    while True:
        ra = random.randint(100000, 999999)
        
        if ra not in ra_usados:
            ra_usados.add(ra)
            return ra
