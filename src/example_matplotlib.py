#$ begin import
import matplotlib.pyplot as plt
import numpy as np
#$ end

try:
    pause
except NameError:
    pause = False
    plt.interactive(True)

np.random.seed(666)                  # make script deterministic

#$ begin make_sin
# make data
x = np.linspace(0.0, 9.0, 19)
model = np.sin(x)
dy = np.random.uniform(0.75, 1, len(x))
y = model + np.random.normal(scale=dy)
#$ end

#$ begin plot_sin
# plot the data
plt.plot(x, y, "b.", label="My data points")
plt.errorbar(x, y, xerr=None, yerr=dy, fmt=None, color='b')
plt.plot(x, model, "r:", label="Model")

# axis limits
plt.xlim(-1, 10)

# labels
plt.xlabel("x")
plt.ylabel("y")
plt.title("title")

# add a legend using the labels you gave to plot()
plt.legend(loc="best", ncol=1).draggable()
#$ end

#$ begin save_sin
# Show the figure (should pop up a new window)
plt.show()
# Save the plot to a file
plt.savefig("figures/plot_sin.pdf")
#$ end

if pause:
    raw_input("Continue? ")

#$ begin clear
# Clear the figure (so we can make a new one)
plt.clf()
#$ end

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#$ begin makeFigure
fig = plt.figure()
#$ end

#$ begin plot_axes_sin
axes = fig.add_axes((0.1, 0.1, 0.85, 0.80))

# plot the data
axes.plot(x, y, "b.", label="My data points")
axes.errorbar(x, y, xerr=None, yerr=dy, fmt=None, color='b')
axes.plot(x, model, "r:", label="Model")

# axis limits
axes.set_xlim(-1, 10)

# labels
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_title("Clever Title")

# add a legend using the labels you gave to plot()
fontProps = dict(size = "small")
axes.legend(loc="best", prop=fontProps, ncol=1).draggable()
#$ end

if pause:
    fig.show()
    raw_input("Continue? ")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#more plotting

#make the figure
fig = plt.figure()

#$ begin subplots
def makeSubplots(figure, nx=2, ny=2):
    """Return a generator of a set of subplots"""
    for window in range(nx*ny):  
        yield figure.add_subplot(nx, ny, window + 1) # 1-indexed

subplots = makeSubplots(fig)
# Initialize
axes = subplots.next()
#$ end
#$ begin histogram
#make a histogram of residuals, returns bin delimiters and number/bin
myhist = axes.hist(dy, bins=5)
axes.set_title("y residuals")
#$ end

fig.savefig("figures/plot_histogram.pdf")
#
# Redo that plot better
#
fig.clf()
subplots = makeSubplots(fig)
axes = subplots.next()

#$ begin histogramII
#make a histogram of residuals, returns bin delimiters and number/bin
myhist = axes.hist(dy, bins=5)
axes.set_title("y residuals")

axes.set_xlim(0.73, 1.01)
ymin, ymax = axes.get_ylim()
axes.set_ylim(ymin, 1.05*ymax)
#$ end

fig.savefig("figures/plot_histogramII.pdf")

#$ begin log
# Initialize and make a log plot
z = x**2 + np.sqrt(dy)

axes = subplots.next()
axes.semilogy(x, z, "g-.")
#$ end
#$ begin rhs_axis
# Move the axis label to the right hand size
axes.yaxis.set_label_position("right")
axes.set_ylabel(r"latex: $x^2+\sqrt{\sigma}$", size="small")
#$ end
#$ begin position_label
# can work in pixel, figure, or axes or plotting coordinates
# in this case put the text in 60%, 10% of the axes
axes.text(0.6, 0.1, "lower right", transform=axes.transAxes)
#$ end

fig.savefig("figures/plot_log.pdf")

#$ begin init_scatter
# Initialize and calculate points
axes = subplots.next()
xs = np.random.random(100)
ys = np.random.random(100)*2
zs = np.sqrt(xs**2 + ys**2/4.0)
#$ end

#$ begin plot_scatter
# Make plot
sc = axes.scatter(xs, ys, c=zs)
fig.colorbar(sc)
#$ end

fig.savefig("figures/plot_scatter.pdf")

#$ begin init_contour
# Initialize and calculate data
axes = subplots.next()
axis = np.linspace(-2.5, 2.5, 100)
X, Y = np.meshgrid(axis, axis)

sigma_x, sigma_y, f = 0.5, 1.0, 3
Z = 1/(2*np.pi*sigma_x*sigma_y)*np.exp(-0.5*((X/sigma_x)**2 + (Y/sigma_y)**2)) + \
    2/(2*np.pi*(f*sigma_x)**2)*np.exp(-0.5*(X**2 + Y**2)/(f*sigma_x)**2)
#$ end

#$ begin plot_contour
# Make a contour plot
CS = axes.contour(X,Y,Z)
#$ end

#$ begin label_contour
# put labels on the contours
axes.clabel(CS, inline=1, fontsize=8)
#$ end

#$ begin aspect
# make circles circular
axes.set_aspect('equal')
#$ end

#$ begin ticklabel
# Change the ticklabel size
axes.tick_params(axis="x", labelsize="small")
#$ end

#$ begin save_multi
# Save the plot to a file
fig.savefig("figures/plot_multi.pdf")
#$ end

if pause:
    raw_input("Continue? ")

plt.clf()

#$ begin plot_where
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50); y = np.sin(x)

plt.plot(x, y, '-', color="red")
l = y > 0
plt.plot(x[l], y[l], 'o', color="green")

plt.plot(x, np.where(l, y, 0.3*y), color="blue", ls=':')
#$ end
fig.savefig("figures/plot_where.pdf")

if pause:
    fig.show()
    raw_input("Exit? ")
