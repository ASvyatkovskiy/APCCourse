#$ begin import
from matplotlib.pylab import *
from numpy import *
#$ end

interactive(True)

np.random.seed(666)                  # make script deterministic

#$ begin make_sin
# make data
x = linspace(0, 9)
model = sin(x)
dy = random.uniform(0.75, 1, len(x))
y = model + random.normal(scale=dy)
#$ end

#$ begin plot_sin
# plot the data
plot(x, y, "b.", label="My data points")
errorbar(x, y, yerr=dy, fmt="none", color='b')
plot(x, model, "r:", label="Model")

# axis limits
xlim(-1, 10)

# labels
xlabel("x")
ylabel("y")
title("title")

# add a legend using the labels you gave to plot()
legend()
#$ end
