import linecache
import numpy as np 

def split_atom_info_head(info):
    """Atom info string -> Atom info list"""
    res = info.strip('\n')
    atom = res.split('\t')
    return atom

def split_atom_info(info):
    """Atom info string -> Atom info list"""
    res = info.strip('\n')
    atom = res.split(' ')
    return atom


def extract_atoms_info(log_filename):
    """Extracts all infos from the log.lammps file. Returns an array"""
    info = []
    run_thermo = int(split_atom_info_head(linecache.getline(log_filename,84))[2])
    run = int(split_atom_info_head(linecache.getline(log_filename,100))[2])
    nb_values = int(run/run_thermo)
    print(nb_values)

    for i in range(115, 115+nb_values+1):
        temp = split_atom_info(linecache.getline(log_filename,i))
        temp = [i for i in temp if i != '']
        info.append(temp)

    return np.array(info)

def get_pyy_ly(atoms_array):
    pyy = []
    ly = []
    for i in range(len(atoms_array)):
        pyy.append(-float(atoms_array[i][2]))
        ly.append(float(atoms_array[i][4]))
    return pyy, ly

