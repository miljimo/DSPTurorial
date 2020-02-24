import mysignal as sigs;


"""
  Writing your mean algorithm.
"""

def mean_algorithm(values):
    number_samples  =  len(values);
    sum_of_values  = 0;
    for value in values:
        sum_of_values += value;

    return (sum_of_values / number_samples)

if __name__=="__main__":
    print(mean_alogirthm(sigs.InputSignal_1kHz_15kHz))
