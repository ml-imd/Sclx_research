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


def sort_programs_dict(cluster_dict, sort_by):
    for program in cluster_dict:
        cluster_dict[program] = dict(sorted(
            cluster_dict[program].items(), key=lambda item: item[1][sort_by], reverse=True))
    return cluster_dict


def count_qualis_occurances_for_programs(src, sort_by):
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

    return sort_programs_dict(cluster_dict, sort_by)


def dict_to_json(filename, dictionary):
    json_dict = json.dumps(dictionary)

    with open(filename, "w") as file:
        file.write(json_dict)


def dict_from_json(src):
    with open(src) as json_file:
        dictionary = json.load(json_file)

        return dictionary


def make_dict(csv_file, cluster_list=None, sort_by="A1/A2/A3/A4"):
    cluster_dict = count_qualis_occurances_for_programs(csv_file, sort_by)
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

def label_bar(ax, bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

def plot(subdict, program_code_list, count_dict, title, image_name, template="program", comparing=False, auto_label=False):
    if template == "program":
        bar_width = 0.08
        colors = ["#54c73a", "#abd216", "#ccce0f", "#f0f200",
                  "#ffce00", "#ff9a00", "#ff6700", "#ff3300", "#ff0000"]
        tick_translate = 4
    elif template == "compare":
        bar_width = 0.15
        colors = ["#d6af36", "#a7a7ad", "#a77044"]
        tick_translate = 1
    
    fig, ax = plt.subplots()
    x = np.arange(len(program_code_list))
    multiplier = 0

    for key in count_dict:
        bar = ax.bar(x + bar_width * multiplier, count_dict[key], width=bar_width, label=key,
               color=colors[multiplier])
        if auto_label:
            label_bar(ax, bar)
        multiplier += 1

    ax.set_xticks(x + tick_translate * bar_width)
    ax.set_xticklabels(program_code_list)
    ax.legend(bbox_to_anchor=(1.04,0), loc="lower left")

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(left=False, bottom=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#DDDDDD')
    ax.set_title(title)

    if len(subdict) > 3:
        fig.autofmt_xdate()
    fig.tight_layout()

    if comparing:
        plt.gca().get_xticklabels()[-1].set_color('red') 

    fig.savefig(image_name)

def plot_program(dict_src, program_code_list_str, cluster, image_name=None, comparing=False):
    program_code_list = string_to_list(program_code_list_str, separator="-")
    subdict = {key: value for key, value in dict_from_json(
        dict_src)[cluster].items() if key in program_code_list}
    count_dict = make_values_dict_from_keys(subdict, ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C/NI/NP"])

    if image_name is None:
        image_name = "../results/" + file_name_from_path(
            dict_src) + "_" + program_code_list_str + ".png"

    plot(subdict, program_code_list, count_dict, "Produções por programa", image_name=image_name, comparing=comparing)

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
                comparing = True
                program_code_list_str += '-' + compare_to + ']'
            else:
                comparing = False
                program_code_list_str += ']'

        count += 1

    plot_program(dict_src, program_code_list_str, cluster, image_name=image_name, comparing=comparing)

def plot_compare(dict_src, program_code_list_str, cluster, image_name=None):
    program_code_list = string_to_list(program_code_list_str, separator="-")
    subdict = {key: value for key, value in dict_from_json(
        dict_src)[cluster].items() if key in program_code_list}
    count_dict = make_values_dict_from_keys(subdict, ["A1/A2/A3/A4", "B1/B2/B3/B4", "C/NI/NP"])

    if image_name is None:
        image_name = "../results/" + file_name_from_path(
            dict_src) + "_" + program_code_list_str + "_compare_" + ".png"
    
    plot(subdict, program_code_list, count_dict, "Comparação entre programas", image_name=image_name, template="compare")

def plot_program_cluster(dict_src, program, cluster_list_str=None, image_name=None):
    dictionary = dict_from_json(dict_src)
    
    if cluster_list_str is not None:
        selected_clusters = string_to_list(cluster_list_str, separator='-')
    else: 
        selected_clusters = dictionary
        
    subdict = {key: dictionary[key][program] for key in selected_clusters if program in dictionary[key]}
    count_dict = make_values_dict_from_keys(subdict, ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C/NI/NP"])

    if image_name is None:
        image_name = "../results/" + file_name_from_path(
            dict_src) + "_" + program + '_' + ".png"

    plot(subdict, subdict.keys(), count_dict, "Porcentagem de publicações por grupo", image_name=image_name, auto_label=True)

#make_dict("../datasets/Particoes.csv")
plot_n_best("../results/Particoes.json", 2, "cluster1", "23001011030P1")
plot_compare("../results/Particoes.json", "[23001011010P0-23001011031P8-23001011020P6]", "cluster1")
plot_program_cluster("../results/Particoes.json", "23001011010P0", "[cluster1-cluster2]")