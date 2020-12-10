# function: 

byte = b'\x02\x04\x00\x01'
int_big = int.from_bytes(byte, 'big')
int_little = int.from_bytes(byte, 'little')

print("function - big: ", int_big, "litundefinedtle: ", int_little)

###################################################################################

# calculation: 
base = 256
print("factors: ", byte[0],", ", byte[1],", ", byte[2], ", ", byte[3])
int_big_2     = byte[0] * base **3 + byte[1] * base **2 + byte[2] * base **1 + byte[3] * base**0;
int_little_2  = byte[3] * base **3 + byte[2] * base **2 + byte[1] * base **1 + byte[0] * base**0;

print("calculation - big: ", int_big_2, ", little: ", int_little_2)
