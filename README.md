# Plotter Application with PySide2 and Matplotlib

![Plotter](plotter.png)

## Introduction

This is a simple python Function Plotter application that allows users to plot mathematical functions using PySide2 for the GUI and Matplotlib for the plotting. With this application, users can visualize various mathematical functions and their curves by entering the equation and specifying the range for the x-axis.

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
