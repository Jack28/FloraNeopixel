
do: build upload

build: src/sketch.ino
	ino build --cppflags="-fno-use-cxa-atexit -ffunction-sections -fdata-sections -g -Os -w" -m flora8

clean:
	ino clean

upload:
	ino upload -m flora8
