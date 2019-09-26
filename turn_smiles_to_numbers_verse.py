import pandas as pd
import numpy as np
atomicIndex = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
               'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19,
               'Ca': 20, 'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, 'Ni': 28,
               'Cu': 29, 'Zn': 30, 'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35, 'Kr': 36, 'Rb': 37,
               'Sr': 38, 'Y': 39, 'Zr': 40, 'Nb': 41, 'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45, 'Pd': 46,
               'Ag': 47, 'Cd': 48, 'In': 49, 'Sn': 50, 'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54, 'Cs': 55,
               'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60, 'Pm': 61, 'Sm': 62, 'Eu': 63, 'Gd': 64,
               'Tb': 65, 'Ty': 66, 'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70, 'Lu': 71, 'Hf': 72, 'Ta': 73,
               'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79, 'Hg': 80, 'Tl': 81, 'Pb': 82,
               'Bi': 83, 'Po': 84, 'At': 85, 'Rn': 86, 'Fr': 87, 'Ra': 88, 'Ac': 89, 'Th': 90, 'Pa': 91,
               'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95, 'Cm': 96, 'Bk': 97, 'Cf': 98, 'Es': 99, 'Fm': 100,
               'Md': 101, 'No': 102, 'Lr': 103, 'Rf': 104, 'Db': 105, 'Sg': 106, 'Bh': 107, 'Hs': 108,
               'Mt': 109, 'Ds': 110, 'Rg': 111, 'Cn': 112, 'Nh': 113, 'Fl': 114, 'Mc': 115, 'Lv': 116,
               'Ts': 117, 'Og': 118, 'c': 119, 'o': 120, 'n': 121, 's': 122,
               '=': 123, '#': 124, '@': 125, '(': 126, ')': 127, '[': 128, ']': 129, '+': 130, '-': 139,
               '0': 140, '1': 141, '2': 142, '3': 143, '4': 144, '5': 145, '6': 146, '7': 147, '8': 148, '9': 149,
               '10': 150, '11': 151, '12': 152, '13': 153, '14': 154, '15': 155, '16': 156, '17': 157, '18': 158,
               '19': 159, '20': 160}


def get_key(dic, value):
    return [k for k, v in dic.items() if v == value]


def get_value(dic, key):
    return [v for k, v in dic.items() if k == key]


smiles = pd.read_csv('YOYO.csv', header=None).values
smiles_v = smiles[:, ::-1]

smiles_vector = np.zeros((smiles.shape[0], 50), dtype='float32')

for i in range(smiles.shape[0]):
    # split the string of smiles
    smiles_split = list(str(smiles_v[i]))[2:-2]
    for j in range(len(smiles_split)):
        smiles_vector[i, j] = float(str(get_value(atomicIndex, smiles_split[j])).strip("[]"))

print(smiles_vector)
pd.DataFrame(smiles_vector).to_csv('smiles_v_YOYO.csv', header=None, index=None)
