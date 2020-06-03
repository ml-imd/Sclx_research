from pandas import DataFrame


from .preprocessing import readData
from .utils import writeDataFrame


def main(dataIn, dataOut):
    data = readData(dataIn).fillna(0).drop("id", axis=1)
    columns = ['autor_docente', 'autor_nao_docente', 'autores', 'id_producao',
               'ano', 'sub_tipo_producao', 'citescore', 'quartil_citescore',
               'percentile', 'quartil_percentile', 'qualis_estrato',
               'PROGRAMAS',
               'progrmas_quantidade']
    new = DataFrame(columns=columns)
    idPubs = sorted(set(data.id_producao))
    qualisEst = {
        'A1': 1, 'A2': 0.9, 'A3': 0.8, 'A4': 0.7, 'B1': 0.5, 'B2': 0.35,
        'B3': 0.2, 'B4': 0.05, 'C': 0, 'NP': 0, 'NI': 0, None: 0, 0: 0
    }
    quartil = {
        'Q4': 1, 'Q3': 0.75, 'Q2': 0.5, 'Q1': 0.25, 'Q0': 0, None: 0, 0: 0
    }

    for idPub in idPubs:
        prod = data[data.id_producao.isin([idPub])]
        authors = sorted(set(prod.id_autor))
        profAuthor = 0
        studAuthor = 0

        for author in authors:
            if prod[prod.id_autor.isin([author])].docente.any():
                profAuthor += 1
            else:
                studAuthor += 1
        progs = sorted(set(prod.CD_PROGRAMA_IES))
        totalProgs = len(progs)
        row = DataFrame({'autor_docente': [profAuthor],
                         'autor_nao_docente': [studAuthor],
                         'autores': [str(authors).replace(', ', '-')],
                         'id_producao': [idPub],
                         'ano': [prod.ano.values[0]],
                         'sub_tipo_producao': [
                             prod.sub_tipo_producao.values[0]],
                         'citescore': [prod.citescore.values[0]],
                         'quartil_citescore': [
                             quartil.get(prod.quartil_citescore.values[0])],
                         'percentile': [prod.percentile.values[0]],
                         'quartil_percentile': [
                             quartil.get(prod.quartil_percentile.array[0])],
                         'qualis_estrato': [
                             qualisEst.get(prod.qualis_estrato.values[0])],
                         'PROGRAMAS': [
                             str(progs).replace("'", '').replace(', ', '-')],
                         'progrmas_quantidade': [totalProgs]
                         })
        new = new.append(row, ignore_index=True)
        print(str(round(idPubs.index(idPub) / len(idPubs) * 100, 3)) + '%')
    writeDataFrame(dataOut, new)
