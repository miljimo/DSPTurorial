from scipy import signal
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style




if __name__ == "__main__":
    t  = np.linspace(0,1.0, 2001);
    sig_5hz =np.sin(2 * np.pi * 5 * t)
    sig_250hz = np.sin(2 * np.pi * 250 * t)
    print(type(sig_5hz))
    fig, axes  =  plt.subplots(4,1, sharex = True);
    fig.suptitle("Random Signal Generations");

    print("5HZ frequence code ={0}".format(len(sig_5hz))); 
    axes[0].plot(sig_5hz );
    axes[1].plot(sig_250hz )
    axes[2].set_title("Addition signal")
    sign_5hz_plus_250hz  = sig_5hz + sig_250hz
    axes[2].plot(sign_5hz_plus_250hz)

    axes[3].set_title("Minus signal")
    sign_5hz_minus_250hz  =  sig_250hz -  sig_5hz
    axes[3].plot(sign_5hz_minus_250hz)

    plt.show();
    
    
