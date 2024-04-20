import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    s=list(data)[0]
    
    return len(s)

    

# Read the csv file
f=open('data.csv',mode='r')
data=csv.reader(f)
print(find_number_of_columns(data))
    