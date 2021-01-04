import re

with open('input.txt', 'r') as f:
    Log = []
    for line in f.readlines():
        instruction = re.findall(r'^(mem)\[(\d+)\] = (\d+)$',line.strip())
        if instruction:
            Log.append(instruction[0])
        else:
            mask = re.findall(r'(mask) = ((X|\d)+)',line.strip())
            Log.append(mask[0][:2])
        
def part_1_2_combined(Log, part):
    Curr_Mask = None
    mem = {}
    count=0
    for inst in Log:
        if inst[0]=='mask':
            Curr_Mask = inst[1]
        else:
            if part==2:
                address, val = int(inst[1]), int(inst[2])
                if Curr_Mask:
                    bin_add = bin(address)[2:].zfill(len(Curr_Mask))
                    bin_add=[(bin_add[index] if bit=='0' else ('1' if bit=='1' else 'X')) for index, bit in enumerate(Curr_Mask)]
                    xpos = [index for index in range(len(bin_add)) if bin_add[index]=='X']
                    for i in range(2**len(xpos)):
                        new_address = bin_add.copy()
                        for index,bit in enumerate(bin(i)[2:].zfill(len(xpos))):
                            new_address[xpos[index]]=bit

                        new_address_int = int(''.join(new_address), 2)
                        if new_address_int in mem:
                            count-=mem[new_address_int]
                        mem[new_address_int]=val
                        count+=val
            else:
                val = int(inst[2])
                if Curr_Mask:
                    bin_val = bin(val)[2:].zfill(len(Curr_Mask))
                    bin_val=''.join([(bin_val[index] if bit=='X' else bit) for index, bit in enumerate(Curr_Mask)])
                    val = int(bin_val, 2)
                if inst[1] in mem:
                    count-=int(mem[inst[1]])
                mem[inst[1]]=val
                count+=val        
    return count

part_1_2_combined(Log, 1)
part_1_2_combined(Log, 2)