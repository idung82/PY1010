
E = 5000  # Elbil med årsforsikring
B = 7500  # Bensinbil med årsforsikring
KM = 100000  # km/år
TA = 8.38 * 365  # Trafikkforsikringsavgift per år
SP = 2  # 2kr/Kwh
DE = (0.2 * SP) * KM  # Drivstoffbruk elbil
DB = 1 * KM  # drivstoffbruk bensinbil
BE = 0.1 * KM  # Bomavgift elbil
BB = 0.3 * KM   # Bomavgift bensinbil
KE = E + TA + DE + BE  # Kostnad elbil
KB = B + TA + DB + BB  # Kostnad bensinbil

print(KE)
print(KB)
