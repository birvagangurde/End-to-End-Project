# Selenium UI Automation Framework

This is a Pytest-based automation framework using Selenium WebDriver. 
The tests are written in Python and designed for UI automation of web applications. 
HTML reports are generated after every test run.

## 📁 Project Structure

├── data/
│ └── test_data.json # Test data in JSON format
├── pageobjects/ # Page Object classes (POM)
├── sel/
│ ├── framework.py # Core framework logic (driver init, utilities, hooks)
│ ├── conftest.py # Pytest fixtures
│ └── test_sorting.py # Test file for table sorting functionality
├── pytest.ini # Pytest config
├── requirements.txt # Project dependencies
└── README.md # You’re reading it

## 🚀 Getting Started

### 1. Clone the repo
    ```bash
         git clone https://github.com/your-username/your-repo-name.git
         cd your-repo-name

2. Set up a virtual environment (optional but recommended)
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   
3. Install dependencies
   pip install -r requirements.txt
   

🧪 Running Tests
Run all tests:
-pytest

Run tests with HTML report:
pytest --html=Reports/report.html

Run tests in parallel:
pytest -n 2
Make sure pytest-xdist is installed if you use -n for parallel runs.


✅ To Do
 -Add screenshots on test failures

 -Integrate with CI/CD (GitHub Actions, Jenkins, etc.)

 -Add logging and better exception handling

✅ Features

Page Object Model (POM)

Configurable test data via JSON

Fixtures & setup/teardown with conftest.py

Generates standalone HTML reports

Easily extendable and CI/CD friendly


   

