import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import nan

df = pd.read_excel('foil.xlsx')
x = df['x']
y = df['y']

x = df['x'].values
y = df['y'].values

x = x[np.logical_not(np.isnan(x))]
y = y[np.logical_not(np.isnan(y))]


def hicks_henne_deform(x_coord, y_coord, n, a_coeffs, w_coeffs, xM_coeffs):
   
    y_deformed = np.array(y_coord)
    
    for i in range(n):
        wi = w_coeffs[i]
        ai = a_coeffs[i]
        xiMi = xM_coeffs[i]
        m = np.log(0.5) / np.log(xiMi)

        y_deformed += ai * np.sin(np.pi * np.array(x_coord) ** m )**wi

    
    return y_deformed


def plot_airfoil(x_c,y_c, title):
    plt.plot(x_c, y_c)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.grid()




# Define the Hicks-Henne coefficients for deformation
n = 11  # Number of sine terms (increase for more deformation)
a_coeffs = [0.03, -0.08, 0.05, -0.04, 0.03, -0.02, 0.01, -0.005, 0.003, -0.002, 0.001]  # Coefficients for the sine terms
w_coeffs = np.full(11,3)  # Frequencies for the sine terms
xM_coeffs = [0.35913372, 0.22967959, 0.12212521, 0.045184  , 0.00508928, 0.00508928, 0.045184  , 0.12212521, 0.22967959, 0.35913372, 0.5 ] # Reference points along the chord line

# Deform the airfoil using the Hicks-Henne function
y_mod = hicks_henne_deform(x, y, n, a_coeffs, w_coeffs, xM_coeffs)

df1 = pd.DataFrame({'x': x, 'y_modified': y_mod} )
path = "C:/Users/user/OneDrive - BUET/Desktop/Deform/Deformed_airfoil(1).xlsx" #give the path you want save the airfoil co-ordinates in
df1.to_excel(path, index=False)

# Plot the original and fully deformed airfoils
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plot_airfoil(x, y, 'Original Airfoil (NACA 0012)')
plt.subplot(1, 2, 2)
plot_airfoil(x, y_mod, 'Deformed Airfoil')
plt.tight_layout()

# Show the plot
plt.show()
