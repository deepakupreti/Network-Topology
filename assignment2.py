#!/usr/bin/python
import random
import sys
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink 

subnet1 = '12.0.0.'
subnet2 = '13.0.0.'


def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller ***\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    first = []
    second = []
    for i in range(int (sys.argv[1]) ):
        if i%2 != 0:
        	name = 'h' + str(i)
        	ipadd = subnet2 + str(i+1)
            h2 = net.addHost(name,ip = ipadd )
            second.append(h2)
        else:
        	name = 'h' +str(i)
        	ipadd = subnet1 + str(i+1)
            h1 = net.addHost(name, ip = ipadd )
            first.append(h1)

        	

    info( '*** Adding switch\n' )
    switch = []
    for i in range(int(sys.argv[2])):
        s = net.addSwitch('s'+str(i+1))
        switch.append(s)


    info( '*** Creating links\n' )
    for i in range(int (sys.argv[2])):
        tmp = net.addLink( first[i], switch[i]) 
        tmp.intf1.config(bw=2)
        tmp = net.addLink(second[i], switch[i])
        tmp.intf1.config(bw=1)

    for i in range(int(sys.argv[2])-1):
        net.addLink(switch[i], switch[i+1])
 
    
    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
