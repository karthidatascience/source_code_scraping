import pandas as pd
import numpy as np

df1=pd.read_excel(r'C:\Users\karthim\Downloads\comparisons\hilago\certi_hidalgo.xlsx')
df2=pd.read_excel(r'C:\Users\karthim\Downloads\comparisons\hilago\final_hidalgo.xlsx')
# print(df1)
df1 = df1.astype(str)
df2 = df2.astype(str)


result_data_combined = []  # Create an empty list to store the combined results

for i in range(0,360000):
    print(i)
    s1_value = df1['ptx_parcel_number'][i]

    # Check for assr_parcel_use_code
    found_rows_df2_assr = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_assr.empty:
        s2 = (df1['assr_parcel_use_code'][i] == found_rows_df2_assr['assr_parcel_use_code'].values[0])
        if not s2:
            s5 = found_rows_df2_assr['assr_parcel_use_code'].values[0] == 'nan'
            if s5:
                additional_info = f"assr_parcel_use_code"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['assr_parcel_use_code'][i], found_rows_df2_assr['assr_parcel_use_code'].values[0], additional_info])

    # Check for neighborhood
    found_rows_df2_neighborhood = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_neighborhood.empty:
        s2_neighborhood = (df1['neighborhood'][i] == found_rows_df2_neighborhood['neighborhood'].values[0])
        if not s2_neighborhood:
            s5_neighborhood = found_rows_df2_neighborhood['neighborhood'].values[0] == 'nan'
            if s5_neighborhood:
                additional_info = f"neighborhood"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['neighborhood'][i], found_rows_df2_neighborhood['neighborhood'].values[0], additional_info])

    found_rows_df2_assr_parcel_use = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_assr_parcel_use.empty:
        s2_assr_parcel_use = (df1['assr_parcel_use'][i] == found_rows_df2_assr_parcel_use['assr_parcel_use'].values[0])
        if not s2_assr_parcel_use:
            s5_assr_parcel_use = found_rows_df2_assr_parcel_use['assr_parcel_use'].values[0] == 'nan'
            if s5_assr_parcel_use:
                additional_info = f"assr_parcel_use"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['assr_parcel_use'][i], found_rows_df2_assr_parcel_use['assr_parcel_use'].values[0], additional_info])

    found_rows_df2_assr_parcel_class_code = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_assr_parcel_class_code.empty:
        s2_assr_parcel_class_code = (df1['assr_parcel_class_code'][i] == found_rows_df2_assr_parcel_class_code['assr_parcel_class_code'].values[0])
        if not s2_assr_parcel_class_code:
            s5_assr_parcel_class_code = found_rows_df2_assr_parcel_class_code['assr_parcel_class_code'].values[0] == 'nan'
            if s5_assr_parcel_class_code:
                additional_info = f"assr_parcel_class_code"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['assr_parcel_class_code'][i], found_rows_df2_assr_parcel_class_code['assr_parcel_class_code'].values[0], additional_info])

    found_rows_df2_assr_parcel_class = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_assr_parcel_class.empty:
        s2_assr_parcel_class = (df1['assr_parcel_class'][i] == found_rows_df2_assr_parcel_class['assr_parcel_class'].values[0])
        if not s2_assr_parcel_class:
            s5_assr_parcel_class = found_rows_df2_assr_parcel_class['assr_parcel_class'].values[0] == 'nan'
            if s5_assr_parcel_class:
                additional_info = f"assr_parcel_class"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['assr_parcel_class'][i], found_rows_df2_assr_parcel_class['assr_parcel_class'].values[0], additional_info])

    found_rows_df2_neighborhood_code = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_neighborhood_code.empty:
        s2_neighborhood_code = (df1['neighborhood_code'][i] == found_rows_df2_neighborhood_code['neighborhood_code'].values[0])
        if not s2_neighborhood_code:
            s5_neighborhood_code = found_rows_df2_neighborhood_code['neighborhood_code'].values[0] == 'nan'
            if s5_neighborhood_code:
                additional_info = f"neighborhood_code"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['neighborhood_code'][i], found_rows_df2_neighborhood_code['neighborhood_code'].values[0], additional_info])


    found_rows_df2_legal_description = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_legal_description.empty:
        s2_legal_description = (df1['legal_description'][i] == found_rows_df2_legal_description['legal_description'].values[0])
        if not s2_legal_description:
            s5_legal_description = found_rows_df2_legal_description['legal_description'].values[0] == 'nan'
            if s5_legal_description:
                additional_info = f"legal_description"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['legal_description'][i], found_rows_df2_legal_description['legal_description'].values[0], additional_info])


    found_rows_df2_owner_name_1 = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_owner_name_1.empty:
        s2_owner_name_1 = (df1['owner_name_1'][i] == found_rows_df2_owner_name_1['owner_name_1'].values[0])
        if not s2_owner_name_1:
            s5_owner_name_1 = found_rows_df2_owner_name_1['owner_name_1'].values[0] == 'nan'
            if s5_owner_name_1:
                additional_info = f"owner_name_1"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['owner_name_1'][i], found_rows_df2_owner_name_1['owner_name_1'].values[0], additional_info])

    found_rows_df2_location_description = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_location_description.empty:
        s2_location_description = (df1['location_description'][i] == found_rows_df2_location_description['location_description'].values[0])
        if not s2_location_description:
            s5_location_description = found_rows_df2_location_description['location_description'].values[0] == 'nan'
            if s5_location_description:
                additional_info = f"location_description"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['location_description'][i], found_rows_df2_location_description['location_description'].values[0], additional_info])

    found_rows_df2_improve_sq_ft = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_improve_sq_ft.empty:
        s2_improve_sq_ft = (df1['improve_sq_ft'][i] == found_rows_df2_improve_sq_ft['improve_sq_ft'].values[0])
        if not s2_improve_sq_ft:
            s5_improve_sq_ft = found_rows_df2_improve_sq_ft['improve_sq_ft'].values[0] == 'nan'
            if s5_improve_sq_ft:
                additional_info = f"improve_sq_ft"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['improve_sq_ft'][i], found_rows_df2_improve_sq_ft['improve_sq_ft'].values[0], additional_info])


    found_rows_df2_land_full_value = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_land_full_value.empty:
        s2_land_full_value = (df1['land_full_value'][i] == found_rows_df2_land_full_value['land_full_value'].values[0])
        if not s2_land_full_value:
            s5_land_full_value = found_rows_df2_land_full_value['land_full_value'].values[0] == '0'
            if s5_land_full_value:
                additional_info = f"land_full_value"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['land_full_value'][i], found_rows_df2_land_full_value['land_full_value'].values[0], additional_info])


    found_rows_df2_land_full_value = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_land_full_value.empty:
        s2_land_full_value = (df1['land_full_value'][i] == found_rows_df2_land_full_value['land_full_value'].values[0])
        if not s2_land_full_value:
            s5_land_full_value = found_rows_df2_land_full_value['land_full_value'].values[0] == '0'
            if s5_land_full_value:
                additional_info = f"land_full_value"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['land_full_value'][i], found_rows_df2_land_full_value['land_full_value'].values[0], additional_info])

    found_rows_df2_land_assessment = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_land_assessment.empty:
        s2_land_assessment = (df1['land_assessment'][i] == found_rows_df2_land_assessment['land_assessment'].values[0])
        if not s2_land_assessment:
            s5_land_assessment = found_rows_df2_land_assessment['land_assessment'].values[0] == '0'
            if s5_land_assessment:
                additional_info = f"land_assessment"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['land_assessment'][i], found_rows_df2_land_assessment['land_assessment'].values[0], additional_info])

    found_rows_df2_improve_full_value = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_improve_full_value.empty:
        s2_improve_full_value = (df1['improve_full_value'][i] == found_rows_df2_improve_full_value['improve_full_value'].values[0])
        if not s2_improve_full_value:
            s5_improve_full_value = found_rows_df2_improve_full_value['improve_full_value'].values[0] == '0'
            if s5_improve_full_value:
                additional_info = f"improve_full_value"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['improve_full_value'][i], found_rows_df2_improve_full_value['improve_full_value'].values[0], additional_info])

    found_rows_df2_improve_assessment = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_improve_assessment.empty:
        s2_improve_assessment = (df1['improve_assessment'][i] == found_rows_df2_improve_assessment['improve_assessment'].values[0])
        if not s2_improve_assessment:
            s5_improve_assessment = found_rows_df2_improve_assessment['improve_assessment'].values[0] == '0'
            if s5_improve_assessment:
                additional_info = f"improve_assessment"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['improve_assessment'][i], found_rows_df2_improve_assessment['improve_assessment'].values[0], additional_info])

    found_rows_df2_personal_full_value = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_personal_full_value.empty:
        s2_personal_full_value = (df1['personal_full_value'][i] == found_rows_df2_personal_full_value['personal_full_value'].values[0])
        if not s2_personal_full_value:
            s5_personal_full_value = found_rows_df2_personal_full_value['personal_full_value'].values[0] == '0'
            if s5_personal_full_value:
                additional_info = f"personal_full_value"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['personal_full_value'][i], found_rows_df2_personal_full_value['personal_full_value'].values[0], additional_info])

    found_rows_df2_personal_assessment = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_personal_assessment.empty:
        s2_personal_assessment = (df1['personal_assessment'][i] == found_rows_df2_personal_assessment['personal_assessment'].values[0])
        if not s2_personal_assessment:
            s5_personal_assessment = found_rows_df2_personal_assessment['personal_assessment'].values[0] == '0'
            if s5_personal_assessment:
                additional_info = f"personal_assessment"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['personal_assessment'][i], found_rows_df2_personal_assessment['personal_assessment'].values[0], additional_info])

    found_rows_df2_full_value_cap_adjustment = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_full_value_cap_adjustment.empty:
        s2_full_value_cap_adjustment = (df1['full_value_cap_adjustment'][i] == found_rows_df2_full_value_cap_adjustment['full_value_cap_adjustment'].values[0])
        if not s2_full_value_cap_adjustment:
            s5_full_value_cap_adjustment = found_rows_df2_full_value_cap_adjustment['full_value_cap_adjustment'].values[0] == '0'
            if s5_full_value_cap_adjustment:
                additional_info = f"full_value_cap_adjustment"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['full_value_cap_adjustment'][i], found_rows_df2_full_value_cap_adjustment['full_value_cap_adjustment'].values[0], additional_info])

    found_rows_df2_assessment_cap_adjustment = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_assessment_cap_adjustment.empty:
        s2_assessment_cap_adjustment = (df1['assessment_cap_adjustment'][i] == found_rows_df2_assessment_cap_adjustment['assessment_cap_adjustment'].values[0])
        if not s2_assessment_cap_adjustment:
            s5_assessment_cap_adjustment = found_rows_df2_assessment_cap_adjustment['assessment_cap_adjustment'].values[0] == '0'
            if s5_assessment_cap_adjustment:
                additional_info = f"assessment_cap_adjustment"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['assessment_cap_adjustment'][i], found_rows_df2_assessment_cap_adjustment['assessment_cap_adjustment'].values[0], additional_info])

    found_rows_df2_total_full_value = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_total_full_value.empty:
        s2_total_full_value = (df1['total_full_value'][i] == found_rows_df2_total_full_value['total_full_value'].values[0])
        if not s2_total_full_value:
            s5_total_full_value = found_rows_df2_total_full_value['total_full_value'].values[0] == '0'
            if s5_total_full_value:
                additional_info = f"total_full_value"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['total_full_value'][i], found_rows_df2_total_full_value['total_full_value'].values[0], additional_info])

    found_rows_df2_total_assessed_value = df2[df2['ptx_parcel_number'] == s1_value]
    if not found_rows_df2_total_assessed_value.empty:
        s2_total_assessed_value = (df1['total_assessed_value'][i] == found_rows_df2_total_assessed_value['total_assessed_value'].values[0])
        if not s2_total_assessed_value:
            s5_total_assessed_value = found_rows_df2_total_assessed_value['total_assessed_value'].values[0] == '0'
            if s5_total_assessed_value:
                additional_info = f"total_assessed_value"
                result_data_combined.append([df1['ptx_parcel_number'][i], df1['total_assessed_value'][i], found_rows_df2_total_assessed_value['total_assessed_value'].values[0], additional_info])


# Create a DataFrame for combined results
result_df_combined = pd.DataFrame(result_data_combined, columns=['ptx_parcel_number', 'value_df1', 'value_df2', 'additional_info'])

# Save the combined DataFrame to an Excel file
result_df_combined.to_excel('final_resultshidalgo.xlsx', index=False)

