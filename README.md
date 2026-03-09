# 📁 Medical Data Validator

A Python program that validates medical records against a strict set of formatting and data rules.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)

## 📌 About

This project validates a list of medical records to ensure each one complies with a defined set of rules correct data types, valid field formats, and required keys. It was built to practice data validation, error handling, regular expressions, and dictionary unpacking in a realistic real world context.

## 🧠 What I Learned
- Regular expressions with `re` — Using `re.fullmatch()` with patterns like `p\d+` and `v\d+` to validate that IDs follow a strict format, and using `re.IGNORECASE` to accept both upper and lowercase
- Dictionary unpacking with `**` — Passing a dictionary's values directly into a function as named arguments using `findInvalidRecords(**dictionary)`, which made the code much cleaner than manually extracting each value
- Validation with a constraints dictionary — Storing each field's validation logic as a `True/False` expression inside a dictionary, then filtering for failed keys — a neat pattern for keeping validation readable and easy to extend
- `isinstance()` for type checking — Validating that fields are the correct type (e.g. `age` is an `int`, `medications` is a `list` of strings) before checking their values
- Set comparison for key validation — Using `set(dictionary.keys()) != keySet` to catch both missing and unexpected keys in one clean check
- Separating concerns — Splitting the logic into `findInvalidRecords()` for field-level validation and `validate()` for record-level structure checks, keeping each function 

## 🛠️ Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x   | Core Language |
| `re`         | Validating ID formats with regular expressions |

## 💡 How It Works
`validate(data)` takes a list of medical record dictionaries and checks two things:
1. **Structure** — Is each record a dictionary with exactly the right keys?
2. **Field values** — Does each field pass its type and format rules?

Field rules are defined in `findInvalidRecords():`

| Field | Rule |
|-------|------|
| `patientID`  | String matching `P` followed by digits (e.g. `P1001`) |
| `age`        | Integer, 18 or older |
| `gender`     | String, either `"male"` or `"female"` |
| `diagnosis`  | String or `None` |
| `medications` | List of strings |
| `lastVisitID` | String matching `V` followed by digits (e.g. `V2301`) |

**Example Output:**

```
Valid format.
```
```
Unexpected format age: 15 at position 0.
Unexpected format patientID: 1001 at position 1.
```

## 🚀 Future Improvements

- [ ] Load medical records from a JSON or CSV file instead of hardcoding them
- [ ] Return a structured validation report instead of just printing errors
- [ ] Add a minimum/maximum age rule and support for more gender options
- [ ] Write unit tests with pytest to cover edge cases like None values, empty lists, and wrong types
- [ ] Allow custom rule sets to be passed in so the validator can be reused for other data formats

## 📂 Project Structure

```
medical-validator/
│
├── P4MedicalValidator.py    # Validation logic and sample medical records
└── README.md
```

*Part of my Python learning journey 🐍 — practicing data validation, regular expressions, and dictionary unpacking*
