import numpy as np
from numpy import pi, sin
import sounddevice as sd


fs = 20000  
dt = 1/fs

t1 = np.arange(0, 1.5, dt)
t2 = np.arange(0, 1.0, dt)
t3 = np.arange(0, 0.5, dt)



f_g = 195.997720
f_c1 = 261.625568
f_d1 = 293.664771
f_h1 = 246.41653
f_e1 = 329.627560	
f_f1 = 349.228235
f_a1 = 440.000005
f_g1 = 391.995440
f_fis1 = 369.994427


x_c1_1 = np.sin(2*pi*f_c1*t1)
x_g1_1 = np.sin(2*pi*f_g1*t1)


x_g_2 = np.sin(2*pi*f_g*t2)
x_c1_2 = np.sin(2*pi*f_c1*t2)
x_h1_2 = np.sin(2*pi*f_h1*t2)
x_d1_2 = np.sin(2*pi*f_d1*t2)
x_e1_2 = np.sin(2*pi*f_e1*t2)
x_f1_2 = np.sin(2*pi*f_f1*t2)
x_a1_2 = np.sin(2*pi*f_a1*t2)


x_d1_3 = np.sin(2*pi*f_d1*t3)
x_c1_3 = np.sin(2*pi*f_c1*t3)
x_e1_3 = np.sin(2*pi*f_e1*t3)
x_f1_3 = np.sin(2*pi*f_f1*t3)
x_g1_3 = np.sin(2*pi*f_g1*t3)
x_fis1_3 = np.sin(2*pi*f_fis1*t3)


melody = np.concatenate((x_g_2, x_c1_2, x_c1_2,x_d1_3, x_c1_3, x_h1_2, x_h1_2, 
                         x_g_2, x_d1_2, x_d1_2,x_e1_3, x_d1_3, x_c1_1, x_g_2, x_c1_2, x_c1_2,x_d1_3, x_c1_3, x_h1_2, x_h1_2, 
                         x_g_2, x_d1_2, x_d1_2,x_e1_3, x_d1_3, x_c1_1, x_g_2, x_e1_2, x_e1_2,
                         x_f1_3, x_e1_3, x_d1_2, x_d1_2, x_f1_2, x_f1_2, x_a1_2, x_g1_3, x_fis1_3,
                         x_g1_1, x_g_2, x_e1_2, x_e1_2, x_f1_3, x_e1_3, x_d1_2, x_d1_2, x_g_2,
                         x_d1_2, x_d1_2, x_e1_3, x_d1_3, x_c1_1, x_g_2, x_e1_2, x_e1_2,
                         x_f1_3, x_e1_3, x_d1_2, x_d1_2, x_f1_2, x_f1_2, x_a1_2, x_g1_3, x_fis1_3,
                         x_g1_1, x_g_2, x_e1_2, x_e1_2, x_f1_3, x_e1_3, x_d1_2, x_d1_2, x_g_2,
                         x_d1_2, x_d1_2, x_e1_3, x_d1_3, x_c1_1))


sd.play(melody, fs)