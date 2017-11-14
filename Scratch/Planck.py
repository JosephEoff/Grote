import numpy as np
import scipy.constants as constants

h = constants.h
c = constants.c
k = constants.k

low_start=10700000000
low_stop=11700000000

hi_start=11700000000
hi_stop=12750000000

f_step=100000

temp_start = 1
temp_stop = 500
temp_step = 10

def plancksLaw(Frequency_Hz, Temperature_K):
    a = 2.0*h*Frequency_Hz**3/c**2
    b = h*Frequency_Hz/(k*Temperature_K)
    power= a/ (np.exp(b)-1)*4*constants.pi
    #print ("Freq:",  Frequency_Hz,  "power",  power)
    return power
    
def convertTodBm(watts):
    watts=watts*1000.0
    dbm=10*np.log10(watts)
    return dbm

def calculate_LowAverage(temperature):
    sum=0.0
    i=0
    for f in range(low_start,  low_stop, f_step):
        i=i+1
        sum=sum+plancksLaw(f, temperature)
    average=sum/i
    print ("Sum:",  sum,  "Average:", average)
    return average
    
def calculate_HiAverage(temperature):
    sum=0.0
    i=0
    for f in range(hi_start,  hi_stop, f_step):
        i=i+1
        sum=sum+plancksLaw(f, temperature)
    average=sum/i
    return average
    
def plotTemperatures():
    lowpower=0.0
    hipower=0.0
    for t in range(temp_start, temp_stop, temp_step):
        lowpower=convertTodBm(calculate_LowAverage(t))
        hipower=convertTodBm(calculate_HiAverage(t))
        c=t-273
        difference=hipower-lowpower
        print ("Kelvin:" , t,  " Celsius: ", c,  "Lo Power:", lowpower, "Hi Power:",hipower," difference:",  difference)
        
        
def plotMidPoints():
    lowpower=0.0
    hipower=0.0
    midlow=(low_stop+low_start)/2
    midhi=(hi_stop+hi_start)/2
    for t in range(temp_start, temp_stop, temp_step):
        temp=t/100
        lowpower=convertTodBm(plancksLaw(midlow, temp))
        hipower=convertTodBm(plancksLaw(midhi, temp))
        c=temp-273.0
        difference=hipower-lowpower
        print ("Kelvin:" , temp,  " Celsius: ", c,  "Lo Power:", lowpower, "Hi Power:",hipower," difference:",  difference)

def plotRange():
    for t in range(0, 100, 1):
        k=t+273.0
        db=convertTodBm(plancksLaw(11200000000, k))
        print ( t, ",", db)
