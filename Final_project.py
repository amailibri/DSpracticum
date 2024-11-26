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
    illinois_yrs = pivot_columns_illinois['Years']

    texas = pd.read_csv('Texas_homicide_data_12-22.csv')
    pivot_columns_texas = texas.transpose()
    texas_homicide = pivot_columns_texas['query1']
    texas_yrs = pivot_columns_texas['Years']

    poverty = pd.read_csv('Poverty_data_12-22.csv')

    # Filter poverty data for Illinois and Texas
    illinois_poverty = poverty[poverty['Name'] == 'Illinois']['Percent in Poverty']
    illinois_yrs2 = poverty['Year']
    texas_poverty = poverty[poverty['Name'] == 'Texas']['Percent in Poverty']
    texas_yrs2 = poverty['Year']

    # plotting texas data
    plt.scatter(texas_homicide, texas_yrs, color='blue', label='Homicides')
    plt.scatter(texas_poverty, texas_yrs2, color='red', label='Poverty')
    plt.title("Texas Percentage in Poverty and Homicide Data 2012-2022")
    plt.show()

    #plotting illinois data
    plt.scatter(illinois_homicide, illinois_yrs, color="blue", label="Homicides")
    plt.scatter(illinois_poverty, illinois_yrs2, color="red", label="Poverty")
    plt.title("Illinois Percentage in Poverty and Homicide Data 2012-2022")
    plt.show()

    #bar chart?



    illinois_merge = pd.merge(illinois, poverty,left_on= 'State', right_on='Name')
    correlation = illinois_merge['Homicide Rate'].corr(illinois_merge["Percent in Poverty"])
    print(f"Correlation between poverty and homicide in Illinois: {correlation}")

main()
