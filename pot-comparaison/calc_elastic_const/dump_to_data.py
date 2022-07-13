import linecache
import numpy as np

def split_info(info):
    res = info.strip('\n').split(' ')
    return res

def get_nb_atoms(dumpfile):
    return int(linecache.getline(dumpfile,4))

def get_box_dim(dumpfile):
    dim = np.zeros((3,2))
    for i in range(len(dim)):
        for j in range(len(dim[i])):
            value = split_info(linecache.getline(dumpfile,6+i))[j]
            dim[i][j] = value
    
    return dim

def get_atoms_info(dumpfile):
    nb_atoms = get_nb_atoms(dumpfile)
    atoms_info = []
    for i in range(nb_atoms):
        values = split_info(linecache.getline(dumpfile,10+i))
        atoms_info.append(values)
    
    return np.array(atoms_info)

#print(get_atoms_info(r'dump.simple-sw'))

def write_data(dumpfile, outputfile):
    box_dim = get_box_dim(dumpfile)
    atoms_info = get_atoms_info(dumpfile)
    with open(outputfile, 'w') as output_file:
        output_file.write('Commentaire inutile\n')
        output_file.write(str(get_nb_atoms(dumpfile)) + ' atoms\n')
        output_file.write('5 atom types\n')
        output_file.write(str(box_dim[0][0]) + ' ' + str(box_dim[0][1]) + ' xlo xhi\n')
        output_file.write(str(box_dim[1][0]) + ' ' + str(box_dim[1][1]) + ' ylo yhi\n')
        output_file.write(str(box_dim[2][0]) + ' ' + str(box_dim[2][1]) + ' zlo zhi\n')
        output_file.write('0.0 0.0 0.0 xy xz yz\n')

        output_file.write('\nMasses\n\n')
        output_file.write('1\t28.0\n2\t28.0\n3\t28.0\n4\t28.0\n5\t28.0\n')
        output_file.write('\nAtoms\n\n')
        
        for i in range(len(atoms_info)):
            line = ''
            for j in range(6):
                line += atoms_info[i][j] + '\t'
            output_file.write(line + '\n')
    return line

write_data(r'dump.pot-ml',r'run_lammps_test/elastic/pot-ML-w-less-atoms-elastic/pot-ml.dat')