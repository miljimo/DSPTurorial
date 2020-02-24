from   matplotlib import pyplot as plt;
import mysignal as sigs;
import math;
from sef_parsers  import SEFParser;

def correlation_dft(signals: list) ->list:
    size =  len(signals);
    k_length       = int(size/2);
    signals_img     =  [0]* k_length
    signals_real    =  [0]* k_length

    # calculation of the signal_real
    for k in range(k_length):
        for i in range(size):
           cos_value  = (2 * math.pi * k * i) / size;
           signals_real[k] +=  signals[i] * math.cos(cos_value);
           signals_img[k]  +=  signals[i] * math.sin(cos_value);
    return [signals_real, signals_img]


def get_magtitude_signals(reals_signals: list, img_signals:list):
    if(len(reals_signals) != len(img_signals)):
        raise TypeError("Expecting both imaginary list and reals");

    size                =  len(reals_signals)
    matitude_signals    =  [0] * size;
    for x in range(size):
       matitude_signals[x] = math.sqrt( (reals_signals[x]**2) + (img_signals[x]**2))
    return matitude_signals;



if(__name__ =="__main__"):

    parser  =  SEFParser();
    doc = parser.Parse(filename = './monitorlog.sef');
    
    response_signal1 = doc.matrix[:,0] #sigs.InputSignal_1kHz_15kHz
    print(len(response_signal1))
    fig,axes = plt.subplots(4,sharex= True);
    print("Fingure configured");
    result  = correlation_dft(response_signal1);
    print("DFT calculated");
    axes[0].set_title("Response Signal");
    axes[0].plot(response_signal1);
    print("Ploted DFT respond signal");
    axes[1].set_title("DFT Frequence Domain Signal (Real Path)");
    axes[1].plot(result[0], color='red');
    axes[2].set_title("DFT Frequence Domain Signal (Imaginary Path)");
    axes[2].plot(result[1], color='green');
    imgs  =  get_magtitude_signals(result[0], result[1])
    axes[3].set_title("DFT Frequence Domain Signal (Magtitudes)");
    axes[3].plot(imgs, color='black');

    plt.show();





