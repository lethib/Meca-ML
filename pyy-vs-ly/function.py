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
    run_thermo = int(split_atom_info_head(linecache.getline(log_filename,93))[2])
    run = int(split_atom_info_head(linecache.getline(log_filename,109))[2])
    nb_values = int(run/run_thermo)

    for i in range(158, 158+nb_values+1):
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

def get_l0(atoms_array):
    """Returns the value of l0"""
    return float(atoms_array[0][4])

def young_module(list_pyy, list_ly, l0):
    """Returns the value of the Young Module"""
    young = []
    eps = []
    delta_eps = []
    delta_pyy = []
    for i in range(len(list_ly)):
        eps_i = (list_ly[i]-l0)/l0
        eps.append(eps_i)

    for j in range(70,len(eps)-1):
        delta_eps.append(eps[j+1] - eps[j])
        delta_pyy.append(list_pyy[j+1] - list_pyy[j])
    
    for k in range(len(delta_eps)):
        young.append(delta_pyy[k]/delta_eps[k])
    return np.mean(young), eps, len(list_pyy)
