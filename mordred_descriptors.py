#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 16:32:59 2021

@author: lucas
"""


import pandas as pd
import rdkit as rd
import argparse
from mordred import Calculator
from mordred import descriptors



############
## Read dataframe with compounds
###########

def calc_desc(mol_path):
    
    mol_array = pd.read_csv(mol_path, header=None)
    
    
    mol_array = mol_array.iloc[:,0].tolist()
    
    mol_array_mol = [rd.Chem.MolFromSmiles(m, sanitize=True) for m in mol_array]
    
    
    calc = Calculator(descriptors, ignore_3D=True)
    
    desc_mol_array = calc.pandas(mol_array_mol)
    #desc_act = desc_act.to_numpy()
    
    return desc_mol_array

def main():
    parser = argparse.ArgumentParser(description='')
        
    parser.add_argument('--i', type=str, required=True)
    parser.add_argument('--o', type=str, required=True)
    args = parser.parse_args()
    
    output = calc_desc(args.i)
    
    pd.DataFrame(output).to_csv(args.o)
    
if __name__=='__main__':
    main()