from function import *
import matplotlib.pyplot as plt 

# Define Variables
filenames = [r'log.lammps-0,8', r'log.lammps-0,6', r'log.lammps-0,4', r'log.lammps-0,2', r'log.lammps-0,1', r'log.lammps']

# Process
for file in filenames:
    info = extract_atoms_info(file)
    pyy, ly = get_pyy_ly(info)
    if file == filenames[5]:
        plt.scatter(ly, pyy)
        plt.plot(ly,pyy, label= '0,0 bin')
    else :
        plt.scatter(ly, pyy)
        plt.plot(ly,pyy, label= '0,' + file[13] + ' bin')

# Plot
plt.xlabel('ly')
plt.ylabel('pyy')
plt.legend(loc='best')
plt.title('pyy vs ly')
plt.show()