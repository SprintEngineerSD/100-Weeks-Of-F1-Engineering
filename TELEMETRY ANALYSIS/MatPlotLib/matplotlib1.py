import matplotlib.pyplot as plt
import numpy as np
x =np.array([2023,2024,2025,2026])
y1 = np.array([15,25,30,20])
y2 = np.array([10,20,32,25])


plt.plot(x,y1, marker='.',markersize=10,markerfacecolor='red',markeredgecolor='black'
                    ,linestyle='solid',linewidth=2,color = 'black')
plt.title('Class size',fontsize=15,family = 'ariel',fontweight='bold')
plt.xlabel('Year',fontsize=15,family = 'ariel',fontweight='bold')
plt.ylabel('Class size',fontsize=15,family = 'ariel',fontweight='bold')
plt.tick_params(axis='both',colors = 'red')
plt.plot(x,y2)
plt.show()






