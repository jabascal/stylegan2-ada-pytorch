import os
import json
import matplotlib.pyplot as plt
import seaborn as sns

def read_metrics_json_plot(json_file_path, output_path=None, xlabel=None, xvals=None):
    with open(json_file_path) as file:
        data = json.load(file)

    for metric_name, metric_vals in data.items():
        if metric_name == 'files':
            continue
        if xvals is None:
            xvals = range(len(metric_vals))            
        fig = plt.figure()
        '''
        plt.ylabel(metric_name)
        plt.plot(xvals, metric_vals)
        '''

        # Plot using seaborn
        sns.lineplot(x=xvals, y=metric_vals)
        plt.ylabel(metric_name)
        if xlabel is not None:
            plt.xlabel(xlabel)

        if output_path is not None:
            filename = os.path.basename(json_file_path).split('.')[0]
            filesave = os.path.join(output_path, f'{filename}_{metric_name}.png')
            fig.savefig(filesave, bbox_inches='tight', dpi=300)
        

if __name__ == "__main__":
    #json_file_path = '/mnt/d/Results/stygan2-ada/cifar10/metrics/metrics_cifar10.json'
    #output_path = '/mnt/d/Results/stygan2-ada/cifar10/metrics'
    json_file_path = 'out/metrics_metfaces.json'
    output_path = '/mnt/d/Results/stygan2-ada/metfaces/metrics'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    xlabel = 'Iterations'
    xvals = [200, 400, 800, 1600, 2200]
    read_metrics_json_plot(json_file_path, output_path, xlabel, xvals) 