from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np;


if __name__ == "__main__":
    x_axis  =  np.arange(1, 7)
    y_axis  =  [7,5,6,7,8,9]
    y_axis2  =  [3,5,6,7,8,9]
    style.use("dark_background");
    plt.plot(x_axis, y_axis , label = "displacement")
    plt.plot(x_axis, y_axis2 ,label = "velocity")
    plt.ylabel("Amplitude");
    plt.xlabel("Frequency");
    plt.legend()
    plt.show()
