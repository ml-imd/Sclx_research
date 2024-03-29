import json
import os.path
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from ntpath import split, basename
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def string_to_list(list_str, separator=',', delimiter='[]'):
    return list_str.strip(delimiter).split(separator)


def file_name_from_path(path):
    head, tail = split(path)
    filename = tail or basename(head)
    # removing filename extension
    if "." in filename:
        i = -1
        while filename[i] != '.':
            i -= 1
        filename = filename[:i]
    return filename


def sort_programs_dict(cluster_dict, sort_by):
    for program in cluster_dict:
        cluster_dict[program] = dict(sorted(
            cluster_dict[program].items(), key=lambda item: item[1][sort_by], reverse=True))
    return cluster_dict


def count_qualis_occurances_for_programs(src):
    df = pd.read_csv(src)
    cluster_dict = {}
    programs_list = []
    for i in df.index:
        qualis = df["qualis"][i]
        cluster = df["Cluster"][i]
        programs_list = string_to_list(
            df["programas"][i], separator='-')
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
    return cluster_dict


def dict_to_json(filename, dictionary):
    # converting dictionary into a json string
    json_dict = json.dumps(dictionary)
    with open(filename, "w") as file:
        file.write(json_dict)


def dict_from_json(src):
    with open(src) as json_file:
        dictionary = json.load(json_file)
        return dictionary


def make_dict(csv_file, cluster_list=None, sort_by="A1/A2/A3/A4"):
    cluster_dict = sort_programs_dict(count_qualis_occurances_for_programs(csv_file), sort_by)
    selected_clusters = cluster_dict
    # checking if a list of clusters was specified
    if cluster_list is not None:
        selected_clusters = string_to_list(cluster_list, separator='-')
    filename = "./" + file_name_from_path(csv_file) + ".json"
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


def get_program_name(program):
    programs = {
        '23001011005P7': 'CIÊNCIAS ODONTOLÓGICAS',
        '23001011031P8': 'CIÊNCIAS DA SAÚDE',
        '23001011033P0': 'SAÚDE COLETIVA',
        '23001011001P1': 'EDUCAÇÃO',
        '23001011036P0': 'DESENVOLVIMENTO E MEIO AMBIENTE',
        '23001011018P1': 'GEODINÂMICA E GEOFÍSICA',
        '23001011028P7': 'GEOGRAFIA',
        '23001011051P9': 'ENGENHARIA CIVIL',
        '23001011066P6': 'GESTÃO DE PROCESSOS INSTITUCIONAIS',
        '23001011021P2': 'ENGENHARIA DE PRODUÇÃO',
        '23001011010P0': 'FÍSICA',
        '23001011024P1': 'ARQUITETURA E URBANISMO',
        '23001011052P5': 'ARQUITETURA, PROJETO E MEIO AMBIENTE',
        '23001011059P0': 'SISTEMÁTICA E EVOLUÇÃO',
        '23001011061P4': 'CIÊNCIAS FLORESTAIS',
        '23001011056P0': 'CIÊNCIAS CLIMÁTICAS',
        '33283010001P5': 'ENSINO DE FÍSICA - PROFIS',
        '23001011012P3': 'QUÍMICA',
        '23001011040P7': 'CIÊNCIAS FARMACÊUTICAS',
        '23001011047P1': 'DESENVOLVIMENTO E INOVAÇÃO TECNOLÓGICA EM MEDICAMENTOS',
        '23001011008P6': 'ENGENHARIA ELÉTRICA',
        '23001011026P4': 'CIÊNCIA E ENGENHARIA DE MATERIAIS',
        '23001011174P3': 'INOVAÇÃO EM TECNOLOGIAS EDUCACIONAIS',
        '23001011003P4': 'PSICOBIOLOGIA',
        '23001011054P8': 'NEUROCIÊNCIAS',
        '23001011020P6': 'BIOQUÍMICA',
        '23001011038P2': 'HISTÓRIA',
        '23001011072P6': 'GESTÃO DA QUALIDADE EM SERVIÇOS DE SAÚDE',
        '31010016027P9': 'SAÚDE DA FAMÍLIA',
        '23001011030P1': 'FILOSOFIA',
        '23001011037P6': 'ANTROPOLOGIA SOCIAL',
        '22003010017P5': 'BIOTECNOLOGIA - Rede RENORBIO',
        '23001011011P7': 'ENGENHARIA QUÍMICA',
        '23001011074P9': 'ENGENHARIA MECATRÔNICA',
        '23001011025P8': 'PSICOLOGIA',
        '23001011075P5': 'NUTRIÇÃO',
        '23001011041P3': 'CIÊNCIA E ENGENHARIA DE PETRÓLEO',
        '23001011170P8': 'BIOINFORMÁTICA',
        '23001011058P3': 'DEMOGRAFIA',
        '23001011053P1': 'ESTUDOS DA MÍDIA',
        '23001011022P9': 'SISTEMAS E COMPUTAÇÃO',
        '23001011176P6': 'ENGENHARIA TÊXTIL',
        '23001011034P7': 'DIREITO',
        '23001011046P5': 'TURISMO',
        '23001011029P3': 'ENFERMAGEM',
        '23001011071P0': 'TECNOLOGIA DA INFORMAÇÃO',
        '23001011023P5': 'ENGENHARIA SANITÁRIA E AMBIENTAL',
        '23001011027P0': 'SERVIÇO SOCIAL',
        '23001011060P8': 'EDUCAÇÃO FÍSICA',
        '23001011063P7': 'ENSINO NA SAÚDE',
        '23001011013P0': 'ESTUDOS DA LINGUAGEM',
        '23001011069P5': 'LETRAS',
        '23001011050P2': 'PRODUÇÃO ANIMAL',
        '23001011015P2': 'ECOLOGIA',
        '23001011067P2': 'MÚSICA',
        '23001011070P3': 'BIOLOGIA ESTRUTURAL E FUNCIONAL',
        '23001011172P0': 'EDUCAÇÃO, TRABALHO E INOVAÇÃO EM MEDICINA',
        '23001011055P4': 'ESTUDOS URBANOS E REGIONAIS',
        '23001011007P0': 'ADMINISTRAÇÃO',
        '23001011076P1': 'CIÊNCIAS CONTÁBEIS',
        '23001011009P2': 'ENGENHARIA MECÂNICA',
        '23001011177P2': 'SAÚDE E SOCIEDADE',
        '23001011035P3': 'CIÊNCIAS BIOLÓGICAS',
        '23001011073P2': 'BIOLOGIA PARASITÁRIA',
        '23001011043P6': 'FISIOTERAPIA',
        '23001011171P4': 'SAÚDE COLETIVA',
        '23001011032P4': 'ENSINO DE CIÊNCIAS NATURAIS E MATEMÁTICA',
        '23001011077P8': 'ENSINO DE CIÊNCIAS E MATEMÁTICA',
        '24001015081P8': 'FONOAUDIOLOGIA',
        '31001017169P2': 'QUÍMICA EM REDE NACIONAL',
        '23001011062P0': 'DESIGN',
        '23001011057P7': 'GESTÃO PÚBLICA',
        '23001011004P0': 'CIÊNCIAS SOCIAIS',
        '23001011173P7': 'CIÊNCIAS DA REABILITAÇÃO',
        '23001011042P0': 'MATEMÁTICA APLICADA E ESTATISTICA',
        '52001016048P0': 'NANOTECNOLOGIA FARMACÊUTICA',
        '23001011044P2': 'ARTES CÊNICAS',
        '41002016026P1': 'PROFARTES',
        '23001011078P4': 'GEOGRAFIA',
        '33004137068P8': 'EDUCAÇÃO FÍSICA',
        '22001018074P6': 'DESENVOLVIMENTO E MEIO AMBIENTE',
        '23001011080P9': 'GESTÃO DA INFORMAÇÃO E DO CONHECIMENTO',
        '23001011175P0': 'GESTÃO E INOVAÇÃO EM SAÚDE',
        '23001011079P0': 'CIÊNCIA, TECNOLOGIA E INOVAÇÃO',
        '23001011039P9': 'ECONOMIA',
        '23001011068P9': 'ENERGIA ELÉTRICA',
        '31001017155P1': 'ENSINO DE HISTÓRIA',
        '24001015046P8': 'FILOSOFIA',
        '31075010001P2': 'MATEMÁTICA EM REDE NACIONAL',
        '53001010073P0': 'CONTABILIDADE'
    }
    return programs[program]


def plot(subdict, program_code_list, count_dict, title, program_name, image_name, template="program", comparing=False,
         auto_label=False, cluster=False, in_this_frame=None):
    # defining some specific attributes based on what template is being used for the graphs
    if template == "program":
        bar_width = 0.08
        colors = ["#54c73a", "#abd216", "#ccce0f", "#f0f200",
                  "#ffce00", "#ff9a00", "#ff6700", "#ff3300", "#ff0000"]
        tick_translate = 4
        axvline_translate = 10 * bar_width + bar_width / 3
    elif template == "compare":
        bar_width = 0.15
        colors = ["#d6af36", "#a7a7ad", "#a77044"]
        tick_translate = 1
        axvline_translate = 4 * bar_width + bar_width / 3
    fig, ax = plt.subplots()
    x = np.arange(len(program_code_list))
    multiplier = 0
    for key in count_dict:
        bar = ax.bar(x + bar_width * multiplier, count_dict[key], width=bar_width, label=key,
                     color=colors[multiplier])
        if auto_label:
            # labeling each bar
            label_bar(ax, bar)
        multiplier += 1
    # plotting vertical lines between each program or group
    j = 0
    for i in range(len(program_code_list) - 1):
        if i > 0:
            j = bar_width + bar_width / 3
        plt.axvline(x=axvline_translate + i * (axvline_translate + bar_width + j), color="#DDDDDD")
    if program_name:
        program_code_list = [get_program_name(program) for program in program_code_list]
    # setting up x labels and legend
    ax.set_xticks(x + tick_translate * bar_width)
    ax.set_xticklabels(program_code_list)
    ax.legend(bbox_to_anchor=(1.04, 0), loc="lower left")
    # setting up plot design
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(left=False, bottom=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#DDDDDD')
    ax.set_title(title)
    ax.set_ylabel("Quantidade")
    if cluster:
        ax.set_xlabel("Grupos")
    else:
        ax.set_xlabel("Programas")
    # rotating x labels if number of programs/groups is greater than 3
    # this way labels won't overlap each other
    if len(subdict) > 3:
        fig.autofmt_xdate()
    fig.tight_layout()
    if comparing:
        plt.gca().get_xticklabels()[-1].set_color('red')
    if in_this_frame is None:
        fig.savefig(image_name)
    else:
        canvas = FigureCanvasTkAgg(fig, master=in_this_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas, in_this_frame)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def plot_program(dict_src, program_code_list_str, cluster, image_name=None, comparing=False, program_name=False,
                 where_to_store="./", in_this_frame=None):
    program_code_list = string_to_list(program_code_list_str, separator="-")
    subdict = {key: value for key, value in dict_from_json(
        dict_src)[cluster].items() if key in program_code_list}
    count_dict = make_values_dict_from_keys(subdict, ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C/NI/NP"])
    if image_name is None:
        image_name = where_to_store + file_name_from_path(
            dict_src) + "_" + program_code_list_str + ".png"
    plot(subdict, program_code_list, count_dict, "Produções por programa", program_name, image_name=image_name,
         comparing=comparing, in_this_frame=in_this_frame)


def plot_n_best(dict_src, n_str, cluster, compare_to=None, image_name=None, program_name=False, in_this_frame=None):
    n = int(n_str)
    program_code_list_str = "["
    count = 0
    for program in dict_from_json(dict_src)[cluster]:
        if count == n:
            break
        if count != n - 1:
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
    plot_program(dict_src, program_code_list_str, cluster, program_name=program_name, image_name=image_name,
                 comparing=comparing, in_this_frame=in_this_frame)


def plot_compare(dict_src, program_code_list_str, cluster, image_name=None, program_name=False, where_to_store="./",
                 in_this_frame=None):
    program_code_list = string_to_list(program_code_list_str, separator="-")
    subdict = {key: value for key, value in dict_from_json(
        dict_src)[cluster].items() if key in program_code_list}
    count_dict = make_values_dict_from_keys(subdict, ["A1/A2/A3/A4", "B1/B2/B3/B4", "C/NI/NP"])
    if image_name is None:
        image_name = where_to_store + file_name_from_path(
            dict_src) + "_" + program_code_list_str + "_compare.png"
    plot(subdict, program_code_list, count_dict, "Comparação entre programas", program_name, image_name=image_name,
         template="compare", in_this_frame=in_this_frame)


def plot_program_cluster(dict_src, program, cluster_list_str=None, image_name=None, where_to_store="./",
                         in_this_frame=None):
    dictionary = dict_from_json(dict_src)
    if cluster_list_str is not None:
        selected_clusters = string_to_list(cluster_list_str, separator='-')
    else:
        selected_clusters = dictionary
    subdict = {key: dictionary[key][program] for key in selected_clusters if program in dictionary[key]}
    count_dict = make_values_dict_from_keys(subdict, ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C/NI/NP"])
    if image_name is None:
        image_name = where_to_store + file_name_from_path(
            dict_src) + "_" + program + '_' + ".png"
    plot(subdict, subdict.keys(), count_dict, "Publicações por grupo", False, image_name=image_name, cluster=True,
         in_this_frame=in_this_frame)


def plot_cluster_compare(dict_src, program, cluster_list_str=None, image_name=None, where_to_store="./",
                         in_this_frame=None):
    dictionary = dict_from_json(dict_src)
    if cluster_list_str is not None:
        selected_clusters = string_to_list(cluster_list_str, separator='-')
    else:
        selected_clusters = dictionary
    subdict = {key: dictionary[key][program] for key in selected_clusters if program in dictionary[key]}
    count_dict = make_values_dict_from_keys(subdict, ["A1/A2/A3/A4", "B1/B2/B3/B4", "C/NI/NP"])
    if image_name is None:
        image_name = where_to_store + file_name_from_path(
            dict_src) + "_" + program + '_' + "compare.png"
    plot(subdict, subdict.keys(), count_dict, "Comparação entre grupos", False, image_name=image_name,
         template="compare", cluster=True, in_this_frame=in_this_frame)


class DataInputCell(tk.Frame):
    def __init__(self, master=None, name=None):
        super().__init__(master)
        self.master = master
        self.name = name
        self.label_name = tk.Label(self, text=self.name, width=20)
        self.label_name.pack(side=tk.LEFT)
        self.entry_name = tk.Entry(self, text=self.name, width=40)
        self.entry_name.pack(side=tk.RIGHT)
        self.pack()


class DataInput(tk.Frame):
    def __init__(self, master=None, names=None):
        super().__init__(master)
        self.master = master
        self.names = names
        self.data = {}
        for self.name in self.names:
            self.data[self.name] = DataInputCell(self, self.name)
        self.pack()


class OneProgram(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=1, fill=tk.BOTH)
        self.control_area = tk.Frame(self)
        self.control_area.pack(side=tk.LEFT)
        self.plotting_area = tk.Frame(self)
        self.plotting_area.pack(side=tk.RIGHT)
        self.dict_src = "./Particoes.json"
        self.control()

    def plot(self):
        self.plotting_area.destroy()
        self.plotting_area = tk.Frame(self)
        self.plotting_area.pack(side=tk.RIGHT)
        self.program = self.data_input.data["Program"].entry_name.get()
        self.cluster_list_str = self.data_input.data["Cluster List"].entry_name.get()
        plot_cluster_compare(dict_src=self.dict_src, program=self.program, cluster_list_str=self.cluster_list_str,
                             in_this_frame=self.plotting_area)

    def control(self):
        self.names = ["Program", "Cluster List"]
        self.data_input = DataInput(self.control_area, self.names)
        if self.data_input.data["Program"].entry_name.get() == "":
            self.data_input.data["Program"].entry_name.insert(tk.END, '23001011010P0')
        if self.data_input.data["Cluster List"].entry_name.get() == "":
            self.data_input.data["Cluster List"].entry_name.insert(tk.END, '[cluster1-cluster2]')
        self.plotting_button = tk.Button(self.control_area, text="Plot", command=self.plot)
        self.plotting_button.pack(side=tk.RIGHT)


class ProgramCompare(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=1, fill=tk.BOTH)
        self.control_area = tk.Frame(self)
        self.control_area.pack(side=tk.LEFT)
        self.plotting_area = tk.Frame(self)
        self.plotting_area.pack(side=tk.RIGHT)
        self.dict_src = "./Particoes.json"
        self.control()

    def plot(self):
        self.plotting_area.destroy()
        self.plotting_area = tk.Frame(self)
        self.plotting_area.pack(side=tk.RIGHT)
        self.program_code_list_str = self.data_input.data["Program List"].entry_name.get()
        self.cluster = self.data_input.data["Cluster "].entry_name.get()
        plot_compare(dict_src=self.dict_src, program_code_list_str=self.program_code_list_str, cluster=self.cluster,
                     program_name=self.program_name, in_this_frame=self.plotting_area)

    def control(self):
        self.names = ["Program List", "Cluster "]
        self.data_input = DataInput(self.control_area, self.names)
        if self.data_input.data["Program List"].entry_name.get() == "":
            self.data_input.data["Program List"].entry_name.insert(tk.END, '[23001011010P0-23001011031P8-23001011020P6]')
        if self.data_input.data["Cluster "].entry_name.get() == "":
            self.data_input.data["Cluster "].entry_name.insert(tk.END, 'cluster1')
        self.program_name = True
        self.plotting_button = tk.Button(self.control_area, text="Plot", command=self.plot)
        self.plotting_button.pack(side=tk.RIGHT)


class NBest(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=1, fill=tk.BOTH)
        self.control_area = tk.Frame(self)
        self.control_area.pack(side=tk.LEFT)
        self.plotting_area = tk.Frame(self)
        self.plotting_area.pack(side=tk.RIGHT)
        self.dict_src = "./Particoes.json"
        self.control()

    def plot(self):
        self.plotting_area.destroy()
        self.plotting_area = tk.Frame(self)
        self.plotting_area.pack(side=tk.RIGHT)
        self.n = int(self.data_input.data["Number of Programs"].entry_name.get())
        self.cluster = self.data_input.data["Cluster"].entry_name.get()
        self.compare_to = self.data_input.data["Compare to"].entry_name.get()
        plot_n_best(dict_src=self.dict_src, n_str=self.n, cluster=self.cluster, compare_to=self.compare_to,
                    program_name=self.program_name, in_this_frame=self.plotting_area)

    def control(self):
        self.names = ["Number of Programs", "Cluster", "Compare to"]
        self.data_input = DataInput(self.control_area, self.names)
        if self.data_input.data["Number of Programs"].entry_name.get() == "":
            self.data_input.data["Number of Programs"].entry_name.insert(tk.END, '2')
        if self.data_input.data["Cluster"].entry_name.get() == "":
            self.data_input.data["Cluster"].entry_name.insert(tk.END, 'cluster1')
        if self.data_input.data["Compare to"].entry_name.get() == "":
            self.data_input.data["Compare to"].entry_name.insert(tk.END, '23001011030P1')
        self.program_name = True
        self.plotting_button = tk.Button(self.control_area, text="Plot", command=self.plot)
        self.plotting_button.pack(side=tk.RIGHT)


class ProgramPerCluster(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=1, fill=tk.BOTH)
        self.control_area = tk.Frame(self)
        self.control_area.pack(side=tk.LEFT)
        self.plotting_area = tk.Frame(self)
        self.plotting_area.pack(side=tk.RIGHT)
        self.dict_src = "./Particoes.json"
        self.control()

    def plot(self):
        self.plotting_area.destroy()
        self.plotting_area = tk.Frame(self)
        self.plotting_area.pack(side=tk.RIGHT)
        self.program = self.data_input.data["Program "].entry_name.get()
        self.cluster_list_str = self.data_input.data["Cluster List "].entry_name.get()
        plot_program_cluster(dict_src=self.dict_src, program=self.program, cluster_list_str=self.cluster_list_str,
                             in_this_frame=self.plotting_area)

    def control(self):
        self.names = ["Program ", "Cluster List "]
        self.data_input = DataInput(self.control_area, self.names)
        if self.data_input.data["Program "].entry_name.get() == "":
            self.data_input.data["Program "].entry_name.insert(tk.END, '23001011010P0')
        if self.data_input.data["Cluster List "].entry_name.get() == "":
            self.data_input.data["Cluster List "].entry_name.insert(tk.END, '[cluster1-cluster2]')
        self.plotting_button = tk.Button(self.control_area, text="Plot", command=self.plot)
        self.plotting_button.pack(side=tk.RIGHT)


class ApplicationStatusBar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.bar = tk.Label(self, text="Welcome to Scylax!", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.bar.pack(expand=1, fill=tk.X)
        self.pack(side=tk.BOTTOM, fill=tk.X)


class ApplicationBody(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.present_screen = None
        self.pack(expand=1, fill=tk.BOTH)

    def one_program(self):
        self.present_screen is not None and self.present_screen.destroy()
        self.present_screen = OneProgram(self)

    def program_compare(self):
        self.present_screen is not None and self.present_screen.destroy()
        self.present_screen = ProgramCompare(self)

    def n_best(self):
        self.present_screen is not None and self.present_screen.destroy()
        self.present_screen = NBest(self)

    def program_per_cluster(self):
        self.present_screen is not None and self.present_screen.destroy()
        self.present_screen = ProgramPerCluster(self)


class ApplicationTopMenu:
    def __init__(self, master=None):
        self.master = master
        self.master.master.menu_bar = tk.Menu(self.master.master)
        self.master.master.file_menu = tk.Menu(self.master.master.menu_bar, tearoff=0)
        self.master.master.file_menu.add_command(label="Load", command=self.load_data)
        self.master.master.menu_bar.add_cascade(label="Data", menu=self.master.master.file_menu)
        self.master.master.edit_menu = tk.Menu(self.master.master.menu_bar, tearoff=0)
        self.master.master.edit_menu.add_command(label="One Program", command=self.master.application_body.one_program)
        self.master.master.edit_menu.add_command(label="Program Compare",
                                                 command=self.master.application_body.program_compare)
        self.master.master.edit_menu.add_command(label="N Best", command=self.master.application_body.n_best)
        self.master.master.edit_menu.add_command(label="Program per cluster",
                                                 command=self.master.application_body.program_per_cluster)
        self.master.master.menu_bar.add_cascade(label="Plot", menu=self.master.master.edit_menu)
        self.master.master.config(menu=self.master.master.menu_bar)

    def load_data(self):
        self.master.application_status_bar.bar["text"] = "Loading..."
        try:
            if os.path.exists("./Particoes.json"):
                if tk.messagebox.askquestion("This data has been imported before",
                                             "Would you like to import anyway?") == "no":
                    self.master.application_status_bar.bar["text"] = "Finished!"
                    return
            file_name = filedialog.askopenfilename(initialdir=".", title="Select file to load data",
                                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            make_dict(file_name)
            self.master.application_status_bar.bar["text"] = "Finished!"
        except:
            self.master.application_status_bar.bar["text"] = "Fail!"


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Scylax")
        w = int(self.master.winfo_screenwidth())
        h = int(self.master.winfo_screenheight())
        self.master.geometry("{}x{}".format(w, h))
        self.application_status_bar = ApplicationStatusBar(self)
        self.application_body = ApplicationBody(self)
        self.application_top_menu = ApplicationTopMenu(self)
        self.pack(expand=1, fill=tk.BOTH)


root = tk.Tk()
app = Application(master=root)
root.mainloop()
