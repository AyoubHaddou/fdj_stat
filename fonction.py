import pandas as pd 

def count_number(x,y):
    count = 0 
    for i in range(len(x['Numero'])):
        for j in x['Numero'][i][0:5]:
            if j == y :
                count += 1 
    return count


def count_number_chance(x,y):
    count = 0 
    for i in range(len(x['Numero'])):
        for j in x['Numero'][i][5:]:
            if j == y :
                count += 1 
    return count

def count_tenth(x) :
    unit = 0 
    ten = 0 
    twenty = 0 
    thirty = 0
    forty = 0 
    line_start = 0 
    line_end = 1
    len_df = len(x) 
    liste = {'Unité' : unit, 'Dizaine' : ten, 'Vingtaine' : twenty, 'Trentaine' : thirty, 'Quarantaine' : forty}

    while len_df >= line_end :
        for i in x.iloc[line_start:line_end,:5].values:
            for j in i :
                if j < 10 :
                    liste['Unité'] +=1 
                elif 10 <= j < 20:
                    liste['Dizaine'] +=1  
                elif 20 <= j < 30:
                    liste['Vingtaine']  += 1 
                elif 30 <= j < 40 :
                    liste['Trentaine'] += 1 
                elif 40 <= j < 50:
                    liste['Quarantaine'] += 1 
        line_start += 1 
        line_end += 1 
    return liste
    

def count_tenth_by_line(x,y):
    unit = 0 
    ten = 0 
    twenty = 0 
    thirty = 0 
    forty = 0 
    line_start = y-1 
    line_end = y
    len_df = len(x) 
    liste = {'Unité' : unit, 'Dizaine' : ten, 'Vingtaine' : twenty, 'Trentaine' : thirty, 'Quarantaine' : forty}

    for i in x.iloc[line_start:line_end,:4].values:
            for j in i :
                if j < 10 :
                    liste['Unité'] +=1 
                elif 10 <= j < 20:
                    liste['Dizaine'] +=1  
                elif 20 <= j < 30:
                    liste['Vingtaine']  += 1 
                elif 30 <= j < 40 :
                    liste['Trentaine'] += 1 
                elif 40 <= j < 50:
                    liste['Quarantaine'] += 1 
    return liste

def mask_search_5(x,y):
    mask = pd.Series(False, index=x.index)
    mask |= x[0].isin([y]) 
    mask |= x[1].isin([y])
    mask |= x[2].isin([y])
    mask |= x[3].isin([y])
    mask |= x[4].isin([y])
    return x[mask]

def mask_search_1(x,y):
    mask = pd.Series(True, index=x.index)
    mask &= x[5].isin([y]) 
    return x[mask]

def mask_all(x,y):
    mask = pd.Series(True, index=x.index)
    mask = pd.Series(False, index=x.index)
    mask |= x[0].isin([y]) 
    mask |= x[1].isin([y])
    mask |= x[2].isin([y])
    mask |= x[3].isin([y])
    mask |= x[4].isin([y])
    mask |= x[5].isin([y])
    return x[mask]

def gen_loto (x):
    liste = []
    liste.append([i for i in x[10:15]])
    return liste


# Test avec le meme fichier en Json importé pour des test 
# db_test = pd.read_json('Loto2.json',orient='records', encoding='utf-8')
# cursor_test = list(db.find({},{'_id':0}))