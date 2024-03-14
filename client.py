import socket

params = {}
elements = []
with open('client.cfg', 'r') as file:
    for line in file:
        if line.strip():  # Ignorar líneas en blanco
            key, value = line.strip().split('=')
            params[key.strip()] = value.strip().encode()
            
            if key.strip() == 'elements':
                # Dividir la lista de dispositivos por ';'
                devices = value.strip().split(';')
                elements = devices
            if key.strip() == 'name':
                name = value
            elif key.strip() == 'situation':
                situation = value
            elif key.strip() == 'mac':
                mac = value
            elif key.strip() == 'local_tcp':
                local_tcp = value
            elif key.strip() == 'server':
                server = value
            elif key.strip() == 'srv_udp':
                srv_udp = value
           
    
print("Bytes generados:", params)
print("elements:", elements)
print("name:", name)



