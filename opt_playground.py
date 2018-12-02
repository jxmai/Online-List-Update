from algs import opt, static_opt

list_size = int(input("Enter list size: "))
inp_sequence = input("Enter sequence: ")

sequence = []
for s in inp_sequence:
    sequence.append(int(s))

initial_list = [i+1 for i in range(list_size)]
opt_output = opt.serve_accesses(sequence,  initial_list[:])
static_output = static_opt.serve_accesses(sequence,  initial_list[:])

print("\nOPT")
print("Final cost: ", opt_output[1])
print("Final List: ", opt_output[0])

print("\nSTATIC")
print("Final cost: ", static_output[1])
print("Final List: ", static_output[0])

print("\n Competitive Ratio:")
print("cr:", float(opt_output[1])/static_output[1])

print("Program ended successfully")
