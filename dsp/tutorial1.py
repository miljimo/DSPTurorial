'''
  Test tutorial.
  sys.float_info.epsilon
'''
import sys
from matplotlib  import pyplot  #   plotting graph library
import numpy                    #   numberical computations
from scipy   import signal      #   Scientific compuatation and dsp processing library.




#main
if __name__ == "__main__":
    result  = numpy.arange(1, 20);
    window =  signal.hann(51)
    pyplot.plot(result)
    pyplot.plot(window)
    pyplot.show()
    
