# Meca-ML 

> Dialogue between molecular dynamics and continuous media: definition of a cohesive model based on atomic scale information. A SIMAP's Project. 

Molecular dynamics calculus are made with **Lammps**.
The Machine Learning part will be done with **Python**. 

### Folder's explanation

- **avg_yy_strain-vs-separation :** scripts to plot the average yy strain versus separation for a crack. Needs a `dump.file` as a file entry. 
- **fy-vs-i_atoms :** scripts to plot fy values versus the id atoms. Used to watch the force values repartition. 
- **pyy-vs-ly :** scripts to plot pyy (average pressure along the y axis) values versus ly (box elongation along the y axis) values. Values are extracted from a `log.lammps` file.
- **rapport :** folder that contains all the files to write my internship report.