import numpy as np
from PySpice.Unit import *
from PySpice.Spice.Netlist import Circuit
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import math
import numpy as np
import pandas as pd


circuit = Circuit('IAM-81018 Gilbert Cell Mixer')
            # 定义直流偏置电路组件值
Rcm = np.arange(50, 450 + 50, 50)
Rtm = np.arange(20, 220 + 50, 50)
Rb1m = np.arange(10, 160 + 30, 30)
Rb2m = np.arange(10, 90 + 20, 20)
Ccm = np.arange(0.4, 1.2 + 0.2, 0.2)
Cbm = np.arange(0.4, 1.2 + 0.2, 0.2)

Rc = 50@u_Ω
Rt = Rtm[0]@u_Ω
Rb1 = Rb1m[0]@u_Ω
Rb2 = Rb2m[0]@u_Ω
Cc= Ccm[0]@u_uF
Cb= Cbm[0]@u_uF
Rr=50@u_Ω
            #添加组件到电路
circuit.R('R8', 'a', 'b', Rc)
circuit.R('R10', 'a', 'e', Rc)
circuit.R('R4', 'p', '0', Rt)
circuit.R('R5', 'q', '0', Rt)
circuit.R('R7', 'f', 'c', Rb1)
circuit.R('R9', 'f', 'c', Rb1)
circuit.R('R3', 'f', 'r', Rb1*0.5)
circuit.R('R1', 'i', 's', Rb2)
circuit.R('R2', 'i', 'l', Rb2)
circuit.R('R11', 'a', 't', 800@u_Ω)
circuit.R('R12', 'o', 't', 700@u_Ω)
circuit.R('R13', 'o', 'n', 500@u_Ω)
circuit.R('R14', 'u', '0', 200@u_Ω)
circuit.R('R15', 'h', '0', 1000@u_Ω)
circuit.R('R17', 'v', '0', 45@u_Ω)
circuit.R('R6', 'k', 'm', 20@u_Ω)
circuit.R('R18', 'w', 'x', Rr)
circuit.R('R19', 'y', 'z', Rr)
circuit.R('R20', 'ad', '0', Rr)
circuit.C('C1', 'z', 'ab', Cc)
circuit.C('C4', 'x', 'ac', Cc)
circuit.C('C5', 'g', 'aa', Cc)
circuit.C('C2', 'l', '0', Cb)
circuit.C('C3', 'r', '0', Cb)
circuit.L('L1', 'ab', 's', 0.5@u_nH)
circuit.L('L2', 'ac', 'c', 0.5@u_nH)
circuit.L('L3', 'aa', 'ad', 0.5@u_nH)
circuit.V('cc', 'a', '0', 5@u_V)

circuit.model('BJTM1', 'npn',
                        is_=1.07411147E-16, bf=1.30035647E+02, nf=1.03,
                        vaf=25, ikf=5.42499974E-03, ise=3.78086717E-13,
                        ne=2.00, br=5.12295082, nr=1.00, ikr=2.80000006E-02,
                        isc=1.16160000E-12, nc=2.00, rb=6.12458791E+01,
                        rbm=1.91785714E+01, re=3.57142857, rc=6.96232096E+01,
                         cje=9.67680017E-14, vje=8.49999987E-01,
                        mje=3.99999994E-01, cjc=6.05000011E-14, vjc=7.49999989E-01,
                        mjc=4.99999993E-01, xcjc=2.52561980E-01, cjs=8.68000015E-14,
                        vjs=6.99999990E-01, mjs=4.99999993E-01, fc=7.99999988E-01,
                        xtf=3.35472224E+00, tf=8.91292803E-12, itf=1.08500002E-02,
                        ptf=1.80E+01, tr=1.60000005E-09, kf=0.00, af=1.00,
                        eg=1.11, xtb=2.20, xti=8.00, tnom=25)
circuit.model('BJTM2', 'npn',
                        is_=2.1482293E-16, bf=1.30035647E+02, nf=1.03,
                        vaf=25, ikf=1.08500002E-02, ise=7.56173434E-13,
                        ne=2.00, br=5.12295082, nr=1.00, ikr=5.600000013E-02,
                        isc=2.00640001E-12, nc=2.00, rb=3.16646062E+01,
                        rbm=1.06309524E+01, re=1.78571429, rc=3.75704756E+01,
                         cje=1.93536003E-13, vje=8.49999987E-01,
                        mje=3.99999994E-01, cjc=1.04500002E-13, vjc=7.49999989E-01,
                        mjc=4.99999993E-01, xcjc=2.92440187E-01, cjs=1.09200002E-13,
                        vjs=6.99999990E-01, mjs=4.99999993E-01, fc=7.99999988E-01,
                        xtf=3.35472224E+00, tf=8.91292803E-12, itf=2.17000005E-02,
                        ptf=1.80E+01, tr=1.60000005E-09, kf=0.00, af=1.00,
                        eg=1.11, xtb=2.20, xti=8.00, tnom=25)
circuit.model('BJTM3', 'npn',
                        is_=2.04315924E-16, bf=1.66178934E+02, nf=1.03,
                        vaf=25, ikf=1.16250003E-02, ise=6.09123888E-13,
                        ne=2.00, br=5.12295082, nr=1.00, ikr=6.00000013E-02,
                        isc=2.31840001E-12, nc=2.00, rb=1.17166379E+02,
                        rbm=2.70221484E+01, re=1.66666667, rc=3.58072512E+01,
                         cje=1.56160003E-13, vje=8.49999987E-01,
                        mje=3.99999994E-01, cjc=1.20750002E-13, vjc=7.49999989E-01,
                        mjc=4.99999993E-01, xcjc=1.95445132E-01, cjs=1.18900002E-13,
                        vjs=6.99999990E-01, mjs=4.99999993E-01, fc=7.99999988E-01,
                        xtf=3.16117215E+00, tf=7.97477712E-12, itf=2.32500005E-02,
                        ptf=1.80E+01, eg=1.11, tr=1.60000005E-09, xtb=2.20,
                        kf=0.00, xti=8.00, af=1.00, tnom=25)
circuit.model('BJTM4', 'npn',
                        is_=4.29644587E-16, bf=1.30035647E+02, nf=1.03,
                        vaf=2.50E+01, ikf=2.17000005E-02, ise=1.51234685E-12,
                        ne=2.00, br=5.12295082, nr=1.00, ikr=1.11999998E-01,
                        isc=3.69600001E-12, nc=2.00, rb=1.61795253E+01,
                        rbm=5.66269841E+00, re=8.92857130E-01, rc=2.27441087E+01,
                       cje=3.87072007E-13, vje=8.49999987E-01,
                        mje=3.99999994E-01, cjc=1.92500003E-13, vjc=7.49999989E-01,
                        mjc=4.99999993E-01, xcjc=3.17506489E-01, cjs=1.54000003E-13,
                        vjs=6.99999990E-01, mjs=4.99999993E-01, fc=7.99999988E-01,
                        xtf=3.35472224E+00, tf=8.91292803E-12, itf=4.34000010E-02,
                        ptf=1.80E+01, eg=1.11, tr=1.60000005E-09, xtb=2.20,
                        kf=0.00, xti=8.00, af=1.00,tnom=25)
circuit.model('BJTM5', 'npn',
                        is_=4.08631847E-16, bf=1.66178934E+02, nf=1.03,
                        vaf=2.50E+01, ikf=2.32500005E-02, ise=1.21824776E-12,
                        ne=2.00, br=5.12295082, nr=1.00, ikr=1.199999998E-01,
                        isc=4.08480002E-12, nc=2.00, rb=5.91784277E+01,
                        rbm=1.41063123E+01, re=8.33333321E-01, rc=2.20144369E+01,
                        cje=3.12320005E-13, vje=8.49999987E-01,
                        mje=3.99999994E-01, cjc=2.12750004E-13, vjc=7.49999989E-01,
                        mjc=4.99999993E-01, xcjc=2.21856636E-01, cjs=1.65300003E-13,
                        vjs=6.99999990E-01, mjs=4.99999993E-01, fc=7.99999988E-01,
                        xtf=3.16117215E+00, tf=7.97477712E-12, itf=4.65000010E-02,
                        ptf=1.80E+01, tr=1.60000005E-09, kf=0.00E+00, af=1.00,
                        tnom=25, eg=1.11, xtb=2.20, xti=8.00)
circuit.BJT('BJT1','m', 'h', 'q',  model="BJTM3")
circuit.BJT('BJT2','k', 'h', 'p',  model="BJTM3")
circuit.BJT('BJT3','d', 's', 'k',  model="BJTM2")
circuit.BJT('BJT4','j', 'l', 'm',  model="BJTM2")
circuit.BJT('BJT5', 'e','r', 'd',  model="BJTM1")
circuit.BJT('BJT7','b', 'c', 'd',  model="BJTM1")
circuit.BJT('BJT6', 'b','r', 'j',  model="BJTM1")
circuit.BJT('BJT8','e', 'c', 'j',  model="BJTM1")
circuit.BJT('BJT9', 'a','f', 'g',  model="BJTM4")
circuit.BJT('BJT10','a', 't', 'f',  model="BJTM3")
circuit.BJT('BJT11','f', 'o', 'i',  model="BJTM3")
circuit.BJT('BJT12', 'i','n', 'h',  model="BJTM3")
circuit.BJT('BJT13','n', 'h', 'u',  model="BJTM3")
circuit.BJT('BJT14', 'g', 'h', 'v', model="BJTM5")

# circuit.SinusoidalVoltageSource('input_RF', 'y', '0', amplitude=0.2@u_V, frequency=1.75@u_GHz)
# circuit.SinusoidalVoltageSource('input_LO', 'w', '0', amplitude=0.44@u_V, frequency=1.75@u_GHz)
#
#             # 运行瞬态分析
# simulator = circuit.simulator(temperature=25, nominal_temperature=25)
# analysis = simulator.transient(step_time=0.0005@u_ns, end_time=0.001@u_us)
# print(np.array(analysis['y']))
from DB import dBm_to_voltage,voltage_to_dBm
fm_RF = np.linspace(1, 20, 20)
# amprf=np.linspace(0.0001,0.002,20)
EMS=np.linspace(0.01,0.1,10)


RF=[]
LO=[]
IF=[]
Fre=[]
Amp=[]


ac_line1 = circuit.AcLine('input_RF', 'y', circuit.gnd, rms_voltage=dBm_to_voltage(0) @ u_V, frequency=3@ u_GHz)
# circuit.SinusoidalVoltageSource('input_LO', 'LO_PORT', circuit.gnd, amplitude=0.003 @ u_V, frequency=855 @ u_MHz)
ac_line2 = circuit.AcLine('input_LO', 'w', circuit.gnd, rms_voltage=dBm_to_voltage(-5) @ u_V, frequency=1.75@ u_GHz)

simulator = circuit.simulator(temperature=25, nominal_temperature=25, method='gear')
analysis = simulator.transient(step_time=0.001 @ u_ns, end_time=ac_line2.period * 10)
print(np.array(analysis['y']))
print(np.array(analysis['w']))
print(np.array(analysis['ad']))

plt.subplot(3, 1, 1)  # 3行1列，第1个子图
plt.plot(analysis.time, analysis['y'])
plt.title('RF_PORT Signal(Input)')

# 绘制 LO_PORT 信号
plt.subplot(3, 1, 2)  # 3行1列，第2个子图
plt.plot(analysis.time, analysis['w'])
plt.title('LO_PORT Signal(Input)')


# 绘制 IF_PORT 信号
plt.subplot(3, 1, 3)  # 3行1列，第3个子图
plt.plot(analysis.time, analysis['ad'])
plt.title('IF_PORT Signal(Output)')

# 调整子图间距
plt.tight_layout()


# 显示图像
plt.show()
