#!/usr/bin/python
# VU meter written in Python (www.python.org) by Tim Howlett 1st April 2013, 
# Does not work with Python 2.7.3 or 2.7.4 Does work with 3.2.3
# Requires the Pygame module (www.pygame.org)and the Pyaudio module (http://people.csail.mit.edu/hubert/pyaudio/)

import sys, pygame, pyaudio, wave, audioop, math
from pygame.locals import *

# set up a bunch of constants 
BGCOLOR = (0, 0, 0)
WINDOWWIDTH = 200
WINDOWHEIGHT = 500
PeakL = 0
PeakR = 0

# setup code
pygame.init()
pygame.mixer.quit() # stops unwanted audio output on some computers
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), RESIZABLE, vsync=1)
pygame.display.set_caption('VU Meter')
fontSmall = pygame.font.Font('freesansbold.ttf', 12)
pa = pyaudio.PyAudio()

info = pa.get_default_input_device_info()
print('Information: ',info)
RATE = int(info['defaultSampleRate'])
print('Rate info: ',RATE)
CHANNEL = int(info['maxInputChannels'])
print('Number of channels: ',CHANNEL)
print()

# open stream 
stream = pa.open(format = pyaudio.paInt16,
            channels = CHANNEL,
            rate = RATE,
            input = True,
            output=True,
            frames_per_buffer = 1024) #4096

print('Stream obj: ',stream)
while True: # main application loop
    # event handling loop for quit events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    # Read the data and calcualte the left and right levels
    data = stream.read(1024)


    ldata = audioop.tomono(data, 2, 1, 0)
    amplitudel = ((audioop.max(ldata, 2))/44100)  #32767
    LevelL = (int(44+(20*(math.log10(amplitudel+(1e-40))))))  # 41

    # print('Lamp: ',amplitudel)
    # pow_in_lsig = audioop.rms(ldata, 2)
    # print('Left level=',LevelL)
    
    rdata = audioop.tomono(data, 2, 0, 1)
    amplituder = ((audioop.max(rdata, 2))/44100)  #32767
    LevelR = (int(44+(20*(math.log10(amplituder+(1e-40))))))  # 41

    # print('Ramp: ',amplituder)
    # pow_in_rsig = audioop.rms(ldata, 2)
    # print('Right level=',LevelR)

    # Use the levels to set the peaks
    if (LevelL > PeakL):
        PeakL = LevelL
    elif (PeakL > 0):
        PeakL = PeakL - 0.2
        
    if (LevelR > PeakR):
        PeakR = LevelR
    elif (PeakR > 0):
        PeakR = PeakR - 0.2

    # Fill the screen to draw from a blank state and draw the clock face
    DISPLAYSURF.fill(BGCOLOR)

    # Write the scale and draw in the lines
    for dB in range (0, 60, 4):
        number = str(dB)
        text = fontSmall.render("-"+number, 1, (255, 255, 255))
        textpos = text.get_rect()
        DISPLAYSURF.blit(text, (55, (12*dB)))
        pygame.draw.line(DISPLAYSURF, (255, 255, 255), (40,5+(12*dB)), (50,5+(12*dB)), 1)
        pygame.draw.line(DISPLAYSURF, (255, 255, 255), (80,5+(12*dB)), (90,5+(12*dB)), 1)
    
    
    # Draw the boxes
    for i in range (0, LevelL):
        if i < 20: 
            pygame.draw.rect(DISPLAYSURF, (0, 192, 0), (10, (475-i*12), 30, 10))
        elif i >= 20 and i < 30:
            pygame.draw.rect(DISPLAYSURF, (255, 255, 0), (10, (475-i*12), 30, 10))
        else:
            pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (10, (475-i*12), 30, 10))
    for i in range (0, LevelR):
        if i < 20: 
            pygame.draw.rect(DISPLAYSURF, (0, 192, 0), (90, (475-i*12), 30, 10))
        elif i >= 20 and i < 30:
            pygame.draw.rect(DISPLAYSURF, (255, 255, 0), (90, (475-i*12), 30, 10))
        else:
            pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (90, (475-i*12), 30, 10))
    # Draw the peak bars
    pygame.draw.rect(DISPLAYSURF, (255,255,255), (10, (485-int(PeakL)*12), 30, 2))
    pygame.draw.rect(DISPLAYSURF, (255,255,255), (90, (485-int(PeakR)*12), 30, 2))
    
    pygame.display.update()
