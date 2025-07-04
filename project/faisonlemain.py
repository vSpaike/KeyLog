import msvcrt

"""
récupère touche seulement dans le terminal 
"""

l_keys = []
cpt=0
while True:
    cpt+=1
    if msvcrt.kbhit():
        key = msvcrt.getch()
        l_keys.append(key)
        # print(f'Key pressed: {key}')
        if cpt > 2:
            cpt=0
            print(l_keys) 