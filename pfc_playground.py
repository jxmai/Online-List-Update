from algs import paid_pfc, static_opt, approx_off

list_size = int(input("Enter list size: "))
inp_sequence = input("Enter sequence: ")

sequence = []
for s in inp_sequence:
    sequence.append(int(s))

initial_list = [i+1 for i in range(list_size)]
opt_output = paid_pfc.serve_accesses(sequence,  initial_list[:])
static_output = static_opt.serve_accesses(sequence,  initial_list[:])
approx_output = approx_off.serve_accesses(sequence,  initial_list[:])

print("\PFC")
print("Final cost: ", opt_output[1])
print("Final List: ", opt_output[0])

print("\nSTATIC")
print("Final cost: ", static_output[1])
print("Final List: ", static_output[0])


print("\nApprox")
print("Final cost: ", approx_output[1])
print("Final List: ", approx_output[0])


print("\n Competitive Ratio:")
print("cr:", float(opt_output[1])/static_output[1])
print("cr:", float(opt_output[1])/approx_output[1])

print("Program ended successfully")
