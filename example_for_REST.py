#/*******************************************************************************
# * @author  Mario Minardi
# * @Email   mariominardi96@gmail.com
# * @file    example_for_REST.py
# * @Type    Python
# * @brief   TBC
# * @date    08/25/2022 (dd/mm/yy)
# *******************************************************************************/

#!/usr/bin/python


import re
import os
from time import sleep

from mininet.net import Mininet
from mininet.link import TCIntf
from mininet.log import setLogLevel, info
from mininet.topo import Topo
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.node import Controller, RemoteController

#initial definition of the network, this is a static definition so all the possible links have to be inserted
class StaticTopo(Topo):
    def build(self):
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')
        switch5 = self.addSwitch('s5')
        switch6 = self.addSwitch('s6')
        switch7 = self.addSwitch('s7')
        switch8 = self.addSwitch('s8')
        switch9 = self.addSwitch('s9')
        switch10 = self.addSwitch('s10')
        switch11 = self.addSwitch('s11')
        switch12 = self.addSwitch('s12')
        switch13 = self.addSwitch('s13')
        switch14 = self.addSwitch('s14')
        switch15 = self.addSwitch('s15')
        switch16 = self.addSwitch('s16')

        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
        host6 = self.addHost('h6')
        host7 = self.addHost('h7')
        host8 = self.addHost('h8')
        host9 = self.addHost('h9')
        host10 = self.addHost('h10')
        host11 = self.addHost('h11')
        host12 = self.addHost('h12')
        host13 = self.addHost('h13')
        host14 = self.addHost('h14')
        host15 = self.addHost('h15')
        host16 = self.addHost('h16')
        host17 = self.addHost('h17')
        host18 = self.addHost('h18')
        host19 = self.addHost('h19')
        host20 = self.addHost('h20')
        host21 = self.addHost('h21')
        host22 = self.addHost('h22')
        host23 = self.addHost('h23')
        host24 = self.addHost('h24')
        host25 = self.addHost('h25')
        host26 = self.addHost('h26')
        host27 = self.addHost('h27')

        #terrestrial links
        self.addLink(host1, switch1, bw = 1000)
        self.addLink(host2, switch1, bw = 1000)
        self.addLink(host3, switch1, bw = 1000)
        self.addLink(host4, switch2, bw = 1000)
        self.addLink(host5, switch2, bw = 1000)
        self.addLink(host6, switch2, bw = 1000)
        self.addLink(host7, switch3, bw = 1000)
        self.addLink(host8, switch3, bw = 1000)
        self.addLink(host9, switch3, bw = 1000)
        self.addLink(host10, switch6, bw = 1000)
        self.addLink(host11, switch6, bw = 1000)
        self.addLink(host12, switch6, bw = 1000)
        self.addLink(host13, switch7, bw = 1000)
        self.addLink(host14, switch7, bw = 1000)
        self.addLink(host15, switch7, bw = 1000)
        self.addLink(host16, switch8, bw = 1000)
        self.addLink(host17, switch8, bw = 1000)
        self.addLink(host18, switch8, bw = 1000)
        self.addLink(host19, switch10, bw = 1000)
        self.addLink(host20, switch10, bw = 1000)
        self.addLink(host21, switch10, bw = 1000)
        self.addLink(host22, switch11, bw = 1000)
        self.addLink(host23, switch11, bw = 1000)
        self.addLink(host24, switch11, bw = 1000)
        self.addLink(host25, switch12, bw = 1000)
        self.addLink(host26, switch12, bw = 1000)
        self.addLink(host27, switch12, bw = 1000)
        self.addLink(switch1, switch4, bw = 1000)
        self.addLink(switch2, switch4, bw = 1000)
        self.addLink(switch3, switch4, bw = 1000)
        self.addLink(switch4, switch5, bw = 1000)
        self.addLink(switch4, switch9, bw = 1000)
        self.addLink(switch6, switch5, bw = 1000)
        self.addLink(switch7, switch5, bw = 1000)
        self.addLink(switch8, switch5, bw = 1000)
        self.addLink(switch5, switch9, bw = 1000)
        self.addLink(switch10, switch9, bw = 1000)
        self.addLink(switch11, switch9, bw = 1000)
        self.addLink(switch12, switch9, bw = 1000)
        self.addLink(switch4, switch13, bw = 500, delay='27ms')
        self.addLink(switch5, switch13, bw = 500, delay='27ms') 
        self.addLink(switch9, switch13, bw = 500, delay='27ms')
        self.addLink(switch4, switch14, bw = 500, delay='27ms')
        self.addLink(switch5, switch14, bw = 500, delay='27ms')
        self.addLink(switch9, switch14, bw = 500, delay='27ms')
        self.addLink(switch4, switch15, bw = 500, delay='27ms')
        self.addLink(switch5, switch15, bw = 500, delay='27ms')
        self.addLink(switch9, switch15, bw = 500, delay='27ms')
        self.addLink(switch4, switch16, bw = 500, delay='27ms')
        self.addLink(switch5, switch16, bw = 500, delay='27ms')
        self.addLink(switch9, switch16, bw = 500, delay='27ms')


def limit():
    """Example of changing the TCLinklimits"""
    myTopo = StaticTopo()
    net = Mininet( topo=myTopo, link=TCLink, controller=RemoteController)
    net.start()
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    h5 = net.get('h5')
    h6 = net.get('h6')
    h7 = net.get('h7')
    h8 = net.get('h8')
    h9 = net.get('h9')
    h10 = net.get('h10')
    h11 = net.get('h11')
    h12 = net.get('h12')
    h13 = net.get('h13')
    h14 = net.get('h14')
    h15 = net.get('h15')
    h16 = net.get('h16')
    h17 = net.get('h17')
    h18 = net.get('h18')
    h19 = net.get('h19')
    h20 = net.get('h20')
    h21 = net.get('h21')
    h22 = net.get('h22')
    h23 = net.get('h23')
    h24 = net.get('h24')
    h25 = net.get('h25')
    h26 = net.get('h26')
    h27 = net.get('h27')

    s1 = net.get('s1')
    s2 = net.get('s2')
    s3 = net.get('s3')
    s4 = net.get('s4')
    s5 = net.get('s5')
    s6 = net.get('s6')
    s7 = net.get('s7')
    s8 = net.get('s8')
    s9 = net.get('s9')
    s10 = net.get('s10')
    s11 = net.get('s11')
    s12 = net.get('s12')
    s13 = net.get('s13')
    s14 = net.get('s14')
    s15 = net.get('s15')
    s16 = net.get('s16')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    limit()
