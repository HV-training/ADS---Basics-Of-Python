

f = open('samplefile.txt', 'w')
f.close()

with open('samplefile.txt', 'w') as f:
    write_data = f.write("Hello Everyone")

f.closed

with open('days.txt', 'w') as f:
    days_list = f.write("sunday \n monday \n tuesday \n wednesday \n thursday \n friday \n saturday")



with open('days.txt', 'r') as f:
    read_days = f.read()
    print(type(read_days))

with open('days.txt', 'r') as f:
    read_days = f.readlines()
    print(type(read_days))

