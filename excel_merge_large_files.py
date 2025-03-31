import os
import pandas as pd

file_path = r"\\sanserver\PFBA Fileserver\Software Engineering\Taxroll_Data\Team Details\backup night shift\karthi\consolidation\3"
output_file = r"\\sanserver\PFBA Fileserver\Software Engineering\Taxroll_Data\Team Details\backup night shift\karthi\consolidation\3.txt"

chunk_size = 500000  # Reduce chunk size to optimize memory usage
header_written = False  # Track if header has been written

for file in os.listdir(file_path):
    if file.endswith('.csv'):
        print(f'Processing file: {file}')
        try:
            for chunk in pd.read_csv(os.path.join(file_path, file),
                                     dtype=str,
                                     low_memory=False,
                                     chunksize=chunk_size):
                chunk.to_csv(output_file, mode='a', index=False, header=not header_written)
                header_written = True  # After first write, set this to True
        except Exception as e:
            print(f"Error processing {file}: {e}")

print(f"Files successfully merged and saved as {output_file}")
