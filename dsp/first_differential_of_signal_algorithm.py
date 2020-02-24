import mysignal as sigs;
from matplotlib import pyplot as plt;
from convoluation_alogirthm import create_list;

def get_diff(input_response_signal):
    length  = len(input_response_signal);
    result_signals  = create_list(length, 0);

    for x in range(length):
        result_signals[x] = input_response_signal[x] - input_response_signal[x-1] # -i will return 0;
        
    return result_signals;

if(__name__ =="__main__"):
    fig, axes = plt.subplots(2, 1, sharex= True);
    fig.suptitle("Differential Algorithm");

    axes[0].plot(sigs.InputSignal_1kHz_15kHz);
    diff_signals  =  get_diff(sigs.InputSignal_1kHz_15kHz);
    axes[1].plot(diff_signals, color='red');

    plt.show();
