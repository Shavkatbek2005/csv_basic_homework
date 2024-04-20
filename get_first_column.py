import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    return list(data)[1]
    
# Read the csv file
f=open('data.csv',mode='r')
data=csv.reader(f)
print(get_first_column(data))