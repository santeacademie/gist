#!/bin/env python3

import os

README = open("README.md","w+")

README.write("#GISTS\n")

for dir in os.scandir('.'):
	if os.path.isdir(dir) and dir.name[0] != '.':
		classifier = dir.name
		README.write("\n\n> {}".format(classifier))

		for subdir in os.scandir(dir):
			gist = subdir.name
			README.write("\n- {}".format(gist))

README.write("\n\n\n")
README.close()

