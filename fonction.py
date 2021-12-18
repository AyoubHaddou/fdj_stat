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

# Test avec le meme fichier en Json importé pour des test 
# db_test = pd.read_json('Loto2.json',orient='records', encoding='utf-8')
# cursor_test = list(db.find({},{'_id':0}))