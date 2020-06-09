from pandas import read_csv
from pandas import DataFrame

def create_author():
    """
    Create a structure to represent an author

    :return: a new dict that represents an author
    """
    author_obj = {
        'id_autor': 0,
        'nome_normalizado': '',
        'h_index': 0,
        'num_colab_inter': 0,
        'num_person_colab_inter': 0,
        'docente_ppg': 0,
        'd1_A1': 0,
        'd1_A2': 0,
        'd1_A3': 0,
        'd1_A4': 0,
        'd1_B1': 0,
        'd1_B2': 0,
        'd1_B3': 0,
        'd1_B4': 0,
        'd1_C/NI/NP': 0,
        'd2_A1': 0,
        'd2_A2': 0,
        'd2_A3': 0,
        'd2_A4': 0,
        'd2_B1': 0,
        'd2_B2': 0,
        'd2_B3': 0,
        'd2_B4': 0,
        'd2_C/NI/NP': 0,
        'd3_A1': 0,
        'd3_A2': 0,
        'd3_A3': 0,
        'd3_A4': 0,
        'd3_B1': 0,
        'd3_B2': 0,
        'd3_B3': 0,
        'd3_B4': 0,
        'd3_C/NI/NP': 0,
        'd4_A1': 0,
        'd4_A2': 0,
        'd4_A3': 0,
        'd4_A4': 0,
        'd4_B1': 0,
        'd4_B2': 0,
        'd4_B3': 0,
        'd4_B4': 0,
        'd4_C/NI/NP': 0
    }
    return author_obj


def split_author(author_list):
    """
    Spliting an author string to an author list

    :param author_list: a string that refers the id of the authors to be splited.
    :return: a list with id authors
    """
    author_list = author_list[1:-1]
    return author_list.split('-')


def get_location_in_dict(year):
    """
    Choosing the correct location according the pulbication year of the paper.

    :param year: the publication year of the corresponding paper.
    :return: a correspondent decade of the paper
    """
    if year >= 2020:
        s = 'd4'
    elif year >= 2010:
        s = 'd3'
    elif year >= 2000:
        s = 'd2'
    elif year >= 1990:
        s = 'd1'
    else:
        s = ''
    return s


def count_qualis_occurances_for_authors(src):
    """
    Save in a csv file a processed data frame with only one "programa" per
    instance

    :param dataIn: a string that refers the name of the data frame which
        should be processed.
    :param dataOut: the output name of the data frame.
    :return: a dictionary with esch position represents an author with all
        publications of the received file.
    """
    dataframe = read_csv(src)
    author_dict = {}
    for i in dataframe.index:
        qualis = dataframe['qualis'][i]
        year = dataframe['ano'][i]
        decada = get_location_in_dict(year)
        author_id_list = split_author(dataframe['autores'][i])
        if decada != '':
            for author_id in author_id_list:
                if author_id not in author_dict.keys():
                    author_dict[author_id] = create_author()
                    author_dict[author_id]['id_autor'] = author_id
                    # Call função
                    metrics = author_other_metrics(int(author_id))
                    if metrics != '':
                        author_dict[author_id]['num_person_colab_inter'] = \
                            metrics.pop()
                        author_dict[author_id]['num_colab_inter'] = metrics.pop()
                        author_dict[author_id]['h_index'] = metrics.pop()
                        author_dict[author_id]['nome_normalizado'] = metrics.pop()
                        author_dict[author_id]['docente_ppg'] = 1
                author_dict[author_id][decada + '_' + qualis] += 1
    return author_dict


def author_other_metrics(author_id):
    """
    Get the author's name, h_index, international colaboration and international
    colaborators if his is a researcher at the UFRN.

    :param author_id: the id of the author to check if his is a researcher at
    the UFRN.
    :return: the respective metrics if his exists in the csv
    """
    data = read_csv('autores_ufrn.csv')
    aux = list(data.id_author)
    try:
        pos = aux.index(author_id)
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


def run(data_in, data_out):
    """
    Save in a csv file a processed dictionary with only one "programa" per
    instance

    :param dataIn: a string that refers the name of the data frame which
    should be processed.
    :param dataOut: the output name of the data frame.
    :return: a void return
    """
    print("called Qualis By Year")
    data_dict = count_qualis_occurances_for_authors(data_in)
    DataFrame.from_dict(data_dict, orient='index').to_csv(data_out, index=False)
