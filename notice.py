#!/bin/env python3

import os

README = open("README.md","w+")

README.write("# GISTS\n")

for dir in os.scandir('.'):
	if os.path.isdir(dir) and dir.name[0] != '.':
		classifier = dir.name
		README.write("\n\n> {}".format(classifier))

		for subdir in os.scandir(dir):
			gist = subdir.name

			descPath = '{}/{}/{}'.format(dir.name, subdir.name, 'DESCRIPTION.md')
			description = '-'

			if (os.path.isfile(descPath)):
				descFile = open(descPath, mode='r')
				description = descFile.read()
				descFile.close()
			README.write("\n- [{}](https://raw.githubusercontent.com/santeacademie/gist/master/{}/{}/{}) | {}".format(gist, classifier, gist, gist, description))

README.write("\n\n\n")
README.close()

