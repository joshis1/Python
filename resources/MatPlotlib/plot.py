''' 

____  _
/ ___|| |__  _ __ ___ _   _  __ _ ___
\___ \| '_ \| '__/ _ \ | | |/ _` / __|
 ___) | | | | | |  __/ |_| | (_| \__ \
|____/|_| |_|_|  \___|\__, |\__,_|___/
                      |___/
'''


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import ticker


# list - ideally should be dictionary - Total ticks, Time in seconds, Iterations/sec, Iterations
ppc = {'Total Ticks': 12444, 'Time in Seconds' :  12.444000, 'Iterations/sec': 883.960141,'Iterations': 11000}
zynq = {'Total Ticks':13576, 'Time in Seconds' :  13.576000, 'Iterations/sec': 2209.781968,'Iterations': 30000}
zynqmp = {'Total Ticks': 15618, 'Time in Seconds' : 15.618000, 'Iterations/sec': 3841.721091, 'Iterations': 60000}
ppc_parameters = list(ppc.values())
zynq_parameters = list(zynq.values())
zyqmp_parameters = list(zynqmp.values())

base_total_ticks = ppc['Total Ticks']
base_time_in_seconds=ppc['Time in Seconds']
base_iterations_per_sec=ppc['Iterations/sec']
base_iterations=ppc['Iterations']

print(base_total_ticks)
base_values = [base_total_ticks,base_time_in_seconds,base_iterations_per_sec, base_iterations]

for i in range(0,4):
    ppc_parameters[i] = (ppc_parameters[i]/base_values[i])
    zynq_parameters[i] = (zynq_parameters[i]/base_values[i])
    zyqmp_parameters[i] =  (zyqmp_parameters[i]/base_values[i])
    
print('ppc parameters')
print(ppc_parameters) 

print('zynq parameters')
print(zynq_parameters)

print('zynqmp_parameters')
print(zyqmp_parameters)
#ppc_parameters= [12444,12.444000,883.960141,11000]
#zynq_parameters=[13576,13.576000,2209.781968,30000]
#zynqmp_parameters=[13576,13.576000,2209.781968,30000]

data = [ ppc_parameters, zynq_parameters, zyqmp_parameters] 
print(data)
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_xticks(np.linspace(0.25,3.25,4))
labels = ['Total_Ticks', 'Time_in_secs', 'Iterations/sec', 'Iterations']
ax.bar(X + 0.00, data[0], color = 'r', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'y', width = 0.25)
ax.bar(X + 0.50, data[2], color = 'g', width = 0.25)
# save the figure
ax.legend(labels=['ppc', 'zynq','zynqmp'])
ax.set_xticklabels(labels)
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
