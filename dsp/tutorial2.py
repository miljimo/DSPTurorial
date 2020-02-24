from matplotlib import pyplot as plt
import numpy as np;
from matplotlib import style;
from mysignal import InputSignal_1kHz_15kHz




if __name__ =="__main__":
    style.use("ggplot");
    style.use("dark_background");
    figure , axes  =  plt.subplots(3,1, sharex = True);
    print(figure);
    print(axes);
    figure.suptitle("Signal Processing : multi-plots");
    axes[0].plot(InputSignal_1kHz_15kHz, color  = 'red');
    axes[0].set_title("Signal 1");
    axes[1].plot(InputSignal_1kHz_15kHz, color = 'green');
    axes[1].set_title("Signal 2");
    axes[2].plot(InputSignal_1kHz_15kHz , color  ='yellow');
    axes[2].set_title("Signal 3");

    plt.show();
