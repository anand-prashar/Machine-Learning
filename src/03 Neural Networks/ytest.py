# coding: utf-8
# import scipy.io as io
from scipy import linspace, io
from pylab import *
from cmath import phase
from math import *

# Load the .mat files
testData = io.loadmat('BelkinTestData_1.mat')
taggingData = io.loadmat('TaggingInfo_1.mat')

# Extract tables
buf = testData['Buffer']
LF1V = buf['LF1V'][0][0]
LF1I = buf['LF1I'][0][0]
LF2V = buf['LF2V'][0][0]
LF2I = buf['LF2I'][0][0]
L1_TimeTicks = buf['TimeTicks1'][0][0]
L2_TimeTicks = buf['TimeTicks2'][0][0]
HF              = buf['HF']
HF_TimeTicks = buf['TimeTicksHF']

# Calculate power (by convolution)
L1_P = LF1V * LF1I.conjugate()
L2_P = LF2V * LF2I.conjugate()
#
L1_ComplexPower = L1_P.sum(axis=1) 
L2_ComplexPower = L2_P.sum(axis=1)

# Extract components
L1_Real = L1_ComplexPower.real
L1_Imag = L1_ComplexPower.imag
L1_App  = abs(L1_ComplexPower)
L2_Real = L2_ComplexPower.real
L2_Imag = L2_ComplexPower.imag
L2_App  = abs(L2_ComplexPower)
#
L1_Pf = [cos(phase(L1_P[i,0])) for i in range(len(L1_P[:,0]))]
L2_Pf = [cos(phase(L2_P[i,0])) for i in range(len(L2_P[:,0]))]


taggingInfo = taggingData['TaggingInfo']

# ======================================================================
# Plotting
fig = figure(1)

# Plot real power consumption
ax1 = fig.add_subplot(411)
ax1.plot(L1_TimeTicks, L1_Real, color='blue')
# ax1.set_title('Real Power (W) and ON/OFF Device Category IDs')
for i in range(len(taggingInfo)):
    ax1.plot([taggingInfo[i,1],taggingInfo[i,1]], [0,4000], color='green', linewidth=2)
    ax1.plot([taggingInfo[i,2],taggingInfo[i,2]], [0,4000], color='red', linewidth=2)
    str1 = 'ON-%s' % taggingInfo[i,0]
    ax1.text(taggingInfo[i,1],4000, str1)
    str2 = 'OFF-%s' % taggingInfo[i,0]
    ax1.text(taggingInfo[i,2],4000, str1)

# Plot Imaginary/Reactive power (VAR)
ax2 = fig.add_subplot(412)
ax2.plot(L1_TimeTicks,L1_Imag)
# ax2.set_title('Imaginary/Reactive power (VAR)')

# Plot Power Factor
ax3 = fig.add_subplot(413)
ax3.plot(L1_TimeTicks,L1_Pf)
# ax3.set_title('Power Factor');
# ax3.set_xlabel('Unix Timestamp');

# Plot HF Noise
ax4 = fig.add_subplot(414)
freq = linspace(0,4096,1000000)
# ax4.set_title('High Frequency Noise')
# ax4.set_ylabel('Frequency KHz')

show()