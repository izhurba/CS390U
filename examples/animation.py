# Example of animation of pyplot patches
# This example grows and shrinks a Rectangle
# Written by Aaron Gordon, Feb. 2019
#
# See https://nickcharlton.net/posts/drawing-animating-shapes-matplotlib.html
# for (a possibly dated??) discussion and other examples
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.animation as animation

FRAME_DELTA = 400       # milliseconds
fig, ax = plt.subplots()
rwidth = 1      # rectangle's width
rheight = 2     # rectangle's height

#values = [7, 12, 14, 18, 24, 25, 21, 19, 13, 6, 5, 6, 4, 5]
values = []
#vals = np.random.randint(50, size = 14)
rect_ = Rectangle((0, 0), rwidth, rheight)
rect_1 = Rectangle((1, 0), rwidth, rheight)
rect_2 = Rectangle((2, 0), rwidth, rheight)
rect_3 = Rectangle((3, 0), rwidth, rheight)
rect_4= Rectangle((4, 0), rwidth, rheight)
rect = Rectangle((0, 0), rwidth, rheight)
rect1 = Rectangle((1, 0), rwidth, rheight)
rect2 = Rectangle((2, 0), rwidth, rheight)
rect3 = Rectangle((3, 0), rwidth, rheight)
rect4 = Rectangle((4, 0), rwidth, rheight)


values = np.random.rand(10,50,1)
values = [i * 100 for i in values]


def init():                     # init function for the animation
    #top_y = max(values) + 3
    ax.set_xlim(0.0, 5.0)
    ax.set_ylim(0.0, 200)
    rect.set_color('r')
    rect1.set_color('g')
    rect2.set_color('b')
    rect3.set_color('c')
    rect4.set_color('y')
    rect_.set_color('m')
    rect_1.set_color('c')
    rect_2.set_color('y')
    rect_3.set_color('m')
    rect_4.set_color('k')

    ax.add_patch(rect_)
    ax.add_patch(rect_1)
    ax.add_patch(rect_2)        
    ax.add_patch(rect_3)
    ax.add_patch(rect_4)
    ax.add_patch(rect)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rect3)
    ax.add_patch(rect4)
    return rect_, rect_1, rect_2, rect_3, rect_4, rect, rect1, rect2, rect3, rect4,


def animate(num):           # called each frame with rectangle height
    rect_.set_height(num[0])
    rect_1.set_height(num[1])
    rect_2.set_height(num[2])
    rect_3.set_height(num[3])
    rect_4.set_height(num[4])

    rect.set_y(rect_.get_height())
    rect1.set_y(rect_1.get_height())
    rect2.set_y(rect_2.get_height())
    rect3.set_y(rect_3.get_height())
    rect4.set_y(rect_4.get_height())

    rect.set_height(num[5])
    rect1.set_height(num[6])
    rect2.set_height(num[7])
    rect3.set_height(num[8])
    rect4.set_height(num[9])
    return rect_, rect_1, rect_2, rect_3, rect_4, rect, rect1, rect2, rect3, rect4,


#def animate2(tum):           # called each frame with rectangle height
#    rect1.set_height(tum)
#    return rect1,            # return a sequence of patches to draw



ani = animation.FuncAnimation(fig, animate, frames=values, init_func=init,
                              interval=FRAME_DELTA, repeat=False, blit=True)
#ani2 = animation.FuncAnimation(fig, animate2, frames=values[0], init_func=init,
#                              interval=FRAME_DELTA, repeat=False, blit=True)
plt.show()
