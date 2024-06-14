import matplotlib.pyplot as plt
from matplotlib import rcParams
config = {
    "font.family":'Times New Roman',
    "axes.unicode_minus": False
    }
rcParams.update(config)
rcParams['font.size'] = 12
# 设置整体图像大小为正方形
import matplotlib.pyplot as plt
import numpy as np
data=np.load('test.npy')
real=data[:,0]
pred=data[:,1]
plt.figure(figsize=(8, 6))
time=np.arange(0,1e-8,1e-11)
plt.gcf().set_facecolor((255/255,244/255,242/255))
plt.plot(time[0:len(real)]*1e9,real,color='navy',linewidth=3,linestyle='-',label='IF-Circuit Simulation')
plt.plot(time[0:len(real)]*1e9,pred,color='red',linewidth=3,linestyle='--',label='IF-VerilogA Simulation')
plt.legend()
plt.xlabel('Time(ns)')  # 设置横坐标标签
plt.ylabel('Amplitude(V)')   # 设置纵坐标标签
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
# plt.vlines(np.arange(x_min, x_max, 0.1), y_min, y_max, colors='gray', linestyles='--', linewidth=1)
# plt.hlines(np.arange(y_min, y_max, (y_max-y_min)/5), x_min, x_max, colors='gray', linestyles='--', linewidth=1)

plt.show()


