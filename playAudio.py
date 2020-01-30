import os
import sys, getopt
import pyglet
import arcade

outputFile = ''
outputDir = ''
opts, args = getopt.getopt(sys.argv[1:],"p:")
for opt, arg in opts:
    print(opt)
    if opt in ("-o", "--ofile"):
        outputFile = arg
        print(outputFile)
    if opt in ("-p"):
        outputDir = arg
        print(outputDir)

if outputDir == '':
    music = pyglet.resource.media(outputFile)
    music.play()
else:
   for file in os.listdir(outputDir):
        print(file)
        music = pyglet.resource.media("songs/"+outputDir+"/"+file)
        music.play()
        pyglet.app.run()

