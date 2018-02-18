#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


topo = Topo()
net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink)
switch = net.addSwitch( 's1' )

# Each host gets 50%/n of system CPU
h1 = net.addHost( 'h%s' % (h + 1), cpu=.5/n)
h2 = net.addHost( 'h%s' % (h + 1), cpu=.5/n)

# 10 Mbps, 5ms delay, 2% # loss, 1000 packet queue
net.addLink(h1, switch, bw=10, delay='5ms', loss=2, max_queue_size=1000, use_htb=True)
net.addLink(h2, switch, bw=10, delay='5ms', loss=2, max_queue_size=1000, use_htb=True)
net.start()
print "Dumping host connections"
dumpNodeConnections( net.hosts)
print "Testing network connectivity"
net.pingAll()
CLI(net)
print "Testing bandwidth between h1 and h4"
h1, h4 = net.get( 'h1', 'h4')
net.stop()
