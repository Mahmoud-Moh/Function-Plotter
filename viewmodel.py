from view import DarkThemeWidget
from model import FunctionPlotterModel
class ViewModel:
    def __init__(self) -> None:
        self.view = DarkThemeWidget(self, 800)
        self.view.show()
        self.model = FunctionPlotterModel()
    
    def validate_input(self, eqn, Xmin, Xmax): 
        return self.model.validate(eqn, Xmin, Xmax)
    
    def get_plot_xys(self, eqn, Xmin, Xmax): 
        return self.model.get_plot_xys(eqn, Xmin, Xmax)
