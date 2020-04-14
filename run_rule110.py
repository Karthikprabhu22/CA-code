import matplotlib.pyplot as plt
import three_state_ca

rule = 110
length = 10
initial_conditions = three_state_ca.random_string(length)
field = three_state_ca.spacetime_field(rule, initial_conditions, length)
three_state_ca.spacetime_diagram(field)
plt.savefig('rule110.pdf')
