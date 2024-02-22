import json
import os
import re

def read_metrics_from_eval_outputs(path_files, path_output, name_output, iter_files, pattern):
    # Get a list of all txt files in the directory
    #txt_files = glob.glob(os.path-.join(path_files, "*.txt"))
    txt_files = [os.path.join(path_files, f"out_metrics_cifar10_{i}.txt") for i in iter_files]

    metrics_names = ["fid50k_full", "kid50k_full", "pr50k3_full_precision", "pr50k3_full_recall"]  
    metrics_names_short = ["fid", "kid", "precision", "recall"]
    metrics = {metric_name: [] for metric_name in metrics_names}
    metrics['files'] = txt_files

    # Iterate over each txt file
    for file in txt_files:
        with open(file, "r") as f:
            # Read the contents of the file
            file_contents = f.read()

            # Find all matches
            matches = re.findall(pattern, file_contents, re.DOTALL)

            # Parse the JSON data
            for match in matches:
                data = json.loads(match)        
                results = data.get("results")
                for key in list(results.keys()):
                    for metric_name, metric_name_short in zip(metrics_names, metrics_names_short):
                        if key == metric_name:
                            metrics[metric_name].append(results[metric_name])    

    # Save the metrics to a json file
    with open(os.path.join(path_output, name_output), "w") as f:
        json.dump(metrics, f, indent=4)

if __name__ == "__main__":
    path_files = 'out'
    path_output = 'out'
    name_output = 'metrics_cifar10.json'
    iter_files = [200, 400, 800, 1400]

    # Pattern to match
    pattern = r'\{"results":.*?\n\n'

    read_metrics_from_eval_outputs(path_files, path_output, name_output, iter_files, pattern)
    