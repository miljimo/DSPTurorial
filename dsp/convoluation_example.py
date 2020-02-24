from matplotlib import pyplot as plt
import mysignal as sigs
from matplotlib import style
from scipy import signal


style.use('ggplot')

f,axes =  plt.subplots(3, sharex=True);
f.suptitle("Convolution");

# plot the input signals
axes[0].plot(sigs.InputSignal_1kHz_15kHz, color='green');

#  plot the inpluse response signal
axes[1].plot(sigs.Impulse_response, color='yellow');

output_signals = signal.convolve(sigs.InputSignal_1kHz_15kHz,sigs.Impulse_response, mode='same')

#  plot the output signals
axes[2].plot(output_signals , color='red');


plt.show();
