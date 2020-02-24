from matplotlib import pyplot as plt
from matplotlib import style
import mysignal as sigs
import csv
import math;

def create_list(size, default_value= None):
    result  = list();
    if(type(size) != int):
        raise TypeError("Expecting size to be int value");
    for index in range(size):
        result.append(default_value);
    return result;

input_signals    =   sigs.InputSignal_1kHz_15kHz
inpulse_signals  =   sigs.Impulse_response


def period_func(signals, T = 0):
    results  = [0] * len(signals)

    for x in range(len(signals)):
        results[x] = math.sin(signals[x] + T)
    return results;



def get_convoluation(input_signal, inpulse_signal):    
   
    input_len   =   len(input_signal);
    inpluse_len =   len(inpulse_signal);
    result      =   create_list(input_len + inpluse_len, 0);

    for x in range(input_len):
        for y in range(inpluse_len):
            result[x+y] += float(input_signal[x] * inpulse_signal[y]);

    return result;


def book_get_convolution(response_signals, inpulse_signal):
    size    = len(response_signals) + len(inpulse_signal)-1 ;
    results = [0] * size;
     
    for k in range(len(response_signals)):
        for n in range(len(inpulse_signal)):
            results[n+k] +=  (response_signals[k] * inpulse_signal[n]);
    return results;
            
    
   


def write_to_csv(filename: str , response_signal:list) -> None:
    status = False;
    with open(filename, 'w+') as output_stream:
        writer  =  csv.writer(output_stream, lineterminator=",");
        for value in response_signal:
            writer.writerow([value]);
        status  = True;
    return status;
    
        

if(__name__ =="__main__"):
    CSV_FILENAME  = "convulution_signals.txt"
    style.use("dark_background");
    fig , axes  =  plt.subplots(4, 4, sharex=True);
    fig.suptitle("Convolution Algorithm");
    
    axes[0][0].set_title("Input Response Signals");
    axes[0][0].plot(input_signals);
    axes[1][0].set_title("Input Inpulse Signals");
    axes[1][0].plot(inpulse_signals);
    convolution_signals  = get_convoluation(input_signals, inpulse_signals);
    axes[2][0].set_title("Convolution");
    axes[2][0].plot(convolution_signals);
    """
    result  =  book_get_convolution(input_signals, inpulse_signals);
    axes[3].set_title("Textbook Convolution");
    axes[3].plot(result);
    write_to_csv(CSV_FILENAME, convolution_signals);
    """
    results  = period_func(input_signals, 4 * math.pi);
    axes[3][0].set_title("Period");
    axes[3][0].plot(results);
    plt.show();
            
            

