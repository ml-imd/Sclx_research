import csv


def writeCSV(name, values):
    try:
        with open(name, "w", encoding="UTF-8") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(values)
        csvFile.close()
    except IOError:
        print("Invalid name")
        raise


def writeDataFrame(name, data):
    try:
        data.to_csv(name, index=False)
    except IOError:
        print("Invalid name")
        raise
