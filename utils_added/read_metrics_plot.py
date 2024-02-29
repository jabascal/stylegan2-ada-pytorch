import os

from read_metrics_txt_output_unique_json import read_metrics_output_json
from read_metrics_json_plot import read_metrics_json_plots

path_files = 'out'
path_output = 'out'
name_data = 'dtd_256_selec_rc50_sub25k'
#name_out_specs = '_tf_FFHQ'
name_out_specs = ''
name_output = f'metrics_{name_data}.json'
#name_output = 'metrics_metfaces.json'
iter_files = [200, 400, 800, 1400, 2000]
path_files = [os.path.join(path_files, f"out_metrics_{name_data}_{i}.txt") for i in iter_files]

# Pattern to match
pattern = r'\{"results":.*?\n'

print(f"list out/: {os.listdir('out')}")

# Read metrics txt outputs and save to json
read_metrics_output_json(path_files, path_output, name_output, iter_files, pattern)

# Read metrics json and plot
json_file_path = os.path.join(path_output, name_output)
outfile_path = os.path.join(path_output, f'{name_data}{name_out_specs}')

xlabel = 'Iterations'
read_metrics_json_plots(json_file_path, outfile_path, xlabel, iter_files) 