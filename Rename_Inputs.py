import bpy

ngroup = bpy.data.node_groups['Kohlensäurebläschen']
blw = ngroup.nodes['Blasenwerte']

for input in blw.inputs:
    for link in input.links:
        randval = link.from_node
        if randval.type != 'RANDOM_VALUE':
            continue

        for rvlink in [i for i in randval.inputs if i.is_linked and i.name in ['Min', 'Max']]:
            neuname = '{} {}'.format(input.name, rvlink.name)
            socket = rvlink.links[0].from_socket
            ginput = next(i for i in ngroup.inputs if i.identifier == socket.identifier)
            ginput.name = neuname
