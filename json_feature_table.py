import ijson

file_path = fr"\\sanserver\PFBA Fileserver\Software Engineering\Taxroll_Data\Team Details\backup night shift\karthi\consolidation\json\Denton-protaxExport-20250414.json"
output_file = 'feature.txt'

with open(file_path, 'r') as file, open(output_file, 'w', encoding='utf-8') as output:
    output.write('pID|sortFeatureName|sortFeatureCode|featureName\n')
    parser = ijson.items(file, 'item')
    output_lines = []

    for item in parser:
        valuations = item.get('valuations', [])
        for valuation in valuations:
            pid1 = valuation.get('pID', 'N/A')
            details = valuation.get('details', {})
            cost_local = details.get('cost-local', {})
            improvements = cost_local.get('improvements', [])
            for i in improvements:
                details_list = i.get('details', [])
                for detail in details_list:
                    features = detail.get('features', [])
                    for k in features:
                        sortFeatureName = k.get('sortFeatureName', 'N/A')
                        sortFeatureCode = k.get('sortFeatureCode', 'N/A')
                        featureName = k.get('featureName', 'N/A')

                        output_lines.append(f'{pid1}|{sortFeatureName}|{sortFeatureCode}|{featureName}\n')
                        print(f'{pid1}--{sortFeatureName}--{sortFeatureCode}--{featureName}')

    output.writelines(output_lines)
