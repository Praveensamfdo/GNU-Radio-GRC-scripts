# Import required modules

import struct

# Define variables

buff_len = 52
state = 0
payload_list = []
float_list = []

# Open the file

f_in = open ('output.tmp', 'rb')

# Extract the payload from the file
while True:
    if (state == 0):
        buff = f_in.read(buff_len)
        if ((buff[0] == 37) and (buff[51] == 93)):
            continue

        else:   # End of preamble
            state = 1
            continue

    elif (state == 1):
        if b'%UUU' in buff:
            payload_list.extend([byte for byte in buff[: buff.index(b'%UUU')]])  # Add all the Bytes before '%UUU' to payload_list
            print ("End of text")
            break

        payload_list.extend([byte for byte in buff])
        buff = f_in.read(buff_len)

        if len(buff) == 0:
            break

f_in.close()

# Convert the payload to double precision floating point values

payload_len = len(payload_list)
i = 0

while (i < payload_len):
    byte_string = bytes(bytearray(payload_list[i: i + 8]))
    double_value = struct.unpack('d', byte_string)[0]
    float_list.append(double_value)
    i += 8

print(float_list)