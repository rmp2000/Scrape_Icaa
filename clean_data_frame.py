import numpy as np

def clean_dataframe(df):
    def clean_cell(cell):
        if isinstance(cell, list):
            if len(cell) == 0:
                return np.nan
            elif len(cell) == 1:
                return cell[0]
            else:
                return cell  # Mantener las listas con múltiples elementos
        else:
            return cell
    
    return df.applymap(clean_cell)