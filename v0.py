import json

import numpy as np
from PySpice.Unit import *
from PySpice.Spice.Netlist import Circuit
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import math
import pandas as pd

# ac_line = circuit.AcLine('ac_source', 'g2', circuit.gnd, rms_voltage=1.6 @ u_V, frequency=5 @ u_GHz)
# circuit.SinusoidalVoltageSource('input_RF', 'RF_PORT', circuit.gnd, amplitude=0.0001 @ u_V, frequency=5 @ u_GHz)

RF = []
LO = []
IF = []
Fre = []
Amp = []
Time = []
RF_=[]

Fre_list = np.linspace(1, 10, 20)
Rf_dbm_list = [-15, -20, -25, -30, -35, -40, -45, -50]
from DB import dBm_to_voltage, voltage_to_dBm

for fre in Fre_list:
    for rf_dbm in Rf_dbm_list:
        circuit = Circuit('Low-power Single Transistor Active Mixer')
        RL = 4700 @ u_Ω
        CLO = 0.5 @ u_pF
        CRF = 1.8 @ u_pF
        RC = 0.47 @ u_kΩ
        RB = 8.2 @ u_kΩ
        LRF = 6.6 @ u_nH
        LIF = 270 @ u_nH
        CP_IF = 33 @ u_pF
        CS_IF = 13.3 @ u_pF

        CDC_RF = 2.2e-10 @ u_uF  # 左
        CDC_IF = 1.3e-10 @ u_uF

        RLO = 50 @ u_Ω
        RRF = 50 @ u_Ω
        RRS_IF = 50 @ u_Ω
        circuit.R('L', 'collector', 'B', RL)
        circuit.C('LO', 'LO_PORT_', 'base', CLO)
        circuit.R('LO', 'LO_PORT', 'LO_PORT_', RLO)
        circuit.C('RF', 'RF_PORT_', 'base', CRF)
        circuit.R('RF', 'RF_PORT', 'RF_PORT_', RRF)
        circuit.R('C', 'B', 'C', RC)
        circuit.R('B', 'A', 'B', RB)
        circuit.L('RF', 'A', 'base', LRF)
        circuit.L('IF', 'collector', 'B', LIF)
        circuit.C('P_IF', 'collector', '0', CP_IF)
        circuit.C('S_IF', 'collector', 'IF_PORT', CS_IF)
        circuit.R('RS_IF', '0', 'IF_PORT', RRS_IF)  # 这是输出波形，负载电压50欧不知道有什么影响
        circuit.C('DC_RF', 'A', '0', CDC_RF)  # 左
        circuit.C('DC_IF', 'B', '0', CDC_IF)
        circuit.V('cc', 'C', '0', 1 @ u_V)
        # 添加 NPN BJT
        circuit.BJT('Q', 'collector', 'base', '0', model="MMBR941")
        circuit.model("MMBR941", "NPN",
                      IS=1e-14,
                      BF=100,
                      NF=1,
                      VAF=20,
                      CJE=0.35e-12,
                      CJC=0.35e-12,
                      TF=1 / 8e9,
                      VJE=0.65,
                      VJC=0.7,
                      MJE=0.33,
                      MJC=0.33,
                      XCjc=0.33,
                      IKF=0.01,
                      TR=10e-9,
                      Cjc=2e-12)

        ac_line1 = circuit.AcLine('input_RF', 'RF_PORT', circuit.gnd, rms_voltage=dBm_to_voltage(rf_dbm) @ u_V,
                                  frequency=fre @ u_GHz)
        ac_line2 = circuit.AcLine('input_LO', 'LO_PORT', circuit.gnd, rms_voltage=dBm_to_voltage(-5) @ u_V,
                                  frequency=1.75 @ u_GHz)
        simulator = circuit.simulator(temperature=25, nominal_temperature=25, method='gear')
        analysis = simulator.transient(step_time=0.01 @ u_ns, end_time=ac_line2.period * 7)
        RF.append(np.array(analysis['RF_PORT']).flatten().tolist()[100:])
        LO.append(np.array(analysis['LO_PORT']).flatten().tolist()[100:])
        IF.append(np.array(analysis['IF_PORT']).flatten().tolist()[100:])
        RF_.append(np.array(analysis['RF_PORT_']).flatten().tolist()[100:])
        Fre.append(fre)
        Amp.append(rf_dbm)
        Time.append(np.array(analysis.time).flatten().tolist())

# save json
data = {'RF': RF, 'LO': LO, 'IF': IF, 'Fre': Fre, 'Amp': Amp, 'Time': Time, 'RF_': RF_}
with open('minxer_data_gain.json', 'w') as f:
    json.dump(data, f)

    # plt.subplot(3, 1, 1)  # 3行1列，第1个子图
    # plt.plot(analysis['RF_PORT'])
    # plt.title('RF_PORT Signal(Input)')
    #
    # # 绘制 LO_PORT 信号
    # plt.subplot(3, 1, 2)  # 3行1列，第2个子图
    # plt.plot(analysis['LO_PORT'])
    # plt.title('LO_PORT Signal(Input)')
    #
    # plt.subplot(3, 1, 3)  # 3行1列，第3个子图
    # plt.plot((-1) * np.array(analysis['IF_PORT']))
    # plt.title('IF_PORT Signal(Output)')
    #
    # # 调整子图间距
    # plt.tight_layout()
    #
    # # 显示图像
    # plt.show()

#
# print(np.array(analysis['RF_PORT']))
# print(np.array(analysis['LO_PORT']))
# print(np.array(analysis['IF_PORT']))


# 画出三个波形
# plt.plot(analysis['RF_PORT'])
# plt.plot(analysis['LO_PORT'])
# plt.plot(analysis['IF_PORT'])
# plt.show()

# it can generate the baseic answer for the next moudel design
# # Define the circuit
# RF_input_power_avg = abs(np.mean((analysis['RF_PORT']-analysis['RF_PORT_'])/50*analysis['RF_PORT_']) * 1e8)
# IF_output_power_avg = abs(np.mean((analysis['IF_PORT']**2)/50) * 1e8)
# RF_input_power_avg_log=10*math.log10(RF_input_power_avg)
# IF_output_power_avg_log=10*math.log10(IF_output_power_avg)
# G=IF_output_power_avg_log-RF_input_power_avg_log
# print(G)

# def align_signals(signal1, signal2):
#     # 计算互相关
#     correlation = np.correlate(signal1, signal2, mode='full')
#     # 找到互相关的最大值对应的延迟
#     delay = np.argmax(correlation) - len(signal1) + 1
#     # 根据延迟调整信号
#     if delay > 0:
#         aligned_signal1 = np.pad(signal1, (delay, 0), 'constant', constant_values=(0, 0))[:len(signal1)]
#         aligned_signal2 = signal2
#     else:
#         aligned_signal1 = signal1
#         aligned_signal2 = np.pad(signal2, (-delay, 0), 'constant', constant_values=(0, 0))[:len(signal2)]
#     return aligned_signal1, aligned_signal2
# 假设 analysis 是你的仿真结果
# 绘制 RF_PORT 信号
