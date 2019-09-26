import pyparsing as pp
import pandas as pd
import csv
from keras.models import load_model

n = 208
index = n+1
amount = 1000
std = 5.0
original_smiles = pd.read_csv('./DataPool/select data/smiles_train_v.csv', index_col=None, header=None).values
original_smile = original_smiles[:, ::-1]
smiles = pd.read_csv(str(index) + '_maccs-smile_' + str(amount) + '(std='+str(std) + ').v3.csv', index_col=None, header=None).values
verse_smiles = smiles[:, ::-1]

unique = 0
unique_number = []
for i in range(amount):
    if i == 0 :
        unique += 1
        unique_number.append(i)
        # print(list(verse_smiles[i]))
    else :
        no = 0
        for j in range(len(unique_number)):
            # print('分子', i, '比較分子編號unique', j)
            if any(verse_smiles[i] != verse_smiles[unique_number[j]]) :
                no += 1
        if no == len(unique_number) :
            unique += 1
            unique_number.append(i)
            # print(list(verse_smiles[i]))




print('產生幾種分子:', unique)
print('每種分子只以最先出現的編號做代表:', unique_number)
print('----------')


unique_smiles = verse_smiles[unique_number]
recognizer = load_model('Recognizer200.h5')
recognition = recognizer.predict(unique_smiles)
with open ('./recognition/' + str(index) + '_maccs-smile_' + str(amount) + '(std='+str(std) + ')_recognition.v3.csv','w', newline='') as output:
    writer = csv.writer(output)
    writer.writerows(recognition)


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


def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]


with open('./smiles/' + str(index) + '_smiles(std=' + str(std) + ').csv', 'w', newline='') as output:
    writer = csv.writer(output)
    a = []
    for j in range(50):
        a.extend(get_key(atomicIndex, original_smile[n, j]))
    b = ''
    b = [b.join(a)]
    print('original ' + str(index) + ' smile:', b)
    print('--------------')
    for i in range(len(unique_smiles)):
        a = []
        for j in range(50):
            a.extend(get_key(atomicIndex, unique_smiles[i, j]))
        b = ''
        b = [b.join(a)]
        print(b)
        writer.writerow(b)

