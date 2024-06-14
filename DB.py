import numpy as np



def voltage_to_dBm(voltage_peak, impedance=50):
    # 计算功率（瓦特）
    power_watts = (voltage_peak ** 2) /  impedance
    # 将功率转换为dBm
    power_dBm = 10 * np.log10(power_watts / 1e-3)
    return power_dBm

# #
# # 示例峰值电压值（伏特）
# voltage_peak = 0.13
# dBm_value = voltage_peak_to_dBm(voltage_peak)
# print(f"峰值电压为: {voltage_peak} V, 对应的dBm值为: {dBm_value:.2f} dBm")

# # 基于分贝的混频器仿真搜集数据


import numpy as np

def dBm_to_voltage(dBm, impedance=50):
    # 将dBm转换为瓦特
    power_watts = 10 ** (dBm / 10) * 1e-3
    # 计算有效值电压
    voltage_rms = np.sqrt(power_watts * impedance)
    # 计算峰值电压
    voltage_peak = voltage_rms
    return voltage_peak



#
# # 示例dBm值
dBm_value = -5
# 计算峰值电压
voltage_peak = dBm_to_voltage(dBm_value)
print(f"dBm值为: {dBm_value} dBm, 对应的峰值电压为: {voltage_peak:.2f} V")
