import linecache
import numpy as np

def split_atom_info(info):
    """Atom info string -> Atom info list"""
    res = info.strip('\n')
    atom = res.split(' ')
    return atom

def go_to_timestep(filename, int_timestep):
    """Returns the start line as an integer of atoms info for a given TIMESTEP"""
    nb_atoms = int(linecache.getline(filename,4))
    return (int_timestep*(nb_atoms+9) + 10)

def extract_atoms_info(filename, start_line):
    """Returns an array with all atoms info for a given TIMESTEP"""
    atoms_TS = []
    nb_atoms = int(linecache.getline(filename, 4))

    for i in range(start_line, start_line+nb_atoms):
        atom_info = split_atom_info(linecache.getline(filename, i))
        atoms_TS.append(atom_info + [i]) #To get the line number
    
    return np.array(atoms_TS)

def get_fy_and_id_atoms(atoms_array):
    """Returns the list of fy values and atoms id from an atoms info array"""
    fy = []
    id_atoms = []
    for i in range(len(atoms_array)):
        fy.append(float(atoms_array[i][6]))
        id_atoms.append(int(atoms_array[i][0]))
    return fy, id_atoms

# start_line = go_to_timestep(r'fy-vs-i_atoms/dump.test', 1)
# print(start_line)
# atoms = extract_atoms_info(r'fy-vs-i_atoms/dump.test',start_line)
# print(atoms)
# fy, id_atoms = get_fy_and_id_atoms(atoms)
# print(fy, id_atoms)