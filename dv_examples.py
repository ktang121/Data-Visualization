import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px


class Examples:
    #class variables
    bar_colors = ['cyan', 'gold', 'turquoise', 'forestgreen', 'teal', 'darkorange', 'cornflowerblue', 'purple', 'dimgray'] 
    df_exp = pd.read_csv('LifeExpectancy.csv', delimiter = ',')  


    def bar_example(self):
        self.df_exp.groupby(['Year','Continent'])['LifeExp'].mean().unstack().plot(kind='bar',width = 0.7, color = self.bar_colors, title = 'Life Expectancy per Continent', figsize = (15, 8))
        plt.xticks(rotation = 'horizontal')
        plt.ylabel("Age in Years", labelpad = 14)
        plt.show()
        


    def pie_example(self):
        self.df_exp[self.df_exp['Year'] == 2007].groupby(['Continent'])['GDPPerCap'].sum().plot(kind='pie', autopct = "%.2f%%", colors = self.bar_colors, figsize = (12, 8))
        plt.show()

    
    def line_example(self):
        fig, ax = plt.subplots(figsize = (15,8))
        self.df_exp.cumsum()
        self.df_exp.groupby(['Year', 'Continent'])['Population'].sum().unstack().plot(style = ['c--^', 'o-', '--', '.', 'm+'],kind = 'line', title = 'Population Total By Continent', ax=ax)
        plt.ylabel("Population In Billions", labelpad = 14)
        plt.show()

   
    def scatter_example(self):
        fig = px.scatter(data_frame = self.df_exp[self.df_exp['Year'] == 2007],
                         x = 'GDPPerCap',
                         y = 'LifeExp',
                         size = 'Population',
                         color = 'Continent',
                         hover_name = 'Country',
                         size_max = 60)
        fig.show()

    def motion_example(self):
        fig = px.scatter(data_frame = self.df_exp,
                         x = 'GDPPerCap',
                         y = 'LifeExp',
                         animation_frame = 'Year',
                         animation_group = 'Country',
                         size = 'Population',
                         color = 'Continent',
                         hover_name = 'Country',
                         facet_col = 'Continent',
                         size_max = 45,
                         category_orders ={'Year':list(range(1950, 2010))})
        fig.show()
                         
        
            
if __name__ == '__main__':

    examples = Examples()  
    examples.bar_example() 
    examples.pie_example() 
    examples.line_example()
    examples.scatter_example()
    examples.motion_example()
        
        
        
