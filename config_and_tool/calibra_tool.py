# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:54:00 2018

@author: heyijia
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pdf import PdfPages

filepath = "/home/cjn/calibra_param/"
with open(filepath + 'planar.txt') as f:  # staticLaserPose_to_show
     planars = np.loadtxt(f, delimiter=" ", dtype='float', comments="#", skiprows=0, usecols=None)        

with open(filepath + 'RoiPoints.txt') as f:  # staticLaserPose_to_show
     points = np.loadtxt(f, delimiter=" ", dtype='float', comments="#", skiprows=0, usecols=None)        

with open(filepath + 'RoiPtOnLines.txt') as f:  # staticLaserPose_to_show
     lines = np.loadtxt(f, delimiter=" ", dtype='float', comments="#", skiprows=0, usecols=None)  
     
# create x,y
xx, yy = np.meshgrid(range(-5,5), range(-5,5))
xx = xx / 10.
yy = yy / 10.

stride = len(xx)

# plot the surface
with PdfPages('calibra_results_pdf.pdf') as pdf:
    
    plt3d = plt.figure().gca(projection='3d')
    for index in range(len(planars)):
    #for index in range(1):
        print len(planars)
        print "ww ",index
        timestamp = planars[index][0];
        print 11
    #########################  draw planars ##############################
        planar = planars[index]
        zz = (-planar[1]*xx - planar[2]*yy - planar[4])*1./planar[3];
        plt3d.plot_surface(xx,yy,zz,rstride=stride, cstride=stride,antialiased=False,linewidth=0, alpha=0.3)

    #########################  draw points ##############################
        x = []
        y = []
        z = []
        for pt in points:
            if pt[0] == timestamp :
                x.append(pt[1])
                y.append(pt[2])
                z.append(pt[3])   
                if len(x) > 2000 :
                    break;            
        print x,y,z
        plt3d.scatter(x,y,z)

        print 22
    #########################  draw lines ############################## 
        x = []
        y = []
        z = []       
        for line in lines:
            if line[0] == timestamp :
                x.append(int(line[1]))
                y.append(int(line[2]))
                z.append(int(line[3]))

            #plt3d.plot(x,y,z,"*-")
            #plt3d.plot(x,y,z)
        print 33
        t_str = "timestamp: " + str(index)        
        plt3d.text2D(0.05, 0.95, t_str, transform=plt3d.transAxes)
        plt3d.set_xlabel('X axis')
        plt3d.set_ylabel('Y axis')
        plt3d.set_zlabel('Z axis')
        plt3d.set_xlim(-1, 1)
        plt3d.set_ylim(-1, 1)
        plt3d.set_zlim(-1, 1)
        print 44
        plt.ion()
#        plt.show()
        print 77
        plt.pause(6)
        print 55
        pdf.savefig()  # saves the current figure into a pdf page  
        
        plt.cla()
        print 66
