from matplotlib import pyplot as plt;
import numpy as np;
import mysignal as sigs;


response  =  np.arange(10) #sigs.InputSignal_1kHz_15kHz;


sin_signals  =  np.sin(response);
cos_signals  =  np.cos(response);

fig , axes  =  plt.subplots(2, 1, sharex= True);
fig.suptitle("Cos vr Sin wave");
axes[0].plot(sin_signals);
axes[0].set_title("Sin wave");
axes[1].plot(cos_signals);
axes[1].set_title("Cos wave");
plt.show();
