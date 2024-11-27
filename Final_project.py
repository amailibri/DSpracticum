'''
DS Practicum Final Project
Comparing Homicide Rates in Texas and Illinois
Testing Correlation to Poverty rates over 2012-2022
'''


import matplotlib.pyplot as plt
import pandas as pd

def main():
    
    illinois = pd.read_csv('Illinois_homicide_data_12-22.csv')
    # shifting the orientation of the data to be able to use pandas to subset
    pivot_columns_illinois = illinois.transpose()

    print(pivot_columns_illinois.columns)
    illinois_yrs = pivot_columns_illinois[0]
    # the labels aren't placed as labels in the data frame so we either need to call the number of the index or
    # somehow make it not aprt of the index
    print(illinois_yrs.index)
    illinois_homicide = pivot_columns_illinois[1]
    print(illinois_homicide)

    #trying to figure out the problem with the first data set then we can just apply to the second
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
    
    # bar chart?
    #not sure how we want to write it i was thinking years on the x and height of poverty on the y
    # both states included in one?
    plt.bar(illinois_yrs2, illinois_poverty, width=0.8)
    plt.bar(texas_yrs2, texas_poverty, width=0.8)
    plt.show()

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


    #not sure if this is how we want to use the poverty data, but it's an idea
    #prob need better documentation in order to use .merge and .corr
    illinois_merge = pd.merge(illinois, poverty,left_on= 'State', right_on='Name')
    correlation = illinois_merge['Homicide Rate'].corr(illinois_merge["Percent in Poverty"])
    print(f"Correlation between poverty and homicide in Illinois: {correlation}")


main()
