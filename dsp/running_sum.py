import numpy as np;
import mysignal as sigs;
from matplotlib import pyplot as plt;
from matplotlib import style;
from scipy import signal


if(__name__ =="__main__"):
    style.use("ggplot");
    style.use("dark_background");
    fig , axes = plt.subplots(2, 1, sharex= True);
    fig.suptitle("Running Sum");
    axes[0].set_title("Input Signal Response");
    axes[0].plot(sigs.InputSignal_1kHz_15kHz);
    cum_sum_signals  =  np.cumsum(sigs.InputSignal_1kHz_15kHz);
    axes[1].set_title("Running Sum Signals");
    axes[1].plot(cum_sum_signals , color ='red');

    plt.show();
    
