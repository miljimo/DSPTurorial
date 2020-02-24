import mysignal as sigs;
from matplotlib import pyplot as plt;
from convoluation_alogirthm import create_list;
import math;

import sys;

EPISON  = sys.float_info.epsilon;

# f(x)  =  4x - 4


def f_4x_minus_4(response_signal:list):
    length   =  len(response_signal);
    results  =  create_list(length)
    
    for x in  range(length):
        results[x]  =  (4 * response_signal[x]) * 0.4;

    return results;

def min_value(response_signals: list):
    
    value  = response_signals[0];

    for v in response_signals:
        if( v < value):
            value  =  v;

    return value;


def max_value(response_signals: list):
    
    value  = response_signals[0];

    for v in response_signals:
        if(v > value):
            value  =  v;

    return value;

def alg_summation(signals):
    result  = 0;
    for value in signals:
        result += value;

    return result;

def arithematic_mean(response_signal):
    result  = 0;
    length =  len(response_signal);
    summation  = 0;
    for value in response_signal:
        summation += value;
    result  =  (summation / length);  
    return result;


def deviation(response_signals):
    length          = len(response_signals);
    results         = create_list(length, 0);
    mean_value      = arithematic_mean(response_signals)  

    for x in range(length):
        results[x]  = response_signals[x] - mean_value;

    return results;


def range_signal(response_signals: list):
    min_val  =  min_value(response_signals)
    max_val  =  max_value(response_signals);

    return (max_val  - min_val)


def standard_deviation(signals):
    mean    =  arithematic_mean(signals)
    result  = 0;
    
    for value in signals:
        result +=((value - mean)**2)

    return math.sqrt( (result/len(signals)))
    

def root_mean_square(response_signals: list):
    summation = 0;
    length  =  len(response_signals);
    
    for value in response_signals:
        summation += (value **2);
    return  math.sqrt((summation/ length));        

def moments(r_value , signals):
    mean    = arithematic_mean(signals)
    length  = len(signals)
    summation = 0;
    for value in signals:
        summation += (value - mean)** r_value
    return (summation/length)


def 

if(__name__ =="__main__"):
        
    input_signals    = sigs.InputSignal_1kHz_15kHz
    diff_signals     =   f_4x_minus_4(input_signals);
    print(range_signal(input_signals));
    print(str(range_signal(diff_signals)));
    fig, axes =  plt.subplots(3, sharex= True);
    fig.suptitle("Function of Signals");

    axes[0].plot(input_signals);
    axes[1].plot(diff_signals , color='red');

    deviation_signal = deviation(input_signals);
    summation =  alg_summation(deviation_signal);
    print(summation)
    axes[2].set_title("Deviation Of x from its mean");
    axes[2].plot(deviation_signal);
    print("Epison  ={0}".format(EPISON));

    data  = input_signals#[12,6,7,3,15,10,18,5]
    print("R.M.S ={0}".format(root_mean_square(data)))

    mean_deviation = arithematic_mean(deviation(data))
    mean  =  arithematic_mean(data);
    print("mean deviation ={0} , mean ={1}".format(mean_deviation,mean ))
    print("standard deviation ={0} , mean_deviation ={1}".format(standard_deviation(data), mean_deviation))
    print("Moment  = {0}".format(moments(2,data )))
    plt.show();
    
