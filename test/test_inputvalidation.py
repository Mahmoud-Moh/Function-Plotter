import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pyside_v1 import InputValidation

@pytest.mark.parametrize(
    ('eqn', 'Xmin', 'Xmax', 'expected_result'), 
    (("x^2", "-5", "5", (0, None)),
    ("x^3+3*x", "", "", (1, "Please enter Xmin and Xmax.")),
    ("x*x", "5", "100",(0, None)),
    ("x*x", "", "100",(1,  "Please enter Xmin and Xmax.")),
    ("x^5 + (1/5)*x", "google", "5", (1, "Xmin and Xmax should be Numbers.")),
    ("(1/0)*x", "4", "100", (1, "Enter Function correctly, click the i button to read the guidelines." )),
    ("x/(x-4)", "-10", "10", (0, None)),
    ("2*x^3 - 5*x^2 + 7*x - 10", "-3", "3", (0, None)),
    ("3.14*x^2 + 2.5*x - 1.2", "-5.5", "5.5", (0, None)),
    ("x^3 - x^2 + 3*x/2 - 1", "-2", "2", (0, None)),
    ("2x^2 + 3x -", "4", "10", (1, "Enter Function correctly, click the i button to read the guidelines.")),
    ("x^3 + x^2 + x + 1", "a", "5", (1, "Xmin and Xmax should be Numbers.")),
    ("2x^2 + 3x - 4", "-4", "4", (1, "Enter Function correctly, click the i button to read the guidelines.")),
    ("(x^2 + 3) / x", "0", "5", (0, None)),
    )
)
def test_inputvalidation(eqn, Xmin, Xmax, expected_result): 
    inputValidation = InputValidation(eqn, Xmin, Xmax)
    result = inputValidation.validate()
    assert result == expected_result