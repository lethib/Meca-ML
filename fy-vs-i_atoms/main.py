from function import *
import matplotlib.pyplot as plt

# Define Variables
filename = r'fy-vs-i_atoms/dump.test'
timestep_chosen = int(input('Numéro du timestep : '))

# Process
start_line = go_to_timestep(filename, timestep_chosen)
atoms_info = extract_atoms_info(filename, start_line)
fy, id_atoms = get_fy_and_id_atoms(atoms_info)
log_id_atoms = np.log(id_atoms)

# Plot
plt.scatter(log_id_atoms, fy)
plt.xlabel('ln(id_atoms)')
plt.ylabel('fy')
plt.title('fy vs ln(id_atoms) for this TIMESTEP : ' + str(timestep_chosen))
plt.show()