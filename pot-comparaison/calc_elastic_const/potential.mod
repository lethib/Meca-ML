# NOTE: This script can be modified for different pair styles 
# See in.elastic for more info.

reset_timestep 0

# Choose potential
variable        A_AlAl equal 0.0029
variable        C_AlAl equal 14.0498
variable        r_AlAl equal 0.068
variable        s_AlAl equal 1.5704

variable        A_AlO  equal 0.0075*(1+0.1*(0))
variable        C_AlO  equal 34.5747*$(1+0.1*(-4))
variable        r_AlO  equal 0.164*(1+0.01*3)
variable        s_AlO  equal 2.6067

variable        A_OO equal 0.011968181
variable        C_OO equal 85.08402081
variable        r_OO equal 0.263*(1+0.01*6)
variable        s_OO equal 3.643

kspace_style 	ewald 1.0e-4

pair_style      born/coul/long 11.6
pair_coeff	1 1 ${A_AlAl} ${r_AlAl}  ${s_AlAl}  ${C_AlAl}   0.
pair_coeff	1 2 ${A_AlO}  ${r_AlO}  ${s_AlO}  ${C_AlO}   0.
pair_coeff	2 2 ${A_OO}   ${r_OO}  ${s_OO}  ${C_OO}   0.

# Setup neighbor style
neighbor        0.3 bin 
neigh_modify    delay 10 

# Setup output

fix avp all ave/time  ${nevery} ${nrepeat} ${nfreq} c_thermo_press mode vector
thermo		${nthermo}
thermo_style custom step temp pe press f_avp[1] f_avp[2] f_avp[3] f_avp[4] f_avp[5] f_avp[6]
thermo_modify norm no

# Setup MD

timestep ${timestep}
fix 4 all nve
if "${thermostat} == 1" then &
   "fix 5 all langevin ${temp} ${temp} ${tdamp} ${seed}"


