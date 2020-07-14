from ABMC19.Model.model import *

model = covidModel(20,100,100,2)
for i in range(20):
    model.step()
