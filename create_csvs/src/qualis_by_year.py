import pandas as pd


def create_author():
    d = {'A1': 0,
         'A2': 0,
         'A3': 0,
         'A4': 0,
         'B1': 0,
         'B2': 0,
         'B3': 0,
         'B4': 0,
         'C/NI/NP': 0}
    autor_obj = {'id_autor': 0,
                 'nome_normalizado': '',
                 'h_index': 0,
                 'num_colab_inter': 0,
                 'num_person_colab_inter': 0,
                 'docente_ppg': 0,
                 'd1': d.copy(),
                 'd2': d.copy(),
                 'd3': d.copy(),
                 'd4': d.copy()
                 }
    return autor_obj


def split_autor(autor_list):
    autor_list = autor_list[1:-1]
    return autor_list.split('-')


def get_location_in_dict(ano):
    if ano >= 2020:
        s = 'd4'
    elif ano >= 2010:
        s = 'd3'
    elif ano >= 2000:
        s = 'd2'
    elif ano >= 1990:
        s = 'd1'
    else:
        s = ''
    return s


def count_qualis_occurances_for_autores(src):
    dataframe = pd.read_csv(src)
    autor_dict = {}
    for i in dataframe.index:
        qualis = dataframe['qualis'][i]
        ano = dataframe['ano'][i]
        decada = get_location_in_dict(ano)
        autor_id_list = split_autor(dataframe['autores'][i])
        if decada != '':
            for autor_id in autor_id_list:
                if autor_id not in autor_dict.keys():
                    autor_dict[autor_id] = create_author()
                    autor_dict[autor_id]['id_autor'] = autor_id
                    # Call função
                    metrics = autor_outras_metricas(int(autor_id))
                    if metrics != '':
                        autor_dict[autor_id]['num_person_colab_inter'] = \
                            metrics.pop()
                        autor_dict[autor_id]['num_colab_inter'] = metrics.pop()
                        autor_dict[autor_id]['h_index'] = metrics.pop()
                        autor_dict[autor_id]['nome_normalizado'] = metrics.pop()
                        autor_dict[autor_id]['docente_ppg'] = 1
                autor_dict[autor_id][decada][qualis] += 1
    return autor_dict


def autor_outras_metricas(autor_id):
    data = pd.read_csv('Pesquisadores_UFRN.csv')
    aux = list(data.id_autor)
    try:
        pos = aux.index(autor_id)
        nome_norm = data.nome_normalizado[pos]
        h_index = data.h_index[pos]
        colaboracoes_inter = data.colaborações_internacionais[pos]
        colaboradores_inter = data.colaboradores_internacionais[pos]
        metrics = list()
        metrics.append(nome_norm)
        metrics.append(h_index)
        metrics.append(colaboracoes_inter)
        metrics.append(colaboradores_inter)
        return metrics.copy()
    except ValueError:
        return ''
