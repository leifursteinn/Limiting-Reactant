M = {'H': 1.00794, 'He' : 4.0026, 'Li' :  6.941, 'Be' : 9.0122, 'B' : 10.811, 'C' : 12.011, 'N': 14.0067, 'O' : 15.9994, 'F': 18.9984, 'Ne' : 20.1797, 'Na': 23.9898, 
     'Mg' : 24.3050, 'Al': 26.9815, 'Si' : 28.0855, 'P': 30.9738, 'S' : 32.066, 'Cl': 36.4530, 'Ar' : 39.948, 'K': 39.0983, 'Ca' : 40.087, 'Sc': 44.9559, 'Ti' : 47.88, 
     'V': 50.942, 'Cr' : 51.996, 'Mn': 54.938, 'Fe' : 55.847, 'Co': 58.933, 'Ni' : 58.69, 'Cu': 63.55, 'Zn' : 65.39, 'Ga': 69.72, 'Ge' : 72.59, 'As': 74.922, 'Se' : 79.96, 
     'Br': 79.904, 'Kr' : 84.80,'Rb': 85.47, 'Sr' : 87.62, 'Y': 88.906, 'Zr' : 91.22, 'Nb': 92.906, 'Mo' : 95.94, 'Tc': 98, 'Ru' : 101.07, 'Rh': 102.91, 'Pd' : 106.42, 
     'Ag': 107.87, 'Cd' : 112.41, 'In': 114.82, 'Sn' : 118.71, 'Sb': 121.75, 'Te' : 127.60, 'I': 126.90, 'Xe' : 131.29, 'Cs' : 132.91, 'La' : 138.91, 'Ce' : 140.12, 
     'Pr' : 140.91, 'Nd' : 144.24, 'Pm' : 145, 'Sm' : 150.36, 'Eu' : 151.96, 'Gd' : 157.25, 'Tb' : 158.92, 'Dy' : 162.5, 'Ho' : 164.93, 'Er' : 167.26, 'Tm' : 168.93, 
     'Yb' : 173.04, 'Lu' : 174.97, 'Hf' : 178.49, 'Ta': 180.95, 'W' : 183.85, 'Re': 186.21, 'Os' : 190.2, 'Ir': 192.22, 'Pt' : 195.08, 'Au': 196.97, 'Hg' : 200.59, 'Tl': 204.38, 
     'Pb' : 207.2, 'Bi': 208.98, 'Po' : 209, 'At': 210, 'Rn' : 222, 'Fr': 223, 'Ra' : 226.03, 'Ac': 117.03, 'Th' : 232.04, 'Pa': 231.04, 'U' : 238.03, 'Np': 237.05, 'Pu' : 244, 
     'Am': 243, 'Cm' : 247, 'Bk' : 247, 'Cf' : 251, 'Es': 252, 'Fm' : 257, 'Md': 258, 'No' : 259, 'Lr': 260, 'Rf' : 261, 'Db': 262, 'Sg' : 263 ,'Bh': 262} 

x = 1
y = 0
output = []
calculate = 0
molecules = int(input("How many molecules are in the original equation? "))
# Storing Forumalae

masses = []
masses_grams = []
final_masses = []


# AMU CALCULATION

for i in range(molecules):
    elements = int(input("How many different elements are in this molecule? H20 would be 2: "))
    masses_grams.append(float(input("How many grams of this molecule are present? ")))
    for i in range(elements):
        print("Example if you have 2 H atoms you say 2 H ")
        print("What is element number " + str(x) + "?")
        amount, inp = input().split()
        for i in range(int(amount)):
            output.append(inp)
        x+=1
        print(output)
    x = 1
    for i in range(len(output)):
        calculate += M[output[y]]
        y += 1
    y = 0
    masses.append(calculate)
print("Masses in this formula (amu)", masses)
for i in range(len(masses)):
    final_masses.append(masses_grams[y] / masses[y])
    y+=1

print("Mole amounts are printed in periodical order:", final_masses)


