#https://pypi.org/project/prettytable/ (module documentation)
#pip install prettytable(install module from cmd or powershell)
from prettytable import from_csv
print('''         CSV TO TABLE CONVERTER      ''')
path = input(str("Enter Path of CSV file (without quotes) :"))#importing path of csv file
csv_file = open(path)#opening csv file
csv_data = from_csv(csv_file) #conerting csv into tabular form 
print(csv_data) #printing tabular form of csv file

