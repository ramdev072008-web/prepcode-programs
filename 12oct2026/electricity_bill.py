units=int(input(" how many units are consumed by a householder"))

complete_group=units//50
remaining_units=units%50

print("completed groups are:",complete_group)
print("remaining units  are",remaining_units)