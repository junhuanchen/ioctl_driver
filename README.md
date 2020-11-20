IOCTL Driver
============

Simple example on how to create a IOCTL driver for Linux.
This can be used for simple testing purposes:
* Access to a special register from kernel mode to get the result in user mode. For example Arm register from CP15 processor.
* Access to some memory mapped region
* ...

This repo contains the following folders:

dev/ : driver source code
-------------------------

* ioctl_interface.c is the source code of the driver. The function that should be modified to add more IOCTL
* ioctl_dev.h is the header file
* ioctl.h contains the list of IOCTL codes. This list is also included in the application
* Makefile to build the driver. If the driver is cross-compiled, the variable KDEV should be adjusted


app/ : application source code
------------------------------

* ioctl_app.c shows an example to access the driver and get the returned value
* Makefile to build the application


load_driver.sh
--------------

Load the driver _ioctl_. This probably needs sudo permissions!

usage
-------

### build ioctl.ko

* cd ./dev
* make all

```shell
  AR      /home/juwan/ioctl_driver/dev/built-in.a
  CC [M]  /home/juwan/ioctl_driver/dev/ioctl_interface.o
  LD [M]  /home/juwan/ioctl_driver/dev/ioctl.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /home/juwan/ioctl_driver/dev/ioctl.mod.o
  LD [M]  /home/juwan/ioctl_driver/dev/ioctl.ko
```

### load ioctl.ko

- sudo bash ./load_driver.sh

```shell
Loading module ioctl
Use lsmod to see all devices loaded
Removing stale nodes
Replacing the old nodes
To remove a device, do "/sbin/rmmod ioctl " and "rm -f /dev/"
```

### C get ioctl.ko

- cd ./app
- make all
- sudo ./ioctl_app

```shell
* Open Driver
Value is 12345678
* Close Driver
```

### Python get ioctl.ko

- sudo ioctl_app.py

```python
from fcntl import ioctl
import struct, sys, os

def test_get_ioctl():
    cmd = 22273 # IOCTL_BASE_GET_MUIR
    fd = os.open("/dev/ioctl", os.O_RDWR)
    print(ioctl(fd, cmd, b'\x12\x34\x56\x78'))
    # [ 7004.977830] <ioctl_d> ioctl: IOCTL_BASE_GET_MUIR 78563412
    os.close(fd)

test_get_ioctl()
```

### view log

- bash dmesg

```shell
[ 5005.290422] <ioctl_d> ioctl: IOCTL_BASE_GET_MUIR 0x12345678
```

### remove device

- sudo rmmod ./dev/ioctl.ko

### about write and read ?

next time~
