from function import *
import matplotlib.pyplot as plt 

# Define Variables
filename = r'log.lammps'

# Process
info = extract_atoms_info(filename)
pyy, ly = get_pyy_ly(info)

# Plot
plt.scatter(ly, pyy)
plt.plot(ly,pyy)
plt.xlabel('ly')
plt.ylabel('pyy')
plt.title('pyy vs ly')
plt.show()