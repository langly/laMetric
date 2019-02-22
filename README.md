# laMetric

## Introduction 

Do this on your own risk.

## Gaining SSH access

Gaining SSH access to the box is requires some hardware modifications which I
am pretty sure will void your guarantee. So, don't tell me that I warned you.
However, it does not require a lot of hardware knowledge. There are probably
ways to hack your way around this, but I am not quite sure how to do it. They
have locked down access to the ssh port with iptables, so you cannot connect
directly to do any sort of bruteforce attempt.

Thus, this readme is based upon having physical access to the box itself. Which
I am pretty sure you already have.. Otherwise, why would you read this
tutorial.

For this steps, I have used Linux though. Mainly because working with the linux
file system on the lametric, it makes everything much simpler.

### Accessing the memory card and file system. 

As I mentioned, this is based on access to the physical lametric.

To begin the operation, you have to remove the bottom sticky pad thing of the
lametric. I just just a small knife to peel it of. Should be relative simple.
After this, find a small screwdriver. I used a phillips #0. Poke around the
edge, and you should be able to find 2 small screws. Unscrew those. After this,
on the same row, you should be able to find some small squares. Pop a flathead
in, and open the box that way.

This will give you access the the internals of the box itself. Here you should
be able to find a SMD microsd card holder. Push the card towards the bottom of
the holder, and it should pop out without any problems. You might have to bend
the holder part a bit though to gain access. However, not a lot of force should
be needed. 

With the SD card out, put it into your favorite SD card reader, find which
device it got detected as using dmsg. E.g. in my system it was detected as
/dev/sdb.

With that information, do the following: 
 dd if=/dev/sdb of=myfile.dsk

After having run for some time, it took about 20 minutes at my machine for the
entire 8GB, you should have a file named myfile.dsk containing the disk image of 
the lametric.

### Modifying the file system

## Drawing on the display

## Other features as I find out.
