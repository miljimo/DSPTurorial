from scipy import signal
from matplotlib import pyplot as plt;
import numpy
import mysignal as sigs;


if (__name__ =="__main__"):
    inpulse  =  sigs.Impulse_response;
    corr_out_signal  =  signal.correlate(sigs.InputSignal_1kHz_15kHz, inpulse, mode="same");
    cov_out_signal   =  signal.convolve(sigs.InputSignal_1kHz_15kHz, inpulse, mode="same");

    fig , axes  =  plt.subplots(4, 1, sharex= True);
    fig.suptitle("Correlation vrs convolution");
    axes[0].plot(sigs.InputSignal_1kHz_15kHz);
    axes[0].set_title("Response Signal");
    axes[1].plot(inpulse);
    axes[1].set_title("Impulse Signal");
    
    axes[2].plot(corr_out_signal);
    axes[2].set_title("Correlation");
    axes[3].plot(cov_out_signal);
    axes[3].set_title("Convolution");
    plt.show();
    

