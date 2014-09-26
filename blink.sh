#!/usr/bin/env bash

#exec > /dev/ttyACM0

#set -x

function strlen(){
	echo -n $@ | wc -c
}

# set color for one LED
# arguments: led red green blue
function setColor(){
	led=$1
	red=$2
	green=$3
	blue=$4

	if [ `strlen $red` -lt 2 ]
	then
		red="0"${red}
	fi
	if [ `strlen $green` -lt 2 ]
	then
		green="0"${green}
	fi
	if [ `strlen $blue` -lt 2 ]
	then
		blue="0"${blue}
	fi

	echo -n $led$red$green$blue
}

# show written states
function show(){
	echo -n "s"
}

# display color
# arguments: red green blue
function setRing(){
	for i in `seq 0 9` a b c d e f
	do
	  setColor $i $1 $2 $3
	done
}

# clear
function clear(){
	setRing 0 0 0
	show
}

# color wheel
# arguments: red green blue timeout
function wheel(){
	for i in `seq 0 9` a b c d e f
	do
		setColor $i $1 $2 $3
		sleep $4
		show
	done
}

######################################


# shift through arguments as colors
function colors(){
	for i in `seq 1 $(($#/3))`
	do
		wheel $1 $2 $3 ".05"
		shift 3
	done
}


clear

while :
do
	colors 0 0 99  0 99 0  99 0 0  55 55 0  0 55 55
done
