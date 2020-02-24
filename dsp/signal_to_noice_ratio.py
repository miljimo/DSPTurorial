import mysignal as sigs;
from mean_algorithm import mean_algorithm  
from standard_deviation_algorithm import standard_deviation

# SNR = signal to noice ratio

def signal_to_noise_ratio(values):
   return (mean_algorithm(values)/standard_deviation(values))  * 100;


if __name__ =="__main__":
    print(signal_to_noise_ratio(sigs.InputSignal_1kHz_15kHz))

