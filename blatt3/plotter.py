import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self):
        self.id_dataset_calc_line = []
        self.mt_dataset_calc_line = []
        self.id_dataset_calc_square = []
        self.mt_dataset_calc_square = []
    
    def process_file(self, file_name):
        with open(file_name, "r") as file:
            data = file.readlines()
            
        hashtag_seen = False

        for raw_line in data:
            line = raw_line.split()
            if line == []:
                continue
            elif line[0] == "###":
                hashtag_seen = True
            
            elif line[0] == "IDs:" and not hashtag_seen:
                self.id_dataset_calc_line.extend(line[1:])
            elif line[0] == "MTs:" and not hashtag_seen:
                self.mt_dataset_calc_line.extend(line[1:])
                
            elif line[0] == "IDs:" and hashtag_seen:
                self.id_dataset_calc_square.extend(line[1:])
            elif line[0] == "MTs:" and hashtag_seen:
                self.mt_dataset_calc_square.extend(line[1:])
        
        
        print(len(self.id_dataset_calc_line))
        print(len(self.mt_dataset_calc_line))
        print(len(self.id_dataset_calc_square))
        print(len(self.mt_dataset_calc_square))

    

    def plot_data(self):
        x = np.array(self.id_dataset_calc_line, dtype=float)
        y = np.array(self.mt_dataset_calc_line, dtype=float)

        plt.scatter(x, y, marker='o', label='Data points', alpha=0.6)

        # Calculate the regression line
        coefficients = np.polyfit(x, y, 1)
        polynomial = np.poly1d(coefficients)
        y_regression = polynomial(x)

        plt.plot(x, y_regression, color='red', label='Regression line')

        plt.title('Data Points with Regression Line')
        plt.xlabel('ID')
        plt.ylabel('MT')

        plt.grid(True)

        plt.legend()
        plt.gcf().set_size_inches(10, 6)
        plt.show()


if __name__ == '__main__':
    plotter = Plotter()
    plotter.process_file('jan.txt')
    plotter.process_file('george.txt')
    plotter.process_file('kevin.txt')
    plotter.plot_data()
