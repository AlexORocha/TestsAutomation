# IMPORT DAS BIBLIOTECAS / MÓDULOS -------------------------------------------
import time

import pyvisa  # BIBLIOTECA PYVISA PARA CONTROLE GPIB
import time

from utils.slack import Slack
from utils.waveform import getwaveparams
from params import END
# ----------------------------------------------------------------------------


# DEFINIÇÕES DO SLACK --------------------------------------------------------
slack = Slack(
                robot_name="Marvin", robot_icon=":robot_face:",
                channel_log='#dev_log', channel_error='#dev_log'
            )
# ----------------------------------------------------------------------------


def run():
    # INICIALIZAÇÃO DO SETUP -----------------------------------------------------
    try:
        rm = pyvisa.ResourceManager()  # INICIA A INSTÂNCIA RM DO PYVISA
        Agilent = rm.open_resource(END)

        if str(rm.last_status) == 'StatusCode.success':
            slack.send_success_message(f'O Agilent foi conectado com sucesso no endereço: {END}\nrm: {str(rm.last_status)}')
        else:
            slack.send_fail_message(f'Não foi possível realizar a comunicação com o Agilent no endereço: {str(rm.last_status)}')
            exit(1)
    except Exception as Error:
        slack.send_fail_message(f'Não foi possível realizar a comunicação com o Agilent.\nErro: {Error}')
        exit(1)
        # ---------------------------------------------------------------------------

    WAVE = 7 # DEBBUGER ESTA INFORMAÇÃO VIRÁ DO FRONT

    # CAPTURAR INFORMAÇÕES DA ONDA -----------------------------------------------
    try:
        wave_info = getwaveparams(WAVE)
        period = wave_info['period']
        frequency = wave_info['frequency']
        width = wave_info['width']
        duration = wave_info['duration']

        slack.send_success_message(f'Parâmetros da Onda {WAVE} capturados com sucesso!\n'
                                   f'Período: {period}\n'
                                   f'Frequência: {frequency}\n'
                                   f'Duração do Pulso: {width}%\n'
                                   f'Duração: {duration}')
    except Exception as Error:
        slack.send_fail_message(f'Não foi possível capturar as informações da onda.\nErro: {Error}')
        exit(1)
    # ----------------------------------------------------------------------------


    # DEFINIÇÕES NO AGILENT ------------------------------------------------------
    try:
        Agilent.clear()  # RESSETANDO O AGILENT PARA O PADRÃO

        Agilent.write('OUTP OFF') # DESLIGA O OUTPUT
        Agilent.write('FUNC PULS')  # FUNÇÃO PULSE
        Agilent.write(f'FUNC:PULS:WIDT {str(width)}')
        Agilent.write('FREQ ' + str(int(frequency)))  # SET DA FREQUÊNCIA
        Agilent.write('VOLT 2.5') # TENSÃO DE 5V
        Agilent.write('VOLT:OFFS 0') # OFFSET DE 0 V

        slack.send_success_message(f'Estado do Agilent para a forma de onda N{WAVE} definido com sucesso!')
    except Exception as Error:
        slack.send_fail_message(f'Não foi possível definir o estado do Agilent.\nErro: {Error}')
        exit(1)

    # ----------------------------------------------------------------------------
    try:
        # ATIVAR E DESATIVAR O TRIGGER DO TAZ ----------------------------------------
        Agilent.write('OUTP ON')  # LIGA O OUTPUT
        time.sleep(duration)
        Agilent.write('OUTP OFF')  # DESLIGA O OUTPUT
        # ----------------------------------------------------------------------------

        slack.send_success_message(f'Teste realizado com sucesso!')
    except Exception as Error:
        slack.send_fail_message(f'Não foi possível realizar o teste.\nErro: {Error}')
        exit(1)