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

def count_qualis_occurances_for_programs(src):
  dataframe = pd.read_csv(src)
  cluster_dict = {}
  programs_list = []

  for i in dataframe.index:
    qualis = dataframe["qualis"][i]
    cluster = dataframe["Cluster"][i]
    programs_list = string_to_list(dataframe["programas"][i], separator='-')
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
																					"total_A": 0,
																					"total_B": 0,
																					"total": 0}
      cluster_dict[cluster][program][qualis] += 1
			cluster_dict[cluster][program]["total"] += 1
			if qualis in ("A1", "A2", "A3", "A4"):
				cluster_dict[cluster][program]["total_A"] += 1
			elif qualis in ("B1", "B2", "B3", "B4"):
				cluster_dict[cluster][program]["total_B"] += 1
      
  return cluster_dict

def dict_to_json(filename, dictionary):
  json_dict = json.dumps(dictionary)
  
  with open(filename, "w") as file:
    file.write(json_dict)

def dict_from_json(src):
  with open(src) as json_file:
    dictionary = json.load(json_file)

    return dictionary

def make_dict(csv_file, cluster_list = None):
  cluster_dict = count_qualis_occurances_for_programs(csv_file)

  if cluster_list is None:
    selected_clusters = cluster_dict
  else:
    selected_clusters = string_to_list(cluster_list, separator='-')

  for cluster in selected_clusters:
    filename = file_name_from_path(csv_file) + "_" + cluster + ".json"
    dict_to_json(filename, cluster_dict[cluster])

def make_qualis_count_list(dictionary):
  count_dict = {"A1": [], 
                "A2": [], 
                "A3": [], 
                "A4": [], 
                "B1": [], 
                "B2": [], 
                "B3": [], 
                "B4": [], 
                "C/NI/NP": []}
  for key in dictionary:
    for qualis in count_dict:
      count_dict[qualis].append(dictionary[key][qualis])

  return count_dict


def plot_program(dict_src, program_code_list_str, image_name = None):
  program_code_list = string_to_list(program_code_list_str, separator="-")
  subdict = {key : value for key, value in dict_from_json(dict_src).items() if key in program_code_list}
  count_dict = make_qualis_count_list(subdict)

  fig, ax = plt.subplots()
  x = np.arange(len(program_code_list))
  bar_width = 0.08
  multiplier = 0
  colors = ["#0d340d", "#165816", "#32c732", "#48bfe3", "#5e60ce", "#7400b8", "#4d0400", "#a80900", "#ff3d33"]

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
    image_name = file_name_from_path(dict_src) + "_" + str(program_code_list) + ".png"
  fig.savefig(image_name)

"""
if __name__ == '__main__':
  globals()[sys.argv[1]](*sys.argv[2:])
"""

cluster1 = count_qualis_occurances_for_programs("Particao_k3_c1.csv")["cluster1"]
ordenados = sorted(cluster1, key=lambda programa : programa["total_A"])
