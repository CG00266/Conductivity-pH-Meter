
"""
ldr.py
Display analog data from Arduino using Python (matplotlib)
Author: Mahesh Venkitachalam
Website: electronut.in
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([],[])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.ht

plt.show() 


# import sys, serial, argparse
# import numpy as np
# from time import sleep
# from collections import deque

# import matplotlib.pyplot as plt 
# import matplotlib.animation as anim

# MAX_X = 100   #width of graph  
# MAX_Y = 5000  #height of graph

# comport = 'COM4'
# baudrate = 250000
# saved_data = []

# ser = serial.Serial(comport, baudrate)

# # intialize line to horizontal line on 0
# line = deque([0.0]*MAX_X, maxlen=MAX_X)

# def update(fn, l2d):  
#     data = ser.readline()
#     line.append(data)
#     saved_data.append(data)
#     # set the l2d to the new line coords
#     # args are ([x-coords], [y-coords])
#     l2d.set_data(range(-MAX_X/2, MAX_X/2), line)

# fig = plt.figure()  
# # make the axes revolve around [0,0] at the center
# # instead of the x-axis being 0 - +100, make it -50 - +50
# # ditto for y-axis -512 - +512
# a = plt.axes(xlim=(-(MAX_X/2),MAX_X/2), ylim=(-(MAX_Y/2),MAX_Y/2))  
# # plot an empty line and keep a reference to the line2d instance
# l1, = a.plot([], [])  
# ani = anim.FuncAnimation(fig, update, fargs=(l1,), interval=50)

# plt.show()  

# #Save data 


















#More rigorous implementation for later... 
# plot class
# class AnalogPlot:
#   # constr
#   def __init__(self, strPort, maxLen):
#       # open serial port
#       self.ser = serial.Serial(strPort, 250000)
#       self.ax = deque([0.0]*maxLen)
#       self.ay = deque([0.0]*maxLen)
#       self.maxLen = maxLen

#   # add to buffer
#   def addToBuf(self, buf, val):
#       if len(buf) < self.maxLen:
#           buf.append(val)
#       else:
#           buf.pop()
#           buf.appendleft(val)

#   # add data
#   def add(self, data):
#       assert(len(data) == 2)
#       self.addToBuf(self.ax, data[0])
#       self.addToBuf(self.ay, data[1])

#   # update plot
#   def update(self, frameNum, a0, a1):
#       try:
#           line = self.ser.readline()
#           data = [float(val) for val in line.split()]
#           # print data
#           if(len(data) == 2):
#               self.add(data)
#               a0.set_data(range(self.maxLen), self.ax)
#               a1.set_data(range(self.maxLen), self.ay)
#       except KeyboardInterrupt:
#           print('exiting')
      
#       return a0, 

#   # clean up
#   def close(self):
#       # close serial
#       self.ser.flush()
#       self.ser.close()    

# # main() function
# def main():
#   # create parser
#   parser = argparse.ArgumentParser(description="LDR serial")
#   # add expected arguments
#   parser.add_argument('--port', dest='port', required=True)

#   # parse args
#   args = parser.parse_args()
  
#   #strPort = '/dev/tty.usbserial-A7006Yqh'
#   strPort = args.port

#   print('reading from serial port %s...' % strPort)

#   # plot parameters
#   analogPlot = AnalogPlot(strPort, 100)

#   print('plotting data...')

#   # set up animation
#   fig = plt.figure()
#   ax = plt.axes(xlim=(0, 100), ylim=(0, 1023))
#   a0, = ax.plot([], [])
#   a1, = ax.plot([], [])
#   anim = animation.FuncAnimation(fig, analogPlot.update, 
#                                  fargs=(a0, a1), 
#                                  interval=50)

#   # show plot
#   plt.show()
  
#   # clean up
#   analogPlot.close()


# # call main
# if __name__ == '__main__':
#   main()