# Meca-ML 

Dialogue between molecular dynamics and continuous media: definition of a cohesive model based on atomic scale information. A SIMAP's Project. 

## The Project

This internship is part of a multiscale analysis of fracture and more precisely by con- ducting a diaglogue in molecular dynamics and description in continuous medium. More precisely, the aim is to identify a cohesive zone model, representing the fracture mechanism at the continuous scale through a ”stress-vector” - ”opening” relation. This model will be identifiable following calculations in molecular dynamics which produce the numerical experiments.

An important part of the work is to conduct Molecular Dynamics simulations on a Silicon (Si) crystal for which the fracture occurs by cleavage. However, since Si has anisotropic elastic properties, it is expected that the fracture properties are also anisotropic. Therefore, simulations for different orientations between the crack plane and the crystalline symmetry planes will also have to be carried out. A systematic approach can be conducted. Nevertheless, the methodology associating Machine Learning and Molecular Dynamics is to be exploited in order to gain in calculation time.

Once the cohesive model is identified, it is then possible to study and predict the intercations between cracking and microstructure (in a polycrystal for example), as well as between crack and cavity.

It is a 100% digital project with a strong interest in simulation methods and Machine Learning.

## The state of the project

At this date (13/07/2022), the project is far from being finished. The approach taken those 10 first weeks was to determine a good set of parameters to have correct simulations. By reading the [internship report](rapport_V1.pdf), you will find all the methods used, results found and comments made. It would be nice to continue this project and maybe going a bit deeper on the [Machine-Learning Potential](pot-comparaison/pot-ML-w-less-atoms-V2/in.pot-ml) because results are good: 

- [ ] Check with Ovito **on multiple timesteps** to see if we have a fine cracking, without blunting during the propagation.
- [ ] If ok, run a tensile test
- [ ] If ok, run a tensile test with a crack at the side

If thoose steps still provides good results, the next step is to create a **database** in order to train a **Machine-Learning** algorithm as explain in the [report's appendices](rapport_V1.pdf). 

## GitLab repository explanation

All the explanations on the GitLab repository are provided in the [wiki of the project](https://gitlab.ensimag.fr/mrozt/meca-ml/-/wikis/home)