# Plotter Application with PySide2 and Matplotlib

![Plotter](plotter.png)

## Introduction

This is a simple Python application called "Plotter" that allows users to plot mathematical functions using PySide2 for the GUI and Matplotlib for the plotting. With this application, users can visualize various mathematical functions and their curves by entering the equation and specifying the range for the x-axis.

## Features

- Plot mathematical functions with a given equation.
- Specify the range for the x-axis (Xmin and Xmax).
- Dark theme interface for a pleasant user experience.

## Requirements

To run the Plotter application, you'll need the following:

- Python 3.x
- PySide2
- NumPy
- Matplotlib

Install the required dependencies using the following command:

``` pip install PySide2 numpy matplotlib ```


## How to Use

1. Run the application by executing the script. A window will appear with the dark-themed user interface.

2. Enter the equation of the function in the "Equation" field. The supported operators are +, -, /, *, and ^ for exponentiation.

3. Specify the range for the x-axis by entering the minimum and maximum values in the "Xmin" and "Xmax" fields, respectively.

4. Click the "Plot" button to visualize the function's curve on the canvas.

5. If you encounter any errors, an error message will be shown in a pop-up window.

## Guidelines for Equation Entry

1. The equation should only contain the supported operators (+, -, /, *, ^) and the variable "x".

2. Example of valid functions:
   - x^3 + (1/5)*x^2 + 3*x + 1
   - -(x-4)^2/(x-6)
   - -5

3. Example of invalid functions:
   - x^3 +
   - -f(x)=(x-4)^2/(x-6)
   - -3x (remember to put * with scalars, correct form is 3*x)

4. Division by zero is handled, so you don't need to worry about that.

## Instructions

If you need further assistance on how to use the application or encounter any issues, you can refer to the "Instructions" page. It contains important guidelines and examples for valid and invalid functions.

## Note

Please note that this application was last updated in 2021, and the technology landscape might have changed since then. If you encounter any compatibility issues or have suggestions for improvements, feel free to contribute or open an issue on GitHub.

## Credits

This application was created by [Your Name]. You can find the source code and contribute on GitHub: [GitHub Repository URL]

---

The code provided above demonstrates a simple Plotter application that uses PySide2 for the GUI and Matplotlib for plotting. You can create a GitHub repository and include the code in a file named `plotter.py`. Add the necessary setup and installation instructions in the README to help users set up and run the application. Make sure to replace `[Your Name]` and `[GitHub Repository URL]` with your actual name and GitHub repository URL, respectively.

Additionally, you might want to add screenshots or images to the README to provide users with a visual representation of the application's interface. Feel free to customize the README to suit your preferences and include any additional information that might be helpful to potential users and contributors.
