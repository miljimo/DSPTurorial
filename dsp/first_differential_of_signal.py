from    matplotlib import pyplot as plt;
import  numpy as np;
from    scipy import signal
import mysignal as sigs;


if(__name__ == "__main__"):
    input_signals    =   sigs.InputSignal_1kHz_15kHz
    diff_signals     =   np.diff(input_signals);

    fig, axes =  plt.subplots(2, sharex= True);
    fig.suptitle("Differential of Signals");

    axes[0].plot(input_signals);
    axes[1].plot(diff_signals , color='red');

    plt.show();
