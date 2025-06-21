# Automated Form Submission using Selenium and Excel

This project automates data entry on the [Unitetools KA portal](https://ka.unitetools.in) using Python, Selenium, and Excel.

## 📂 Project Structure

```

project-folder/
│
├── chromedriver\_win32/
│   └── chromedriver.exe      # ChromeDriver executable (required)
│
├── test.xlsx                 # Excel file with data to be submitted
├── automation\_script.py      # Main Selenium automation script
└── README.md                 # This file

````

## 🔧 Prerequisites

Ensure you have the following installed:

- Python 3.7+
- Google Chrome browser
- ChromeDriver compatible with your Chrome version

### 📦 Required Python Libraries

Install dependencies with:

```bash
pip install selenium pandas openpyxl
````

## 📁 Excel File Format (`test.xlsx`)

Ensure your Excel sheet has the following **column headers** (one row of headers, starting from A1):

* `Customer Type*`
* `Member Name*`
* `Admission Number*`
* `Surname*`
* `Gender*`
* `Share Balance ( )*`
* `Village*`
* `Ledger Folio No.*`
* `Date of Birth`
* `Age as on Admission Date`
* `Father Name*`
* `Mobile Number`
* `Address`
* `Spouse Name`
* `Dividend Amount ( )`
* `Thrift Balance(  )`
* `DCCB SB Account No.`

> 🔔 All fields are required. Optional fields in the site (like Caste, Marital Status, etc.) are currently skipped in the script.

## 🚀 Running the Script

1. **Set up `chromedriver.exe`:**
   Download and place the [ChromeDriver](https://sites.google.com/chromium.org/driver/) in the `chromedriver_win32` folder.

2. **Run the script:**

```bash
python automation_script.py
```

3. **Login credentials:**
   You will be prompted to enter your username and password in the terminal.

## ✅ Features

* Automated login to the website
* Reads each row from Excel and fills the form fields
* Submits and confirms each form submission
* Uses Selenium to interact with form elements
* Handles basic type conversion from Excel (e.g., int to str)

## ⚠️ Notes

* Currently uses `time.sleep()` which can be unreliable; you can improve it using `WebDriverWait` with `expected_conditions`.
* Aadhaar number field is incorrectly filled using the mobile number. You should replace the selector and field accordingly.
* No error logging or retry mechanism is implemented—add this for production usage.
* Duplicate field selectors for "Father Name\*" exist—only one is needed.

## 🛠️ To Do

* Use `WebDriverWait` instead of `time.sleep()` for better stability
* Add logging for success/failure entries
* Handle optional fields like Marital Status, Caste, Farmer Type
* Improve error handling and retry logic
* Add GUI for uploading the Excel file (future enhancement)

## 📌 Author

Created by **Spoorti Jadhav**
Python + Django Developer
This project is part of automating manual workflows to increase productivity.

```

---

Let me know if you also want to include `.gitignore`, a sample `requirements.txt`, or a template Excel file (`test.xlsx`) example.
```
