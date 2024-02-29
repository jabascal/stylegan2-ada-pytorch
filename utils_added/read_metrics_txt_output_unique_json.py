import json
import os
import re

def read_metrics_output_json(path_files, path_output, name_output, iter_files, pattern):
    # Get a list of all txt files in the directory
    #txt_files = glob.glob(os.path-.join(path_files, "*.txt"))
    metrics_names = ["fid50k_full", "kid50k_full", "is50k_mean", "is50k_std", 
                        #"pr50k3_full_precision", "pr50k3_full_recall",
                     "pr50k3_precision", "pr50k3_recall",
                     ]  
    metrics = {metric_name: [] for metric_name in metrics_names}
    metrics['files'] = path_files

    # Iterate over each txt file
    for file in path_files:
        with open(file, "r") as f:
            # Read the contents of the file
            print(f"Reading file: {file}")
            file_contents = f.read()

            # Find all matches
            matches = re.findall(pattern, file_contents, re.DOTALL)

            # Parse the JSON data
            for match in matches:
                data = json.loads(match)        
                results = data.get("results")
                for key in list(results.keys()):
                    for metric_name in metrics_names:
                        if key == metric_name:
                            metrics[metric_name].append(results[metric_name])    

    # Save the metrics to a json file
    with open(os.path.join(path_output, name_output), "w") as f:
        json.dump(metrics, f, indent=4)

if __name__ == "__main__":
    path_files = 'out'
    path_output = 'out'
    name_data = 'metfaces_256_tffreeze4'
    name_output = f'metrics_{name_data}.json'
    #name_output = 'metrics_metfaces.json'
    iter_files = [200, 400, 600]
    path_files = [os.path.join(path_files, f"out_metrics_{name_data}_{i}.txt") for i in iter_files]

    # Pattern to match
    pattern = r'\{"results":.*?\n'

    read_metrics_output_json(path_files, path_output, name_output, iter_files, pattern)
    