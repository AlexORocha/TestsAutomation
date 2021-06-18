from params import *


# DEFINICIÇÃO DA FORMA DE ONDA -----------------------------------------------
def getwaveparams(waveform):
    if waveform == 1:
        period = WAVE1_PERIOD
        frequency = 1/period
        width = WAVE1_TIME_HIGH
        duration = WAVE1_BURSTS * (WAVE1_TIME_HIGH + WAVE1_TIME_LOW)
    elif waveform == 2:
        period = WAVE2_PERIOD
        frequency = 1 / period
        width = WAVE2_TIME_HIGH
        duration = WAVE2_BURSTS * (WAVE2_TIME_HIGH + WAVE2_TIME_LOW)
    elif waveform == 3:
        period = WAVE3_PERIOD
        frequency = 1 / period
        width = WAVE3_TIME_HIGH
        duration = WAVE3_BURSTS * (WAVE3_TIME_HIGH + WAVE3_TIME_LOW)
    elif waveform == 4:
        period = WAVE4_PERIOD
        frequency = 1 / period
        width = WAVE4_TIME_HIGH
        duration = WAVE4_BURSTS * (WAVE4_TIME_HIGH + WAVE4_TIME_LOW)
    elif waveform == 5:
        period = WAVE5_PERIOD
        frequency = 1 / period
        width = WAVE5_TIME_HIGH
        duration = WAVE5_BURSTS * (WAVE5_TIME_HIGH + WAVE5_TIME_LOW)
    elif waveform == 6:
        period = WAVE6_PERIOD
        frequency = 1 / period
        width = WAVE6_TIME_HIGH
        duration = WAVE6_BURSTS * (WAVE6_TIME_HIGH + WAVE6_TIME_LOW)
    elif waveform == 7:
        period = WAVE7_PERIOD
        frequency = 1 / period
        width = WAVE7_TIME_HIGH
        duration = WAVE7_BURSTS * (WAVE7_TIME_HIGH)

    wave_info = {
        'period': period,
        'frequency': frequency,
        'width' : width,
        'duration': duration
    }

    return wave_info
# ----------------------------------------------------------------------------