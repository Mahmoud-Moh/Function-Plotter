import numpy as np

class FunctionPlotterModel: 
    def preprocess_eqn(self, eqn): 
        return eqn.replace("x^", "x**")    

    def validate_numbers(self, Xmin, Xmax): 
        """
        This function validates Xmin, Xmax are valid float values.

        Parameters:
            Xmin (str), Xmax (str): raw input of Xmin, Xmax entries.

        Returns:
            int: 0 if ok, 1 if exception happened
            error messsage: if 1 returned in first parameter, error message contains the 
            message that should be showed to user.
        """
        try: 
            Xmin = float(Xmin)
            Xmax = float(Xmax)
        except: 
            if Xmin == "" or Xmax == "":
                return 1, "Please enter Xmin and Xmax."
            elif not isinstance(Xmin, (int, float)) or not isinstance(Xmax, (int, float)): 
                return 1, "Xmin and Xmax should be Numbers."
        return 0, None 
    
    def validate_eqn(self, eqn):
        """
        This function validates Equation.

        Returns:
            int: 0 if ok, 1 if exception happened
        """
        try: 
            x=1
            val = eval(eqn)
        except: 
            return 1, "Enter Function correctly, click the i button to read the guidelines."
        return 0, None
    
    def validate(self, eqn, Xmin, Xmax):
        """
        Validate the equation and numbers.

        Returns:
            tuple: A tuple containing:
                int: 0 if validation is successful, 1 if an exception occurred.
                str: An error message if 1 is returned, containing the message to show to the user.
        """ 
        eqn = self.preprocess_eqn(eqn)
        state1, message1 = self.validate_eqn(eqn)
        state2, message2 = self.validate_numbers(Xmin, Xmax)

        if state2: 
            return 1, message2
        elif state1: 
            return 1, message1
        else: 
            return 0, None 
    
    def get_plot_xys(self, eqn, Xmin, Xmax):
        """
        Plot the graph of the equation.

        Returns:
            x, f(x)
        """ 
        eqn = self.preprocess_eqn(eqn)
        no_of_points = 100
        points_x = np.linspace(Xmin, Xmax, no_of_points)
        y = [0] * no_of_points
        for i in range(no_of_points): 
            x = points_x[i]
            y[i] = eval(eqn)
        return points_x, y