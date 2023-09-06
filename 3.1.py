f = open("przyklad.txt", "r")
z_counter = 0
o_counter = 0
zrownowazone = 0
prawie = 0

for line in f:
    for num in line:
        if num == "0":
            z_counter += 1
        elif num == "1":
            o_counter += 1
        elif num == "\n":
            if z_counter == o_counter:
                zrownowazone += 1
            elif z_counter + 1 == o_counter or o_counter + 1 == z_counter:
                prawie += 1
            z_counter = 0
            o_counter = 0

print(zrownowazone, prawie)
