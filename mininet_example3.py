#Nabil Rahiman
#NYU, Abudhabi
#email:nr83@nyu.edu
#18/Feb/2018

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            # Each host gets 50%/n of system CPU
            host = self.addHost( 'h%s' % (h + 1), cpu=.5/n )
            # 10 Mbps, 5ms delay, 2% loss, 1000 packet queue
            self.addLink( host, switch, bw=10, delay='5ms', loss=2, max_queue_size=1000 )

"Create and test a simple network"
topo = SingleSwitchTopo(n=4)

# Mininet provides performance limiting and isolation features, through the
# CPULimitedHost and TCLink classes.
net = Mininet(topo, host=CPULimitedHost, link=TCLink)
net.start()
print "Dumping host connections"
dumpNodeConnections(net.hosts)
print "Testing network connectivity"
net.pingAll()
CLI(net)
net.stop()

