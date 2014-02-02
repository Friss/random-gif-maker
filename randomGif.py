import os
import random
import subprocess
from moviepy.editor import *


def scanfolder(root):
	"""
	Get all movies with certain file extenstion andd append to list
	Params: root - path to root movies Directory
	Returns: movies - list of movies found.
	"""
	movies = []
	for path, dirs, files in os.walk(root):
		for f in files:
			if f.endswith('.mkv') or f.endswith('.m2ts') or f.endswith('.avi'):
			    #print os.path.join(path, f)
			    movies.append(os.path.join(path,f))
	#print movies	        
	return movies

def getLength(filename):
	"""
	Get information on choosen movie file. 
	Params: filename - path to movie to check
	Returns: list containing the line "Duration"
	Note: For some reason json output wouldn't show Duration while this call does.
	"""
	result = subprocess.Popen(["ffprobe", filename],stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	return [x for x in result.stdout.readlines() if "Duration" in x]


def makeGif(root):
	files = scanfolder(root) #Get all Movies

	moviepath = random.choice(files) #Random Movie from list

	moviename = moviepath[root.__len__():].split("/")[2] #Remove Root Directory and Subfolder
	moviename = moviename[:moviename.index(".")] #Remove file extenstion 
	moviename = moviename.split("[")[0] #Remove any [2013/1080p/720p]
	moviename = moviename.split("(")[0] #Remove any (2013/1080p/720p)
	print "Movie Chosen: " + moviename

	duration = getLength(moviepath)[0].split(",") #Get Duration
	duration = duration[0].split(" ")
	duration = duration[3].split(":") #Break into hour, mins, secs
	#print duration
	
	hour = random.randint(0,int(duration[0])) #Random hour
	mins = random.randint(0,int(duration[1])+1) #Random min
	secs = float(duration[2]) #Parse secs to float

	timePassed = round(random.uniform(0, 3),2) #Random seconds to elapse up to 3.
	
	"""
	print hour
	print mins
	print secs
	print timePassed
	"""
	
	#Make GIF 1/3 sized.
	VideoFileClip(moviepath).\
				subclip((hour,mins,secs),(hour,mins,secs+timePassed)).\
				resize(0.3).\
				to_gif('movie.gif')
	
	return moviename, hour, mins, secs
	

if __name__ == "__main__":
	var = raw_input("Enter Path to Movie Directory: ")
	print "Movies Path: ", var
	moviename, hour, mins, secs = makeGif(var)
	exit()