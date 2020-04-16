import matplotlib.pyplot as plt
import three_state_ca

rule = 110
length = 5
initial_conditions = [1,0,1,0,1]
field = three_state_ca.spacetime_field(rule, initial_conditions, length)
three_state_ca.spacetime_diagram(field)
plt.savefig('rule110.pdf')
