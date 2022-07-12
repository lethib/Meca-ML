import matplotlib.pyplot as plt
from data import *

# Sort by keys, returns a list of tuples
sw = sorted(energies_sw.items())
reaxff = sorted(energies_reaxff.items())
pot_ml = sorted(energies_ML.items())

# Unpack lists of pairs into two tuples
a_sw, e_sw = zip(*sw)
a_reax, e_reax = zip(*reaxff)
a_pot_ml, e_pot_ml = zip(*pot_ml)

# Convert to correct value for the graph
v_at_sw = [((a*4)**3)/nb_atoms for a in a_sw]
e_at_sw = [e/nb_atoms for e in e_sw]

v_at_reax = [((a*4)**3)/nb_atoms for a in a_reax]
e_at_reax = [e/nb_atoms for e in e_reax]

v_at_pot_ml = [((a*4)**3)/nb_atoms for a in a_pot_ml]
e_at_pot_ml = [e/nb_atoms for e in e_pot_ml]

# Plot on 3 different graphs (scale problem) but on the same figure
fig, axs = plt.subplots(1, 3)
fig.suptitle('Atomic Energy vs Atomic volume')

axs[0].plot(v_at_sw,e_at_sw, c='orange')
axs[0].set_title('SW')
axs[1].plot(v_at_reax,e_at_reax, c='red')
axs[1].set_title('ReaxFF')
axs[2].plot(v_at_pot_ml,e_at_pot_ml, c='green')
axs[2].set_title('Pot ML')

# plt.plot(v_at_sw,e_at_sw,label='SW')
# plt.plot(v_at_reax,e_at_reax,label='ReaxFF')
# plt.plot(v_at_pot_ml,e_at_pot_ml,label='Pot ML')
# plt.legend(loc='best')

fig.text(0.5, 0.02, 'Atomic Volume ($\mathring{A}^3$)', ha='center', va='center')
fig.text(0.03, 0.5, 'Potential Atomic Energy ($eV/atom$)', ha='center', va='center', rotation='vertical')

plt.tight_layout()
plt.show()