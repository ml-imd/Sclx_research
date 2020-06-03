from pandas import DataFrame
from pandas import read_csv


def run(dataIn, dataOut):
    """
    Save in a csv file a processed data frame with only one "programa" per
    instance

    :param dataIn: a string that refers the name of the data frame which
    should be processed.
    :param dataOut: the output name of the data frame.
    :return: a void return
    """
    data = (dataIn, encoding='utf-8')
    columns = list(data.columns.values)
    new = DataFrame(columns=columns)
    for id, row in data.iterrows():
        length_programs = row["prog._qtd"]
        if length_programs == 1:
            new = new.append(row, ignore_index=True)
        else:
            split_programs = str(row.programas).split("-")
            split_programs[0] = split_programs[0][1:]
            split_programs[length_programs - 1] = split_programs[
                                                      length_programs - 1][:-1]
            while len(split_programs) > 0:
                aux = DataFrame({'#': [row['#']],
                                 'autor_docente': [row['autor_docente']],
                                 'autores': [row['autores']],
                                 'producao': [row['producao']],
                                 'ano': [row['ano']],
                                 'tipo_producao': [row['tipo_producao']],
                                 'citescore': [row['citescore']],
                                 'quartil_citescore': [row['quartil_citescore']],
                                 'percentile': [row['percentile']],
                                 'quartil_percentile': [row['quartil_percentile']],
                                 'q_p': [row['q_p']],
                                 'qualis_estrato': [row['qualis_estrato']],
                                 'qualis': [row['qualis']],
                                 'programas': [str([split_programs.pop(

                                 )]).replace("'", "")],
                                 'prog._qtd': [1],
                                 'Cluster': [row['Cluster']]
                                 })
                new = new.append(aux, ignore_index=True)
    new.to_csv(dataOut, index=False)
