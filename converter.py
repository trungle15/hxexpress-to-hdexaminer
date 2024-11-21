import pandas as pd
import os
import glob
import math

# Define the function to process the Excel files
def process_excel_files(input_directory, output_csv):
    master_data = []

    # Get all Excel files in the input directory
    all_files = glob.glob(os.path.join(input_directory, "*.xlsx"))

    for file in all_files:
        # Load the Excel file
        xls = pd.ExcelFile(file)
        
        # Read the summary sheet
        summary_df = pd.read_excel(xls, sheet_name='Summary')
        
        # Extract timepoints and # Deut values from the summary sheet
        timepoints = summary_df.iloc[1:, 0].tolist()  # Column 'time (min)'
        deut_values = summary_df.iloc[1:, 2].tolist()  # Column 'Rel D Lvl (Da)'

        for timepoint, num_deut in zip(timepoints, deut_values):
            # Convert timepoint to the appropriate format
            if timepoint == 0.0:
                deut_time = "0 sec"
            elif 0.0 < timepoint < 1.0:
                deut_time = "20 sec"
            elif 1.0 <= timepoint < 6.0:
                deut_time = f"{int(math.floor(timepoint))} min"
            elif 6.0 <= timepoint < 11.0:
                deut_time = "10 min"
            elif 11.0 <= timepoint < 30.0:
                deut_time = "20 min"
            elif 30.0 <= timepoint < 60.0:
                deut_time = "30 min"
            elif 60.0 <= timepoint < 240.0:
                deut_time = "1 hour"
            else:
                deut_time = "3 hour"
                

            # Create dummy data and extract required values
            row_data = {
                "Protein State": "Dummy Protein State",
                "Deut Time": deut_time,
                "Experiment": file,
                "Start": 1,  # Dummy Start
                "End": 10,   # Dummy End
                "Sequence": "Dummy Sequence",
                "Charge": 1,  # Dummy Charge
                "Search RT": 1.23,  # Dummy Search RT
                "# Deut": num_deut,
                "Deut %": 50.0,  # Dummy Deut %
            }
            master_data.append(row_data)

    # Convert master data list to DataFrame and save as CSV
    master_df = pd.DataFrame(master_data)
    master_df.to_csv(output_csv, index=False)

# Run the script
input_directory = "input_dir"  # Update with the actual path
output_csv = "master.csv"     # Update with the desired output path
process_excel_files(input_directory, output_csv)
print(f"Master CSV file saved at: {output_csv}")
