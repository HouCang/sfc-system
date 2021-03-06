import networkx as nx
# import matplotlib.pyplot as plt
from core.net import Net
from core.sfc import SFC
from core.vnf import VNF
import random

topology = None




def generate_substrate_network():
    substrate_network = Net()
    substrate_network.init_bandwidth_capacity(1, 6, 100)
    substrate_network.init_bandwidth_capacity(1, 2, 100)
    substrate_network.init_bandwidth_capacity(2, 3, 100)
    substrate_network.init_bandwidth_capacity(3, 4, 100)
    substrate_network.init_bandwidth_capacity(4, 5, 100)
    substrate_network.init_bandwidth_capacity(5, 6, 100)
    substrate_network.init_bandwidth_capacity(2, 6, 100)
    substrate_network.init_bandwidth_capacity(2, 5, 100)
    substrate_network.init_bandwidth_capacity(3, 5, 100)

    substrate_network.init_link_latency(1, 6, 2)
    substrate_network.init_link_latency(1, 2, 2)
    substrate_network.init_link_latency(2, 3, 2)
    substrate_network.init_link_latency(3, 4, 2)
    substrate_network.init_link_latency(4, 5, 2)
    substrate_network.init_link_latency(5, 6, 2)
    substrate_network.init_link_latency(2, 6, 2)
    substrate_network.init_link_latency(2, 5, 2)
    substrate_network.init_link_latency(3, 5, 2)

    substrate_network.init_node_cpu_capacity(1, 100)
    substrate_network.init_node_cpu_capacity(2, 100)
    substrate_network.init_node_cpu_capacity(3, 100)
    substrate_network.init_node_cpu_capacity(4, 100)
    substrate_network.init_node_cpu_capacity(5, 100)
    substrate_network.init_node_cpu_capacity(6, 100)

    return substrate_network

topology = generate_substrate_network()





