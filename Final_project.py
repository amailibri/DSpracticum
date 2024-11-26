'''
DS Practicum Final Project
Comparing Homicide Rates in Texas and Illinois
Testing Correlation to Poverty rates over 2012-2022
'''


import matplotlib.pyplot as plt
import pandas as pd
from pandas import pivot


def main():
    illinois = pd.read_csv('Illinois_homicide_data_12-22.csv')
    pivot_columns_illinois = illinois.transpose()
    illinois_homicide = pivot_columns_illinois['query1']

    texas = pd.read_csv('Texas_homicide_data_12-22.csv')
    pivot_columns_texas = texas.transpose()
    texas_homicide = pivot_columns_texas['query1']

    poverty = pd.read_csv('Poverty_data_12-22.csv')

    # Filter poverty data for Illinois and Texas
    illinois_poverty = poverty[poverty['Name'] == 'Illinois']['Percent in Poverty']
    texas_poverty = poverty[poverty['Name'] == 'Texas']['Percent in Poverty']

    # plotting texas data
    plt.scatter(texas_poverty, texas_homicide)
    plt.title("Texas Percentage in Poverty and Homicide Data 2012-2022")
    plt.show()

    #plotting illinois data
    plt.scatter(illinois_poverty, illinois_homicide, color="blue", label="Illinois")
    plt.title("Illinois Percentage in Poverty and Homicide Data 2012-2022")
    plt.show()

    illinois_merge = pd.merge(illinois, poverty,left_on= 'State', right_on='Name')
    correlation = illinois_merge['Homicide Rate'].corr(illinois_merge["Percent in Poverty"])
    print(f"Correlation between poverty and homicide in Illinois: {correlation}")

main()
