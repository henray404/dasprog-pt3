U = int(input())
K = int(input())
M = int(input())

atkM = M // 2 * 2
atkK = K // 2 * 5
atkD = 100
healthM = 100/100
healthK = 500/100

healthD = 1000/100

total_dmg = (atkM * healthM) + (atkK * healthK) + (atkD * healthD)
ucup_health = U - total_dmg

if ucup_health > 0:
    print(f"Yey! Ucup Menang! HP tersisa: {round(ucup_health)}")
else:
    print('Yah! Ucup Meninggoy.')
