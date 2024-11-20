import matplotlib as pyplot

def load_data(filename):
  with open(filename, "r") as infile:
    homocide_data = []
    line = infile.readline()
    years = line.split(",")
    

