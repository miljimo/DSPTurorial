import mysignal as sigs;
from mean_algorithm import mean_algorithm  


def get_variance(values):
    result =  0;
    mean  = mean_algorithm(values);
    for value in values:
        result += (value - mean)**2
    return result / len(values);
        




if __name__ == "__main__":
    variance  = get_variance(sigs.InputSignal_1kHz_15kHz)
    print(variance);
    

