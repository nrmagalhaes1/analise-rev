import openpyxl, os

users = str(os.getlogin())
unidadeDeDisco = str(os.path.abspath(os.sep))

def recolherValorPhi(filename):
    path = rf'{filename}'
    wb_obj = openpyxl.load_workbook(path, data_only= True) 
    sheet_obj = wb_obj.active

    phi = []
    c=0
    for i in range(8, 22):
        cell_obj = sheet_obj.cell(row = i, column = 7) 
        phi.append(cell_obj.value)
        c += 1
        
    c=0
    for i in range(25, 48):
        cell_obj = sheet_obj.cell(row = i, column = 7) 
        phi.append(cell_obj.value)
        c += 1


    return phi

def recolherValorvolume(filename):
    path = rf'{filename}'
    wb_obj = openpyxl.load_workbook(path, data_only= True) 
    sheet_obj = wb_obj.active

    phi = []
    c=0
    for i in range(8, 22):
        cell_obj = sheet_obj.cell(row = i, column = 11)
        phi.append(cell_obj.value)
        c += 1
        
    c=0
    for i in range(25, 48):
        cell_obj = sheet_obj.cell(row = i, column = 11) 
        phi.append(cell_obj.value)
        c += 1

    return phi

def valor_total(filename):
    t= []
    path = rf'{filename}'
    wb_obj = openpyxl.load_workbook(path, data_only= True) 
    sheet_obj = wb_obj.active
    cell_obj = sheet_obj.cell(row = 7, column = 7) 
    t.append(cell_obj.value)
    cell_obj = sheet_obj.cell(row = 7, column = 11) 
    t.append(cell_obj.value)
    
    return t