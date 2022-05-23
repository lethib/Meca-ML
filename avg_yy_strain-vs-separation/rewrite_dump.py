# coding: utf-8

import numpy as np
from pandas import DataFrame

def trier_fichier(infile, output_file, timesteps):
    """Sorts the dump.file by atom id in order to have the same structure. Creates an output file."""

    # nombre d'atomes
    input_file = open(infile, 'r')
    for i in range(3):
        input_file.readline()
    nb_atoms = int(input_file.readline().strip('\n'))
    input_file.close()


    # tri de tous les timesteps du fichier
    with open(infile, 'r') as input_file:
        with open(output_file, 'w') as output_file:
            for k in range(timesteps):
                data = []
                #réécrit l'en-tête
                for i in range(9):
                    line = input_file.readline()
                    output_file.write(line)
                for i in range(nb_atoms):
                    data.append(input_file.readline().strip('\n').split())
                data = DataFrame(data)

            #  print(type(data.iloc[0,0]))
                data[0] = data[0].astype(int)
                data = data.sort_values(by=[0])
                data[0] = data[0].astype(str)
                data = np.array(data)
                
            #  print(data)
                for i in data:
                    output_file.write(' '.join(i)+'\n')
    return output_file
