# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:15:57 2026

@author: Aksel
"""
import pandapower as pp

net = pp.create_empty_network()

# Busser
b1 = pp.create_bus(net, vn_kv=11, name="Bus 1")
b2 = pp.create_bus(net, vn_kv=11, name="Bus 2")

# Slack
pp.create_ext_grid(
    net,
    bus=b1,
    vm_pu=1.0
)

# Impedans
pp.create_impedance(
    net,
    from_bus=b1,
    to_bus=b2,
    rft_pu=0.1,
    xft_pu=0.5,
    sn_mva=100
)

# Last
pp.create_load(
    net,
    bus=b2,
    p_mw=50,
    q_mvar=20
)

# Lastflyt
pp.runpp(net, algorithm="nr",max_iteration=50)

print(net.res_bus)