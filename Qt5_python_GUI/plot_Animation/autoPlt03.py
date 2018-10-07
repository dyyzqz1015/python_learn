import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

print(fig,ax)
x = np.arange(0, 2*np.pi, 0.01)

line, = ax.plot(x, np.sin(x))
print(x)


# plt.plot(x,np.sin(x))
# line=plt.plot(x,np.sin(x))
# fig=plt.Figure()

def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,
# print([np.nan]*len(x))
# print(init())
def animate(i):
    line.set_ydata(np.sin(x+i))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    interval=50,
    # blit=True,
    # save_count=50
)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()