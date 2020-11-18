import pandas as pd


def create_author():
    """
    Create a structure to represent an author

    :return: a new dict that represents an author
    """
    author_obj = {'programas': []}

    return author_obj


def count_program_occurances_for_authors(src):
    """
    Save in a csv file a processed data frame with only one "programa" per
    instance

    :param dataIn: a string that refers the name of the data frame which
        should be processed.
    :param dataOut: the output name of the data frame.
    :return: a dictionary with esch position represents an author with all
        publications of the received file.
    """
    dataframe = pd.read_csv(src)
    data_author = {}

    for i in dataframe.index:
        programa = dataframe['CD_PROGRAMA_IES'][i]
        author = dataframe['id_autor'][i]

        if (author in data_author.keys()) and (
                programa not in data_author[author]):
            data_author[author]['programas'].append(programa)
        elif author not in data_author.keys():
            data_author[author] = create_author()
            data_author[author]['programas'].append(programa)

    return data_author


def run():
    """
    Save in a csv file a processed dictionary with only one "programa" per
    instance

    :param dataIn: a string that refers the name of the data frame which
    should be processed.
    :param dataOut: the output name of the data frame.
    :return: a void return
    """
    data_in = "../input/dados_autores.csv"
    data_out = '../results/autoresProcessados.csv'
    print("called Qualis By Year")
    data_dict = count_program_occurances_for_authors(data_in)
    pd.DataFrame.from_dict(data_dict, orient='index').to_csv(data_out,
                                                             index=False)


if __name__ == '__main__':
    run()
