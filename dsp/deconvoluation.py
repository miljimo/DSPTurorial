from matplotlib import pyplot as plt
from matplotlib import style
import mysignal as sigs
from scipy import signal
import numpy as np;
import csv
from sef_parsers import SEFParser;
import math;
        

if(__name__ =="__main__"):
    parser  = SEFParser();
    document  =  parser.Parse(filename = './monitorlog.sef');
    sig =  document.matrix[:, 3];
    filter_sig      =  sigs.Impulse_response;
    conv_result     =  signal.convolve(sig, filter_sig);
    deconv_result   =  signal.deconvolve(conv_result, filter_sig);
    fig , axes = plt.subplots(4, 1, sharex= True);
    axes[0].plot(sig);
    axes[1].plot(filter_sig);
    axes[2].plot(conv_result);
 
    axes[3].plot(deconv_result[0]);

    

    plt.show();
    
    pass;
            
            

