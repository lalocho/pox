#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.node import OVSController

class part1_topo(Topo):
    
    def build(self):
        pass
        #switch1 = self.addSwitch('switchname')
        #host1 = self.addHost('hostname')
        #self.addLink(hostname,switchname)
        FirstHost = self.addHost( 'h1' )
        SecondHost = self.addHost( 'h2' )
        ThirdHost = self.addHost( 'h3' )
        FourthHost = self.addHost( 'h4' )
       
        FirstSwitch = self.addSwitch( 's1' )
        
        # Add links between SW and Hosts
        self.addLink( FirstHost, FirstSwitch )
        self.addLink( SecondHost, FirstSwitch )
        self.addLink( FirstSwitch, FourthHost )
        self.addLink( FirstSwitch, ThirdHost )


topos = {'part1' : part1_topo}

if __name__ == '__main__':
    t = part1_topo()
    net = Mininet (topo=t,controller = OVSController)
    net.start()
    CLI(net)
    net.stop()
