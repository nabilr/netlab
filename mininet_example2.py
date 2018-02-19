#Nabil Rahiman
#NYU, Abudhabi
#email:nr83@nyu.edu
#18/Feb/2018


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

"Create and test a simple network"
topo = SingleSwitchTopo(n=4)
net = Mininet(topo)
net.start()
print "Dumping host connections"
dumpNodeConnections(net.hosts)
print "Testing network connectivity"
h1 = net.get('h1')
h2 = net.get('h2')
print("ping h2")
#CLI(net)
print h1.cmd('ping -c 3 %s' %  h2.IP())
#net.pingAll()
net.stop()

