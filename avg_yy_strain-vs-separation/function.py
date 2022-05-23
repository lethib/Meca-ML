import linecache
import numpy as np

def split_atom_info(info):
    """Atom info string -> Atom info list"""
    res = info.strip('\n')
    atom = res.split(' ')
    return atom

def count_nb_line(file):
    """Count the number of line of 1 dump file"""
    fd = open(file,'r')
    n=0
    for line in fd:
        n += 1
    fd.close()
    return n


def extract_atom_type(file, type):
    """Extract atom type from a dump.file for ONE TIMESTEP ! Return an array"""
    atom_type_1 = []
    nb_atoms = int(linecache.getline(file,4))
    nb_line = nb_atoms+9

    for i in range(1,nb_line+1):
        atom_info = split_atom_info(linecache.getline(file,i))
        if len(atom_info) == 1:
            continue
        elif atom_info[1] == str(type):
            atom_type_1.append(atom_info + [i]) #i correspond to the line number which would be helpful for later
    return np.array(atom_type_1)

def define_box(a_0, Delta_X, Delta_Y):
    """Return Box coordinates"""
    Y_MIN = 10*a_0
    Y_MAX = Y_MIN + Delta_Y*a_0
    X_MIN = 10*a_0
    X_MAX = X_MIN + Delta_X*a_0
    return Y_MIN, Y_MAX, X_MIN, X_MAX

def atoms_in_box(atoms_array, Y_MIN, Y_MAX, X_MIN, X_MAX):
    """Return an array with all atoms in the box"""
    atoms_in = []
    for i in range(0,len(atoms_array)):
        if float(atoms_array[i][2]) >= X_MIN and float(atoms_array[i][2]) <= X_MAX:
            if float(atoms_array[i][3]) >= Y_MIN and float(atoms_array[i][3]) <= Y_MAX:
                atoms_in.append(atoms_array[i])
    return np.array(atoms_in)

def new_atoms_info(file, array_atom_in, nb_atoms, ite):
    """Return the atoms that were in the box new information as an array"""
    lines_to_go = []
    for i in range(len(array_atom_in)):
        lines_to_go.append(int(array_atom_in[i][8])+ite*(nb_atoms+9))

    res = []
    for line in lines_to_go:
        res.append(split_atom_info(linecache.getline(file, line)))
    return np.array(res)

def calc_avg_yy_strain(array_atoms_in, nb_atoms, Delta_X, a_0):
    """Return the average yy strain"""
    sum = 0
    for i in range(0,len(array_atoms_in)):
        sum += float(array_atoms_in[i][6])
    fy_avg = sum*(1/nb_atoms)
    sy_avg = fy_avg/(Delta_X*a_0)
    return sy_avg

def calc_separation(array_atoms_in, Delta_Y, a_0):
    """Return the separation"""
    L_0 = Delta_Y*a_0
    Y_list = []
    for i in range(0,len(array_atoms_in)):
        Y_list.append(float(array_atoms_in[i][3]))
    sep = max(Y_list) - min(Y_list) - L_0
    return sep