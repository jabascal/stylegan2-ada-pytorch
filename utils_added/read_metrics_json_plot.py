import os
import json
import matplotlib.pyplot as plt
import seaborn as sns

def read_metric_json(json_file_path, metric_name=None):
    with open(json_file_path) as f:
        data = json.load(f)
    if 'files' in data:
        iters = [int(file.split('_')[-1].split('.')[0]) for file in data['files']]
    if metric_name is not None:        
        metric = data[metric_name]
    return metric, iters

def read_metrics_json_plots(json_file_path, outfile_path=None, xlabel=None, xvals=None):
    with open(json_file_path) as file:
        data = json.load(file)

    if xvals is None:
        files = data.get('files')
        xvals = [int(file.split('_')[-1].split('.')[0]) for file in files]
    if xvals is None:
        xvals = range(len(metric_vals))            
    
    for metric_name, metric_vals in data.items():
        if metric_name == 'files':
            continue
        fig = plt.figure()
        sns.lineplot(x=xvals, y=metric_vals)
        plt.ylabel(metric_name)
        if xlabel is not None:
            plt.xlabel(xlabel)

        if outfile_path is not None:
            filesave = f'{outfile_path}_{metric_name}.png'
            fig.savefig(filesave, bbox_inches='tight', dpi=300)
        

if __name__ == "__main__":
    #json_file_path = '/mnt/d/Results/stygan2-ada/cifar10/metrics/metrics_cifar10.json'
    #output_path = '/mnt/d/Results/stygan2-ada/cifar10/metrics'
    name_data = 'dtd_32_rc10'
    name_out_specs = '' #'_rc10'
    json_file_path = f'out/metrics_{name_data}.json'
    output_path = f'/mnt/d/Results/stygan2-ada/{name_data}/metrics/'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    outfile_path = os.path.join(output_path, f'metrics_{name_data}_{name_out_specs}')
    xlabel = 'Iterations'
    xvals = [200, 400, 800, 1400, 2000]
    read_metrics_json_plots(json_file_path, outfile_path, xlabel, xvals) 