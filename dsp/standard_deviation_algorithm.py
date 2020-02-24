import mysignal as sigs;
from variance_algorithm import get_variance;

# Algorithm to compute the standard deviations of a signal.
def standard_deviation(values):
    return (get_variance(values)**0.5);

if __name__ =="__main__":    
    print(standard_deviation(sigs.InputSignal_1kHz_15kHz))
