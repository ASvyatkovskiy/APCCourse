#$ begin import
import matplotlib.figure
import numpy as np
#$ end

np.random.seed(666)                  # make script deterministic

# make data
x = np.linspace(0.0, 9.0, 19)
model = np.sin(x)
dy = np.random.uniform(0.75, 1, len(x))
y = model + np.random.normal(scale=dy)

#$ begin makeFigure
fig = matplotlib.figure.Figure()
#$end

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
#$ end

#$ begin plotToCanvas
from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigCanvas

canvas = FigCanvas(fig)
canvas.print_figure("foo.png")          # a PNG file this time
#$ end
