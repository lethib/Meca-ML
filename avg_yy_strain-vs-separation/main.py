from function import *
import matplotlib.pyplot as plt
from rewrite_dump import trier_fichier

# Define variables
filename = r'avg_yy_strain-vs-separation/dump.test'
nb_atoms = int(linecache.getline(filename,4))
nb_timestep = int(count_nb_line(filename)/(nb_atoms+9))
trier_fichier(filename, r'avg_yy_strain-vs-separation/sorted.file', nb_timestep) #File sorting to always have the same structure
sorted_dump = r'avg_yy_strain-vs-separation/sorted.file'
a_0 = 0.93
Delta_X = 4
Delta_Y = 8
Y_MIN, Y_MAX, X_MIN, X_MAX = define_box(a_0, Delta_X, Delta_Y)
list_avg_yy_strain = []
list_separation = []

# Finding atoms in the box
arr_atom_type = extract_atom_type(sorted_dump, 1)
atoms_inside = atoms_in_box(arr_atom_type, Y_MIN, Y_MAX, X_MIN, X_MAX)
print(atoms_inside)


# Looping on all the TIMESTEPS
for j in range(nb_timestep):
    atoms_info = new_atoms_info(sorted_dump, atoms_inside, nb_atoms, j) #Actualing atoms position and force that were presents in the box
    sy_avg = calc_avg_yy_strain(atoms_info, nb_atoms, Delta_X, a_0)
    sep = calc_separation(atoms_info, Delta_Y, a_0)
    list_avg_yy_strain.append(sy_avg)
    list_separation.append(sep)

# Plot
plt.scatter(list_separation, list_avg_yy_strain) #Scatter -> Nuage de points
plt.xlabel('separation')
plt.ylabel('average yy strain')
plt.title('total cohesive law based on ' + str(nb_timestep) + ' timesteps')
plt.show()