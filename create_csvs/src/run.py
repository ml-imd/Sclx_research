import sys

import papers_data_creation
import qualis_by_year
import split_program


def name_the_file(filename, dataIn):
    """
    Modify the name of the file passed as a param'

    :param filename: the parameter received in command line
    :param dataIn: the name of the file received by command line
    :return: the location of the file
    """
    try:
        length = len(filename.split('/'))

        if length == 1:
            file_location = '../results/' + filename
        elif length == 2:
            file_location = file_location + dataIn + 'Output.csv'
        else:
            file_location = filename
    except NameError:
        file_location = file_location + dataIn + 'Output.csv'

    return file_location


if __name__ == "__main__":
    path = '.'

    if sys.argv[1] == '-h' or sys.argv[1] == '--help' or sys.argv[1] == '-H':
        print('This file require 3 parameters, that follows:')
        print(
            'The first represents witch file do you want to execute, in order:'
        )
        print('\t 1 - papers_data_creation.py this file generate a new csv,',
              'where each line represents a paper.')
        print('\t 2 - split_program this file generate a new csv, where each',
              'line represents a "programa".')
        print('\t 3 - qualis_by_year this file create a new csv file, where',
              'each line represent a researcher.')
        print(
            '\n The second parameter represent the input file and the location'
        )
        print(
            '\n The last parameter represents the output file and the location'
        )
    else:
        dataIn = sys.argv[2]
        dataOut = name_the_file(sys.argv[3], sys.argv[1].split('.')[0])
        num = int(sys.argv[1])

        if num == 1:
            papers_data_creation.run(dataIn, dataOut)
        elif num == 2:
            split_program.run(dataIn, dataOut)
        elif num == 3:
            qualis_by_year.run(dataIn, dataOut)
        else:
            print('cannot be excuted')
            sys.exit(1)
