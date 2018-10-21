    
import sys
import csv

def main():
    name = input("Patient name:\t")

    #isalpha doesn't consider spaces so check if each char is a space or char in turn
    if not all(c.isalpha() or c.isspace() for c in name):
        print("\nError: Name can only contain alphabtes\n")
        sys.exit()

    try:
        age = int(input("Patient age:\t"))
    except:
        print("\nError: Invalid age")
        sys.exit()

    phone = input("Patient phone number:\t")

    # 'a+' opens a file for both reading and writing and creates file if not exists
    with open('records.csv', 'a+') as csv_file:
        patient_records = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_file.seek(0) #ensure you're at the start of the file..
        first_char = csv_file.read(1) #get the first character
        if not first_char:
            #file empty initialize csv with row names
            patient_records.writerow(['Name', 'Age', 'Phone'])

        patient_records.writerow([name, age, phone])

    print("\n Data written into records.csv\n")


if __name__=="__main__":
    main()