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

    

    def plot_data(self, calc_type):
        if calc_type == "horizontal":
            id_dataset = self.id_dataset_calc_line
            mt_dataset = self.mt_dataset_calc_line
        elif calc_type == "compact":
            id_dataset = self.id_dataset_calc_square
            mt_dataset = self.mt_dataset_calc_square
        
        x = np.array(id_dataset, dtype=float)
        y = np.array(mt_dataset, dtype=float)

        plt.scatter(x, y, marker='o', label='Data points', alpha=0.6)

        b, a = np.polyfit(x, y, 1)
        print(f"a: {a}, b: {b}")
        
        y_pred = a + b * x
        plt.plot(x, y_pred, color='red', label='Regression line')
        
        plt.title(f'Index of Difficulty and Movement Time for {calc_type} calculator')
        plt.xlabel('ID')
        plt.ylabel('MT')

        plt.grid(True)

        plt.legend()
        plt.gcf().set_size_inches(10, 6)
        plt.show()


if __name__ == '__main__':
    """plotter = Plotter()
    plotter.process_file('blatt3/jan.txt')
    plotter.process_file('blatt3/george.txt')
    plotter.process_file('blatt3/kevin.txt')
    plotter.plot_data("compact")"""
    
    
    
    my_string = "Es ist zu erkennen, dass beim horizontalen Layout mit zunehmendem Index of Difficulty auch die Movement Time steigt. Beim kompakten Layout nimmt die Movement Time hingegen weniger stark zu. Dies könnte darauf zurückzuführen sein, dass die Tasten im horizontalen Layout teils sehr weit auseinanderliegen, während sie im kompakten Layout relativ nahe beieinander angeordnet sind. Folglich ist der kompakte Calculator im Durchschnitt hinsichtlich der Schreibgeschwindigkeit konstant schnell, unabhängig von der Höhe des Index of Difficulty, was ihn zu einer benutzerfreundlicheren und effizienteren GUI macht. Dies verdeutlicht, dass eine engere Anordnung der Tasten die Benutzerfreundlichkeit und Effizienz des Interfaces erheblich verbessert."


    print(len(my_string.split()))