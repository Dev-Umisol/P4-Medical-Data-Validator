# Validate a set of medical data to ensure that in complies with a set of rules

#! Project 4: Medical Data Validator
# This project helped me gain a better understanding of data validation, small bit of error handling, and use of regular expressions
# It also helped me practice unpacking dictionaries.

import re

# Sample medical record for testing
medicalRecords = [
    {
        "patientID": "P1001", 
        "age": 34,
        "gender": "Female",
        "diagnosis": "Hypertension",
        "medications": ["Lisinopril"],
        "lastVisitID": "V2301"
    }
]

# Function to find invalid records in a medical record
def findInvalidRecords(patientID, age, gender, diagnosis, medications, lastVisitID):
    constraints = {
        "patientID": isinstance(patientID, str) and re.fullmatch("p\d+", patientID, re.IGNORECASE),
        "age": isinstance(age, int) and age >= 18,
        "gender": isinstance(gender, str) and gender.lower() in ("male", "female"),
        "diagnosis": isinstance(diagnosis, str) or diagnosis is None,
        "medications": isinstance(medications, list) and all([isinstance(i, str) for i in medications]),
        "lastVisitID": isinstance(lastVisitID, str) and re.fullmatch("v\d+", lastVisitID, re.IGNORECASE)
    }
    
    return [key for key,value in constraints.items() if not value]

# Function to validate a set of medical records
def validate(data):
    isSequence = isinstance(data, (list, tuple))
    
    if not isSequence:
        print("Invalid format: expected a list or tuple")
        return False
    
    isInvalid = False
    keySet = set(["patientID", "age", "gender", "diagnosis", "medications", "lastVisitID"])
    
    # Iterate through the medical records and validate each one
    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            isInvalid = True
            continue
        # Check if the dictionary has the correct keys
        if set(dictionary.keys()) != keySet:
            print(f"Invalid format: {dictionary} at position {index} has missing and/or invalid keys.")
            isInvalid = True
            continue
            
        invalidRecords = findInvalidRecords(**dictionary) # Unpacking the dictionary to pass the values as arguments to the function
        
        for invalidRecord in invalidRecords:
            print(f"Unexpected format {invalidRecord}: {dictionary[invalidRecord]} at position {index}.")
            isInvalid = True
    
    if isInvalid == True:
        return False
    
    print("Valid format.")
    
    return True

validate(medicalRecords)