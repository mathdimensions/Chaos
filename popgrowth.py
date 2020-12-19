# created by David Skerritt
# this is a model for population growth based on Robert Mays logistic map
# from Chaos by Gleick. differential equations, chaos, mathematical biology
# an example of chaos in simple systems
# as r becomes > 3.5, chaos starts to emerge

import matplotlib
import matplotlib.pyplot as plt

def Malthusian_pop_growth(r, x): # model / function

    total = (r*x*(1 - x))        # r = rate of growth, x = population size
    return total



a, b = 2.7, .02     # rate of growth(a(r)) = 2.7, initial pop size(b(x)) = .02
i = 1

#plt.axis([0, 1, 0, 1])

for i in range(100):

    print(Malthusian_pop_growth(a, b))

    b = Malthusian_pop_growth(a, b)    # set b = previous population size
    i+=1

    plt.scatter(b, b)
    plt.pause(.01)


plt.grid()
plt.show()
