import matplotlib
print(matplotlib.__version__)
from matplotlib import pyplot

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500,2500,1053,500]

matplotlib.pyplot.plot(labels,values)
pyplot.show()