import os
import sys, getopt
import pyglet
import arcade

outputFile = ''
opts, args = getopt.getopt(sys.argv[1:],"o:")
for opt, arg in opts:
    if opt in ("-o", "--ofile"):
        outputFile = arg
        print(outputFile)

music = pyglet.resource.media(outputFile)
music.play()

pyglet.app.run()