from   matplotlib import pyplot as plt;
import mysignal as sigs;
import math;
from dft_algorithm import correlation_dft, get_magtitude_signals


def inverse_dft(real_signals :list, img_signals: list)->list:
    size            =  len(real_signals) + len(img_signals)
    length =  len(real_signals)
    domain_signals  =  [0] *size;

    for k in range(len(real_signals)):
        real_signals[k] =  real_signals[k] / length;
        img_signals[k]  =  img_signals[k] / length;
        
        for i in range(size):
            cos_value  = (2 * math.pi * k * i) / size;
            domain_signals[i] += real_signals[k] * math.cos(cos_value);
            domain_signals[i] += img_signals[k] * math.sin(cos_value);

    return domain_signals;



#
def plotter(response_signals:list):
    result  = correlation_dft(response_signals);
    fig,axes = plt.subplots(5,sharex= True);
    axes[0].set_title("Response Signal");
    axes[0].plot(response_signals);
    axes[1].set_title("DFT Frequence Domain Signal (Real Path)");
    axes[1].plot(result[0], color='red');
    axes[2].set_title("DFT Frequence Domain Signal (Imaginary Path)");
    axes[2].plot(result[1], color='green');
    imgs  =  get_magtitude_signals(result[0], result[1])
    axes[3].set_title("DFT Frequence Domain Signal (Magtitudes)");
    axes[3].plot(imgs, color='black');
    axes[4].set_title("Inverse DFT for Real and Imaginary Signals");
    inverse_signals  =  inverse_dft(result[0], result[1]);
    axes[4].plot(inverse_signals);
    plt.show();

if(__name__ =="__main__"):

    response_signals  = sigs.ecg_signal; #sigs.InputSignal_1kHz_15kHz
    plotter(response_signals)

   

   





