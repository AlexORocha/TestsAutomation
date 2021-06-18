# PARÂMETROS

# SLACK ----------------------------------
SLACK_TOKEN = 'xoxb-2154043457015-2185523088178-2v9ehpVsutJL4Dk0TQz4ytdL'
SLACK_URL_SERVICE = 'https://slack.com/api/chat.postMessage'

# PARÂMETROS GERAIS ----------------------
END = 'TCPIP::192.168.100.80::INSTR'  # ENDEREÇO DA CONEXÃO DO AGILENT 33220A

# ONDA 01 --------------------------------
WAVE1_NAME = 'CENTRAL DE AQUECIMENTO 2'
WAVE1_TIME_HIGH = 1.5 * 10**(-6) # s
WAVE1_TIME_LOW = 25.0 * 10**(-6) # s
WAVE1_PERIOD = 26.5 * 10**(-6) # s
WAVE1_BURSTS = 6
# ----------------------------------------

# ONDA 02 --------------------------------
WAVE2_NAME = 'CENTRAL DE AQUECIMENTO 3'
WAVE2_TIME_HIGH = 0.5 * 10**(-6) # s
WAVE2_TIME_LOW = 2 * 10**(-6) # s
WAVE2_PERIOD = WAVE2_TIME_HIGH + WAVE2_TIME_LOW # s
WAVE2_BURSTS = 2
# ----------------------------------------

# ONDA 03 --------------------------------
WAVE3_NAME = 'Acendedor de Fogão'
WAVE3_TIME_HIGH = 5.0 * 10**(-6) # s
WAVE3_TIME_LOW = 1.5 * 10**(-6) # s
WAVE3_PERIOD = WAVE3_TIME_HIGH + WAVE3_TIME_LOW # s
WAVE3_BURSTS = 20
# ----------------------------------------

# ONDA 04 --------------------------------
WAVE4_NAME = 'Lava Louças'
WAVE4_TIME_HIGH = 2.5 * 10**(-6) # s
WAVE4_TIME_LOW = 12.5 * 10**(-6) # s
WAVE4_PERIOD = WAVE4_TIME_HIGH + WAVE4_TIME_LOW # s
WAVE4_BURSTS = 10
# ----------------------------------------

# ONDA 05 --------------------------------
WAVE5_NAME = 'Lâmpadas Fluorescentes'
WAVE5_TIME_HIGH = 0.5 * 10**(-6) # s
WAVE5_TIME_LOW = 25.0 * 10**(-6) # s
WAVE5_PERIOD = WAVE5_TIME_HIGH + WAVE5_TIME_LOW # s
WAVE5_BURSTS = 2
# ----------------------------------------

# ONDA 06 --------------------------------
WAVE6_NAME = 'Tráfego 3A'
WAVE6_TIME_HIGH = 0.5 * 10**(-6) # s
WAVE6_TIME_LOW = 7.5 * 10**(-6) # s
WAVE6_PERIOD = WAVE6_TIME_HIGH + WAVE6_TIME_LOW # s
WAVE6_BURSTS = 2
# ----------------------------------------

# ONDA 07 --------------------------------
WAVE7_NAME = 'Tráfego 3B'
WAVE7_TIME_HIGH = 0.25 * 10**(-6) # s
WAVE7_TIME_LOW = 'N/A' # us
WAVE7_PERIOD = 1 * 10**(-6) # s
WAVE7_BURSTS = 1
# ----------------------------------------