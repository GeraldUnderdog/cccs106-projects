# Lab 1 Report: Environment Setup and Python Basics

**Student Name:** [Parro, Carl Gerald J.]  
**Student ID:** [231002334]  
**Section:** [BSCS3A]  
**Date:** [August 27, 2025]  

---

## Environment Setup

### Python Installation
- **Python Version:** 3.11.5  
- **Installation Issues:** No major issues. I only needed to ensure that *“Add Python to PATH”* was checked during installation. After restarting the Command Prompt, `python --version` worked correctly.  
- **Virtual Environment Created:** ✅ `cccs106_env_parro`  

### VS Code Configuration
- **VS Code Version:** 1.82.0  
- **Python Extension:** ✅ Installed and configured  
- **Interpreter:** ✅ Set to `.\cccs106_env_parro\Scripts\python.exe`  

### Package Installation
- **Flet Version:** 0.28.3  
- **Other Packages:** None at this time  

---

## Programs Created

### 1. `hello_world.py`
- **Status:** ✅ Completed  
- **Features:**  
  - Displays formatted headers and welcome message  
  - Prints student information (name, ID, program, year level)  
  - Performs age calculation based on birth year  
  - Shows Python version and platform info  
- **Notes:** Straightforward to implement. The f-string formatting made it easy to print variables neatly.  

### 2. `basic_calculator.py`
- **Status:** ✅ Completed  
- **Features:**  
  - Accepts two numbers as input  
  - Performs addition, subtraction, multiplication, and safe division (handles divide by zero)  
  - Displays larger/smaller number  
  - Includes error handling for invalid inputs  
- **Notes:** Had to use `try-except` for handling invalid input, which improved program reliability.  

---

## Challenges and Solutions
- **Challenge:** Remembering to activate the virtual environment before running programs.  
  - **Solution:** Added a sticky note reminder and always check `(cccs106_env_parro)` is visible in the terminal before running Python.  
- **Challenge:** Handling invalid input in the calculator.  
  - **Solution:** Used `try-except` to catch `ValueError` and display an error message.  
- **Challenge:** Setting the interpreter in VS Code.  
  - **Solution:** Used *Command Palette → Python: Select Interpreter* to point to the virtual environment.  

---

## Learning Outcomes
Through this lab, I learned how to:  
- Install and configure Python properly, including PATH setup.  
- Create and manage virtual environments for organized development.  
- Configure VS Code with extensions and custom settings for Python projects.  
- Write simple but structured Python programs that use variables, input/output, calculations, and error handling.  
- Apply basic debugging and troubleshooting practices when encountering setup or runtime issues.  

Overall, this lab gave me confidence in setting up my programming environment and writing my very first Python applications.  

---

## Screenshots

- **Environment Setup:**  
  ![Environment Setup](lab1_screenshots/environment_setup.png)

- **VS Code Setup:**  
  ![VS Code Setup](lab1_screenshots/vscode_setup.png)

- **Hello World Output:**  
  ![Hello World Output](lab1_screenshots/hello_world_output.png)

- **Basic Calculator Output:**  
  ![Basic Calculator Output](lab1_screenshots/basic_calculator_output.png)

