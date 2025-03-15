velocidade= 61
local_carro= 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_pass_radar_1 = local_carro >=(LOCAL_1 - RADAR_RANGE) and \
local_carro <=(LOCAL_1 + RADAR_RANGE)
carro_mult_radar_1 = vel_carro_pass_radar_1 and carro_pass_radar_1





if vel_carro_pass_radar_1:
    print('velocidade carro passou do radar 1')

if carro_pass_radar_1:
    print('carro passou no randar 1')

if carro_pass_radar_1:
    print('Carro multado em radar 1')

