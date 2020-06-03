import utils
from pandas import DataFrame
from pandas import read_csv


# from sklearn.model_selection import RepeatedStratifiedKFold, StratifiedKFold

# from sklearn.preprocessing import StandardScaler

def createNewData():
    data = DataFrame(readData("data-1583789001103.csv"))
    newData = data.copy()
    utils.writeDataFrame("newBase.csv", newData)
    print("Finish!!\n")


def readData(dataset="./newBase.csv"):
    """Read a csv file and load into a variable with pandas package

        Parameters
        ----------
            dataset: {string}
                the csv file which be readed
    """
    data = read_csv(dataset, encoding='utf-8')

    return data


# Split data into train and test
def splitSamples(data):
    samples = data.iloc[:, 0:4095].values
    target = data.iloc[:, 4096].values

    return samples, target


# Spliting train ans test data
def crossValidation(k):
    try:
        return StratifiedKFold(n_splits=k)
    except ValueError:
        print("Please put a number > 2")


def repeatCrossValidation(folds, repeats):
    try:
        return RepeatedStratifiedKFold(n_splits=folds, n_repeats=repeats)
    except ValueError:
        print("A least 2 folds and repeats!")
