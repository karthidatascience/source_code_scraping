import ijson

file_path = fr"\\sanserver\PFBA Fileserver\Software Engineering\Taxroll_Data\Team Details\backup night shift\karthi\consolidation\json\Travis-protaxExport-20250418.json"



with open(file_path, 'r') as file:
    parser = ijson.items(file, 'item')
    for i, item in enumerate(parser):
        if i == 1:
            print(item)
            break