# Link budget for downlink
# GEO satellite
import math
fc_ghz = float(input("Enter a carrier frequency in GHZ: "))
da_t = float(input("Enter a antenna diameter in Meter: "))
eff_t = float(input("Enter a transmitter efficiency: "))
pt_w = float(input("Enter a transmitted power in WATT: "))

# Satellite station
eff_r = float(input("Enter a receiver efficiency: "))
teta_3db = float(input("Enter a beamwidth (theta 3dB) in Degree: "))
d_km = float(input("Enter a link distance in KM: "))
d_m = d_km * 1000

# general equation
pt_dbw = 10 * math.log10(pt_w)
fc_hz = fc_ghz * (10 ** 9)
c = 299792458
landa = c / fc_hz

# Compute transmitter gain in dBi
gt = (10 * math.log10(eff_r * (70 * math.pi / teta_3db) ** 2))

# compute the effective isotropic radiated power
eirp = (pt_dbw + gt)

# power flux density
pfd = (eirp - (10 * math.log10(4 * math.pi * (d_m ** 2))))

# free space loss
lfs = (20 * math.log10(4 * math.pi * d_m / landa))

# compute the received gain
gr = (10 * math.log10(eff_t * (math.pi * da_t / landa) ** 2))

# compute the received power
pr = eirp + gr - lfs

print('The transmitter gain is:', gt, '[dBi]')

print('The Effective Isotropic Radiated Power (EIRP) is:', eirp, '[dBW]')

print('The power flux density is:', pfd, '[dBW/m^2]')

print('The free space loss is:', lfs, '[dBi]')

print('The received gain is:', gr, '[dBi]')

print('The received power is:', pr, '[dBW]')
