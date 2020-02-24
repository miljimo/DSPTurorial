from matplotlib import pyplot as plt;
from convoluation_alogirthm import create_list;
import mysignal as sigs;



def get_running_sum(response_signal: list):
    length =  len(response_signal);
    result_signals  = create_list(length, 0);
    for x in range(length):
        sum_value  =  0;
        if((x - 1) >= 0 ):
            sum_value = result_signals[x -1];
        result_signals[x] =  sum_value + response_signal[x];
    
    return result_signals;


if(__name__ =="__main__"):
    results_signal  =  get_running_sum(sigs.InputSignal_1kHz_15kHz);
    fig, axes = plt.subplots(2,1, sharex=True);
    fig.suptitle("Running Signal Algorithm");
    axes[0].plot(sigs.InputSignal_1kHz_15kHz);
    axes[1].plot(results_signal)

    plt.show();
