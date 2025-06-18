import ijson

file_path = fr'C:\Users\karthim\Downloads\json\Travis-protaxExport-20240419.json'

output_file = 'propertyCharacteristics_Travis.txt'

with open(file_path, 'r') as file, open(output_file, 'w') as output:
    output.write('pID|marketArea|dba|altDBA|condoPct|condoUnit|irrigationAcres|irrigationCapacity|irrigationGPM|irrigationWells|region|roadAccess|topography|sicCd|useCd|utilities|subType|subset|view|zoning|openBusinessDate\n')
    parser = ijson.items(file, 'item')
    for item in parser:
        propertyCharacteristics = item.get('propertyCharacteristics', [])
        for propertyCharacteristics in propertyCharacteristics:
            pID = propertyCharacteristics.get('pID')
            marketArea = propertyCharacteristics.get('marketArea')
            dba = propertyCharacteristics.get('dba')
            altDBA = propertyCharacteristics.get('altDBA')
            condoPct = propertyCharacteristics.get('condoPct')
            condoUnit = propertyCharacteristics.get('condoUnit')
            irrigationAcres = propertyCharacteristics.get('irrigationAcres')
            irrigationCapacity = propertyCharacteristics.get('irrigationCapacity')
            irrigationGPM = propertyCharacteristics.get('irrigationGPM')
            irrigationWells = propertyCharacteristics.get('irrigationWells')
            region = propertyCharacteristics.get('region')
            roadAccess = propertyCharacteristics.get('roadAccess')
            topography = propertyCharacteristics.get('topography')
            sicCd = propertyCharacteristics.get('sicCd')
            useCd = propertyCharacteristics.get('useCd')
            utilities = propertyCharacteristics.get('utilities')
            subType = propertyCharacteristics.get('subType')
            subset = propertyCharacteristics.get('subset')
            view = propertyCharacteristics.get('view')
            zoning = propertyCharacteristics.get('zoning')
            openBusinessDate = propertyCharacteristics.get('openBusinessDate')

            print(f'{pID}|{marketArea}|{dba}|{altDBA}|{condoPct}|{condoUnit}|{irrigationAcres}|{irrigationCapacity}|{irrigationGPM}|{irrigationWells}|{region}|{roadAccess}|{topography}|{sicCd}|{useCd}|{utilities}|{subType}|{subset}|{view}|{zoning}|{openBusinessDate}\n')
            output.write(f'{pID}|{marketArea}|{dba}|{altDBA}|{condoPct}|{condoUnit}|{irrigationAcres}|{irrigationCapacity}|{irrigationGPM}|{irrigationWells}|{region}|{roadAccess}|{topography}|{sicCd}|{useCd}|{utilities}|{subType}|{subset}|{view}|{zoning}|{openBusinessDate}\n')