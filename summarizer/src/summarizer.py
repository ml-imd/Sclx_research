import numpy as np
import pandas as pd
from ntpath import split, basename
import matplotlib.pyplot as plt
import json
import sys


def string_to_list(list_str, separator=',', delimiter='[]'):
    return list_str.strip(delimiter).split(separator)


def file_name_from_path(path):
    head, tail = split(path)
    filename = tail or basename(head)

    if "." in filename:
        i = -1
        while(filename[i] != '.'):
            i -= 1
        filename = filename[:i]

    return filename


def sort_programs_dict(cluster_dict, sort_by="A1/A2/A3/A4"):
    for program in cluster_dict:
        cluster_dict[program] = dict(sorted(
            cluster_dict[program].items(), key=lambda item: item[1][sort_by], reverse=True))
    return cluster_dict


def count_qualis_occurances_for_programs(src):
    dataframe = pd.read_csv(src)
    cluster_dict = {}
    programs_list = []

    for i in dataframe.index:
        qualis = dataframe["qualis"][i]
        cluster = dataframe["Cluster"][i]
        programs_list = string_to_list(
            dataframe["programas"][i], separator='-')
        for program in programs_list:
            if cluster not in cluster_dict:
                cluster_dict[cluster] = {}
            if program not in cluster_dict[cluster]:
                cluster_dict[cluster][program] = {"A1": 0,
                                                  "A2": 0,
                                                  "A3": 0,
                                                  "A4": 0,
                                                  "B1": 0,
                                                  "B2": 0,
                                                  "B3": 0,
                                                  "B4": 0,
                                                  "C/NI/NP": 0,
                                                  "A1/A2/A3/A4": 0,
                                                  "B1/B2/B3/B4": 0,
                                                  "total": 0}

            cluster_dict[cluster][program][qualis] += 1
            cluster_dict[cluster][program]["total"] += 1
            if qualis in ("A1", "A2", "A3", "A4"):
                cluster_dict[cluster][program]["A1/A2/A3/A4"] += 1
            elif qualis in ("B1", "B2", "B3", "B4"):
                cluster_dict[cluster][program]["B1/B2/B3/B4"] += 1

    return sort_programs_dict(cluster_dict)


def dict_to_json(filename, dictionary):
    json_dict = json.dumps(dictionary)

    with open(filename, "w") as file:
        file.write(json_dict)


def dict_from_json(src):
    with open(src) as json_file:
        dictionary = json.load(json_file)

        return dictionary


def make_dict(csv_file, cluster_list=None):
    cluster_dict = count_qualis_occurances_for_programs(csv_file)
    selected_clusters = cluster_dict

    if cluster_list is not None:
        selected_clusters = string_to_list(cluster_list, separator='-')

    filename = "../results/" + file_name_from_path(csv_file) + ".json"
    dict_to_json(filename, {key: value for key, value in cluster_dict.items() if key in selected_clusters})


def make_values_dict_from_keys(dictionary, keys):
    values_dict = {k: [] for k in keys}
    
    for key in dictionary:
        for value in values_dict:
            values_dict[value].append(dictionary[key][value])

    return values_dict


def plot_program(dict_src, program_code_list_str, cluster, image_name=None):
    program_code_list = string_to_list(program_code_list_str, separator="-")
    subdict = {key: value for key, value in dict_from_json(
        dict_src)[cluster].items() if key in program_code_list}
    count_dict = make_values_dict_from_keys(subdict, ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C/NI/NP"])

    fig, ax = plt.subplots()
    x = np.arange(len(program_code_list))
    bar_width = 0.08
    multiplier = 0
    colors = ["#54c73a", "#abd216", "#ccce0f", "#f0f200",
              "#ffce00", "#ff9a00", "#ff6700", "#ff3300", "#ff0000"]

    for qualis in count_dict:
        ax.bar(x + bar_width * multiplier, count_dict[qualis], width=bar_width, label=qualis,
               color=colors[multiplier])
        multiplier += 1

    ax.set_xticks(x + 4 * bar_width)
    ax.set_xticklabels(program_code_list)
    ax.legend()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#DDDDDD')
    ax.set_title('Produções por programa')

    fig.tight_layout()

    if image_name is None:
        image_name = "../results/" + file_name_from_path(
            dict_src) + "_" + program_code_list_str + ".png"
    fig.savefig(image_name)

def plot_n_best(dict_src, n_str, cluster, compare_to=None, image_name=None):
    n = int(n_str)
    program_code_list_str = "["
    count = 0

    for program in dict_from_json(dict_src)[cluster]:
        if count == n:
            break

        if count != n-1:
            program_code_list_str += program + '-'
        else:
            program_code_list_str += program 
            if compare_to is not None:
                program_code_list_str += '-' + compare_to + ']'
            else:
                program_code_list_str += ']'

        count += 1

    plot_program(dict_src, program_code_list_str, cluster, image_name)

def plot_compare(dict_src, program_code_list_str, cluster, image_name=None):
    program_code_list = string_to_list(program_code_list_str, separator="-")
    subdict = {key: value for key, value in dict_from_json(
        dict_src)[cluster].items() if key in program_code_list}
    count_dict = make_values_dict_from_keys(subdict, ["A1/A2/A3/A4", "B1/B2/B3/B4", "C/NI/NP"])

    fig, ax = plt.subplots()
    x = np.arange(len(program_code_list))
    bar_width = 0.15
    multiplier = 0
    colors = ["#d6af36", "#a7a7ad", "#a77044"]

    for rank in count_dict:
        ax.bar(x + bar_width * multiplier, count_dict[rank], width=bar_width, label=rank,
               color=colors[multiplier])
        multiplier += 1

    ax.set_xticks(x + bar_width)
    ax.set_xticklabels(program_code_list)
    ax.legend()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#DDDDDD')
    ax.set_title('Comparação entre programas')

    fig.tight_layout()

    if image_name is None:
        image_name = "../results/" + file_name_from_path(
            dict_src) + "_" + program_code_list_str + "_compare_" + ".png"
    fig.savefig(image_name)

def plot_program_cluster(dict_src, program, image_name=None):
    dictionary = dict_from_json(dict_src)
    subdict = {key: dictionary[key][program] for key in dictionary if program in dictionary[key]}
    count_dict = make_values_dict_from_keys(subdict, ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C/NI/NP"])

    fig, ax = plt.subplots()
    x = np.arange(len(subdict))
    bar_width = 0.08
    multiplier = 0
    colors = ["#54c73a", "#abd216", "#ccce0f", "#f0f200",
              "#ffce00", "#ff9a00", "#ff6700", "#ff3300", "#ff0000"]

    for qualis in count_dict:
        ax.bar(x + bar_width * multiplier, count_dict[qualis], width=bar_width, label=qualis,
               color=colors[multiplier])
        multiplier += 1

    ax.set_xticks(x + 4 * bar_width)
    ax.set_xticklabels(subdict.keys())
    ax.legend()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#DDDDDD')
    ax.set_title('Porcentagem de publicações por grupo')

    fig.tight_layout()

    if image_name is None:
        image_name = "../results/" + file_name_from_path(
            dict_src) + "_" + program + '_' + ".png"
    fig.savefig(image_name)

#make_dict("../datasets/Particao_k3_c1.csv")
#plot_n_best("../results/Particao_k3_c1.json", 3, "cluster1", "23001011030P1")
#plot_compare("../results/Particao_k3_c1.json", "[23001011010P0-23001011031P8-23001011020P6]", "cluster1")
plot_program_cluster("../results/Particao_k3_c1.json", "23001011010P0")