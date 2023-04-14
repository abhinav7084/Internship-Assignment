import pandas as pd
import xlrd


input_sheet1 = pd.read_table(r"https://docs.google.com/spreadsheets/d/1r1M9SSAtnbxEB7EvanhsCDBCHMw6UiJnCTwy4BX2GMU/edit?usp=sharing")
input_sheet2 = pd.read_table(r"https://docs.google.com/spreadsheets/d/1wGzscNbSpp66IXkgh-RR-mHBLzDHtxUcmjX9h7q_Awk/edit?usp=sharing")


input_fields = ["Name", "Team Name", "User ID"]
output_fields = ["Output1", "Output2", "Output3"]


output_sheet1 = pd.DataFrame(columns=output_fields)
output_sheet2 = pd.DataFrame(columns=output_fields)


for i in range(len(input_sheet1)):
    input_row1 = input_sheet1.iloc[i]
    input_row2 = input_sheet2.iloc[i]
    
    output_row1 = {}
    output_row2 = {}
    
    # output_row1["Output1"] = input_row1["S No"] + input_row2["S No"]
    output_row1["Output1"] = input_row1["Name"] * input_row2["Name"]
    output_row1["Output2"] = input_row1["Team Name"] - input_row2["Team Name"]
    output_row1["Output3"] = input_row1["User ID"] + input_row2["User ID"]
    
    # output_row2["Output1"] = input_row1["S No"] - input_row2["S No"]
    output_row2["Output1"] = input_row1["Name"] / input_row2["Name"]
    output_row2["Output2"] = input_row1["Team Name"] * input_row2["Team Name"]
    output_row2["Output3"] = input_row1["User ID"] - input_row2["User ID"]
    
    output_sheet1 = output_sheet1.append(output_row1, ignore_index=True)
    output_sheet2 = output_sheet2.append(output_row2, ignore_index=True)


output_sheet1.to_excel("https://docs.google.com/spreadsheets/d/1juau2TN6rTjl-ndkm-FaGQsscisSY10ugxCvYSGRepY/edit?usp=sharing", index=False)
output_sheet2.to_excel("https://docs.google.com/spreadsheets/d/12JmTbAkRhVKBw5_u2kV7GSv-fc7C1UqNW6ACqgxOgf8/edit?usp=sharing", index=False)