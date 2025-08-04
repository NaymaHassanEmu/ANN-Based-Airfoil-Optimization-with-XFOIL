Manuscript Link: https://drive.google.com/file/d/1y9ej7HuEGkcN1u5myHpvQfycqxxVweps/view?usp=drive_link
Shape optimization of NACA0012 using ANN-based surrogate model. 
The “Hicks-Henne bump function” has been used to parameterise and deform the original shape according to design parameters. 
Sampling parameters are generated using quasi-random low-discrepancy sequences called “Sobol” sequences. 
Numerical simulations have been conducted using the potential flow-based panel method solver “XFOIL” to obtain lift and drag coefficients of deformed foil shapes. 
An ANN-based surrogate model has been trained to predict the lift-coefficient and drag-coefficient corresponding to design parameters. 
The Python library “scipy. optimise.minimize” has been used to optimise the surrogate model on the basis of objective functions to obtain optimal design parameters. 

