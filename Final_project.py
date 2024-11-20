import matplotlib as pyplot
import pandas as pd


def main():
    illinois = pd.read_csv('Illinois_homicide_data_12-22.csv')
    pivot_columns_illinois = illinois.transpose()
    print(pivot_columns_illinois)
    texas = pd.read_csv('Texas_homicide_data_12-22.csv')
    pivot_columns_texas = texas.transpose()
    print(pivot_columns_texas)

    poverty = pd.read_csv('Poverty_data_12-22.csv')
    # subset
    in_poverty = poverty['Percent in Poverty']
    print(in_poverty)
main()

