#!/usr/bin/python

from __future__ import print_function
import time
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.util import dumpNodeConnections


class TopologiaLinear(Topo):
    def build(self):
        hosts = []
        switches = []

        for i in range(6):
            host = self.addHost(f'h{i+1}', ip=f'10.0.0.{i+1}/24', mac=f'00:00:00:00:00:{i+1:02x}')
            switch = self.addSwitch(f's{i+1}')
            self.addLink(host, switch, cls=TCLink, bw=25)
            hosts.append(host)
            switches.append(switch)

        for i in range(5):
            self.addLink(switches[i], switches[i+1], cls=TCLink, bw=25)


def run():
    topo = TopologiaLinear()
    net = Mininet(topo=topo, controller=None, link=TCLink, autoSetMacs=True)
    net.start()

    info('*** Informações de conexões dos hosts:\n')
    dumpNodeConnections(net.hosts)

    info('*** IP e interfaces dos hosts:\n')
    for h in net.hosts:
        print(h.name)
        print(h.cmd('ip addr'))

    info('*** Teste de ping entre todos os nós:\n')
    net.pingAll()

    h1 = net.get('h1')
    h2 = net.get('h2')

    info('*** Iniciando iperf (h1 como servidor, porta 5555)...\n')
    h1.cmd('iperf -s -p 5555 -i 1 > servidor.txt &')
    time.sleep(1)

    info('*** Executando iperf do h2 para h1 por 15 segundos...\n')
    h2.cmd(f'iperf -c {h1.IP()} -p 5555 -i 1 -t 15 > cliente.txt')

    info('*** Resultados salvos em servidor.txt e cliente.txt\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
