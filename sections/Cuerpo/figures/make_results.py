import pandas as pd


path = '.'
save_path = 'algorithms_results'

# Read all results files in current subdirectories except final subdirectory
list_subfolders_with_paths = ['./Heart_Failure', './Mobile_Price', './Bank_Marketing', './Tanzania_Watter_Pump']
combined_results = []
for filename in list_subfolders_with_paths:
    combined_results.append(pd.read_csv(filename + '/results.csv'))

# Eliminate not interesting columns
for table in combined_results:
    table.drop(['Tree Size' ,'Training Size', 'Max. Values', 'N. Iters', 'N. Layers', 'N. Neurons', 'N. Trees'], axis=1, inplace=True)

# Read algorithms names
algorithms_names = combined_results[0]["Algorithms"].tolist()
for table in combined_results:
    table.drop('Algorithms', axis=1, inplace=True)

# Build results file for each algorithm
final_tables = []
i = 0
for algorithm in algorithms_names:
    algorithm_table = pd.DataFrame([], dtype=object)
    for combined_table in combined_results:
        new_row = combined_table.iloc[i]
        algorithm_table = algorithm_table.append(new_row, ignore_index=True)
        
    final_tables.append(algorithm_table)
    i += 1

# Append dataset name column
for table in final_tables:
    table.insert(0, 'Dataset', ['Heart Failure', 'Mobile Price', 'Bank Marketing', 'Tanzania Watter Pump'])

# Write tables to disk
i = 0
for algorithm in algorithms_names:
    final_tables[i].to_csv(save_path + '/' + algorithm + '_Results.csv', index=False)
    i += 1
