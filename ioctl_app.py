
from fcntl import ioctl
import struct, sys, os

def test_get_mac():
    import socket
    ''' 
    /usr/include/i386-linux-gnu/bits/ioctls.h
    * Socket configuration controls. */
    #define SIOCGIFNAME 0x8910      /* get iface name       */
    #define SIOCSIFLINK 0x8911      /* set iface channel        */
    #define SIOCGIFCONF 0x8912      /* get iface list       */
    #define SIOCGIFFLAGS    0x8913      /* get flags            */
    #define SIOCSIFFLAGS    0x8914      /* set flags            */
    #define SIOCGIFADDR 0x8915      /* get PA address       */
    #define SIOCSIFADDR 0x8916      /* set PA address       */
    #define SIOCGIFDSTADDR  0x8917      /* get remote PA address    */
    #define SIOCSIFDSTADDR  0x8918      /* set remote PA address    */
    #define SIOCGIFBRDADDR  0x8919      /* get broadcast PA address */
    #define SIOCSIFBRDADDR  0x891a      /* set broadcast PA address */
    #define SIOCGIFNETMASK  0x891b      /* get network PA mask      */
    #define SIOCSIFNETMASK  0x891c      /* set network PA mask      */
    #define SIOCGIFMETRIC   0x891d      /* get metric           */
    #define SIOCSIFMETRIC   0x891e      /* set metric           */
    #define SIOCGIFMEM  0x891f      /* get memory address (BSD) */
    #define SIOCSIFMEM  0x8920      /* set memory address (BSD) */

    '''

    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        ip=ioctl(sock.fileno(), 0x8915, struct.pack('64s', b'lo'))
        print(ip[20:24])
        ip=socket.inet_ntoa(ip[20:24])
        print(ip)
    except:
        print(sys.exc_info())

# test_get_mac()

def test_get_ioctl():
    cmd = 22273 # IOCTL_BASE_GET_MUIR
    fd = os.open("/dev/ioctl", os.O_RDWR)
    print(ioctl(fd, cmd, b'\x12\x34\x56\x78'))
    # [ 7004.977830] <ioctl_d> ioctl: IOCTL_BASE_GET_MUIR 78563412
    os.close(fd)

test_get_ioctl()
