#Nabil Rahiman
#NYU, Abudhabi
#email:nr83@nyu.edu
#18/Feb/2018


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import CPULimitedHost
from mininet.link import TCLink
import time

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            # 10 Mbps, 5ms delay, 2% loss, 1000 packet queue
            host = self.addHost('h%s' % (h + 1), cpu=.5/n )
            self.addLink(host, switch,  bw=10, delay='5ms', loss=2, max_queue_size=1000)

n = 3
print("creating network topology[ftp server and %s clients]" % str(n-1))
print("Please vereify the client[id].log")

topo = SingleSwitchTopo(n)
net = Mininet(topo,  host=CPULimitedHost, link=TCLink)
net.start()

ftp_server = net.get('h1')
ftp_server.cmd('./FTPserver &')
print("server is running")
ftp_server.cmd('ps')


clients = []
for i in range(2, n + 1):
	clients.append(net.get('h%s' % str(i)))

pids = []
for i in range(0, n - 1):
	clients[i].cmd('bash test.sh %s 8080 %s  &'  %   (ftp_server.IP(), str(i+1)))
	pids.append(int(clients[i].cmd('echo $!') ))

print("clients are connected:", pids)
for i in range(0, n - 1):
	clients[i].cmd('wait', pids[i])

#net.pingAll()
net.stop()

