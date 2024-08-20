# Selenium Python tests for Luma

# Note
Tests will be executed in Microsoft Edge.

# Requirements

* Python 3
* pip
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>)

# Installation

1. Clone the repository 
2. Open a terminal
3. Go to the project root directory.
4. Create a virtual environment: `python -m venv venv`
5. Activate the virtual environment: `.\venv\Scripts\activate`
6. Install the required libraries:  `pip install -r requirements.txt`

# Test Execution

1. Open a terminal
2. Navigate to the root directory of the project
3. Run: `pytest .\Tests\scenarios_tests.py --html=results/report.html`

# Results

After the tests are done executing, the results can be found in 'results/report.html' file.
