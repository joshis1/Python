'''

____  _
/ ___|| |__  _ __ ___ _   _  __ _ ___
\___ \| '_ \| '__/ _ \ | | |/ _` / __|
 ___) | | | | | |  __/ |_| | (_| \__ \
|____/|_| |_|_|  \___|\__, |\__,_|___/
                      |___/
'''

import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

from matplotlib.ticker import MaxNLocator
from matplotlib import ticker


def get_data_from_file(file):
    """

    :rtype: object
    """
    with open(file) as f:
        plot_list = csv.reader(f)
        csv_headings = next(plot_list)
        values = next(plot_list)
        zip_iterator = zip(csv_headings, values)
        return dict(zip_iterator)


def plot_normalized_bar_graph(label_val, plot_data, attrib_keys):
    X = np.arange(len(plot_data[0]))
    fig = plt.figure()
    colors = "rgyb0pbm"
    color_val = list(colors)
    space = 0
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xticks(np.linspace(0, 2.5, len(plot_data[0])))
    for index, label in enumerate(label_val):
        ax.bar(X + space, plot_data[index], color=color_val[index], width=0.25)
        space = space+0.25
    # save the figure
    labels = attrib_keys
    ax.legend(labels=label_val)
    ax.set_xticklabels(labels)
    plt.savefig('device_performance.png', dpi=300, bbox_inches='tight')


def get_labels(versions_data):
    labels_list = []
    for version_data in versions_data:
        labels_list.append(version_data['fw_version'])
    return labels_list


def get_attribute_keys_list(versions_data):
    test_name_keys = versions_data[0].keys()
    # print(test_name_keys)
    return list(test_name_keys)[1:]


def get_attributes_values_list(versions_data_list):
    final_data = []
    for version_data in versions_data_list:
        # Don't consider the fw version as attribute so slice with 1:
        test_list = list(version_data.values())[1:]
        # Unfortunately, all the fields are string so convert each of string to float.
        test_list = list(map(float, test_list))
        # Get a list of attribute values list.
        final_data.append(test_list)
    return final_data


def get_data_plot_normalized_values(final_attribute_data):
    normalized_values = []
    base_value = np.array(final_attribute_data[0])
    for value in final_attribute_data:
        # print(np.array(value) / base_value)
        normalized_values.append(list(np.array(value) / base_value))
    return normalized_values


if __name__ == "__main__":
    graph_list = []
    for i, arg in enumerate(sys.argv):
        if i > 0:
            attrib = get_data_from_file(sys.argv[i])
            graph_list.append(attrib)
    get_labels(graph_list)
    attrib_values = get_attributes_values_list(graph_list)
    # print(attrib_values)
    result_data = get_data_plot_normalized_values(attrib_values)
    attrib_keys = get_attribute_keys_list(graph_list)
    # print(attrib_keys)
    labels = get_labels(graph_list)
    plot_normalized_bar_graph(labels, result_data, attrib_keys)

