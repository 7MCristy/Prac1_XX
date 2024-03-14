#lectura del fichero client.cfg

with open ('client.cfg', 'r') as cl_file:
    lines = cl_file.read().splitlines(keepends=True)
    print(lines)
