#!/bin/bash

binwalk -e $@ > /dev/null 2>&1 #binwalk on dolls.jpg and redirecting the output to /dev/null
cd _$@.extracted/ #going inside the extracted directory which is named "_dolls.jpg.extracted"

while true; do 
	if test -f "flag.txt"; then #checking if there is a flag.txt file
		cat "flag.txt" #printing the contect of the flag file
		exit 0
	fi

	cd base_images/ 
	image=$(find . -name *.jpg) #finding the next image
	image=$(echo "${image:2}")
	binwalk -e $image > /dev/null 2>&1
	cd _${image}.extracted/
	
done

