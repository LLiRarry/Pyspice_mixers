import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
with open('minxer_data.json', 'r') as f:
    data = json.load(f)

RF = data['RF']
LO = data['LO']
IF = data['IF']
Time=data['Time']
Fre=data['Fre']
Amp=data['Amp']

Time[0]=Time[0][50:len(RF[0])]
for i in range(len(Time[0])):
    Time[0][i]=Time[0][i]-Time[0][0]
time=np.arange(0,1e-8,1e-11)
index=3
print(Fre[index],Amp[index])
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

plt.figure(figsize=(7, 7))
plt.gcf().set_facecolor((255/255,244/255,242/255))
# 绘制 RF 信号
plt.subplot(3, 1, 1)  # 3行1列，第1个子图
plt.plot(time[0:len(RF[index])]*1e9, RF[index],color='navy')
plt.title('RF   1GHz   -30dBm')
plt.xlabel('Time(ns)')  # 设置横坐标标签
plt.ylabel('Amplitude(V)')   # 设置纵坐标标签

# 绘制密集的虚线网格
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
plt.vlines(np.arange(x_min, x_max, 0.1), y_min, y_max, colors='gray', linestyles='--', linewidth=1)
plt.hlines(np.arange(y_min, y_max, (y_max-y_min)/5), x_min, x_max, colors='gray', linestyles='--', linewidth=1)

# 绘制 LO_PORT 信号
plt.subplot(3, 1, 2)  # 3行1列，第2个子图
plt.plot(time[0:len(LO[index])]*1e9, LO[index],color='darkorange')
plt.title('LO   1.75GHz   -5dBm')
plt.xlabel('Time(ns)')
plt.ylabel('Amplitude(V)')

# 绘制密集的虚线网格
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
plt.vlines(np.arange(x_min, x_max, 0.1), y_min, y_max, colors='gray', linestyles='--', linewidth=1)
plt.hlines(np.arange(y_min, y_max, (y_max-y_min)/5), x_min, x_max, colors='gray', linestyles='--', linewidth=1)

# 绘制 IF 信号
plt.subplot(3, 1, 3)  # 3行1列，第3个子图
plt.plot(time[0:len(IF[index])]*1e9, IF[index],color='brown')
plt.title('IF')
plt.xlabel('Time(ns)')
plt.ylabel('Amplitude(V)')

# 绘制密集的虚线网格
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
plt.vlines(np.arange(x_min, x_max, 0.1), y_min, y_max, colors='gray', linestyles='--', linewidth=1)
plt.hlines(np.arange(y_min, y_max, (y_max-y_min)/5), x_min, x_max, colors='gray', linestyles='--', linewidth=1)

# 调整子图间距
plt.tight_layout()

# 显示图像
plt.show()

# plt.figure(figsize=(7, 7))
#
# # 绘制 RF 信号
# plt.subplot(3, 1, 1)  # 3行1列，第1个子图
# plt.plot(time[0:len(RF[index])]*1e9, RF[index])
# plt.title('RF')
# plt.xlabel('Time(ns)')  # 设置横坐标标签
# plt.ylabel('Amplitude(V)')   # 设置纵坐标标签
# plt.grid(True, linestyle='--', linewidth=1)  # 添加密集的虚线网格
#
#
# # 绘制 LO_PORT 信号
# plt.subplot(3, 1, 2)  # 3行1列，第2个子图
# plt.plot(time[0:len(LO[index])]*1e9, LO[index])
# plt.title('LO')
# plt.xlabel('Time(ns)')
# plt.ylabel('Amplitude(V)')
# plt.grid(True, linestyle='--', linewidth=0.5)  # 添加密集的虚线网格
#
# # 绘制 IF 信号
# plt.subplot(3, 1, 3)  # 3行1列，第3个子图
# plt.plot(time[0:len(IF[index])]*1e9, IF[index])
# plt.title('IF')
# plt.xlabel('Time(ns)')
# plt.ylabel('Amplitude(V)')
# plt.grid(True, linestyle='--', linewidth=0.5)  # 添加密集的虚线网格
#
# # 调整子图间距
# plt.tight_layout()
#
# # 显示图像
# plt.show()
