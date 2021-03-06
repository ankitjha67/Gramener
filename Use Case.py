# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 00:37:56 2018

@author: ankitjha67
"""

import pandas as pd # import pandas
import numpy as np # import numpy # import matplot
import matplotlib.pyplot as plt # import seaborn for visualization
import seaborn as sns # import seaborn for visualization
np.random.seed(10) # seed set to 10
pd.set_option('chained_assignment',None)

read = pd.read_csv("C:/Users/ankitjha67/Downloads/gramener-usecase-nas/nas-pupil-marks.csv") # read the file
definex = read[['STUID', 'State']]

read1 = read[['Gender', 'Age', 'Category',
       'Same language', 'Siblings', 'Handicap', 'Father edu', 'Mother edu',
       'Father occupation', 'Mother occupation', 'Below poverty',
       'Use calculator', 'Use computer', 'Use Internet', 'Use dictionary',
       'Read other books', '# Books', 'Distance', 'Computer use',
       'Library use', 'Like school', 'Subjects', 'Give Lang HW',
       'Give Math HW', 'Give Scie HW', 'Give SoSc HW', 'Correct Lang HW',
       'Correct Math HW', 'Correct Scie HW', 'Correct SocS HW',
       'Help in Study', 'Private tuition', 'English is difficult',
       'Read English', 'Dictionary to learn', 'Answer English WB',
       'Answer English aloud', 'Maths is difficult', 'Solve Maths',
       'Solve Maths in groups', 'Draw geometry', 'Explain answers',
       'SocSci is difficult', 'Historical excursions', 'Participate in SocSci',
       'Small groups in SocSci', 'Express SocSci views',
       'Science is difficult', 'Observe experiments', 'Conduct experiments',
       'Solve science problems', 'Express science views', 'Watch TV',
       'Read magazine', 'Read a book', 'Play games', 'Help in household',
       'Maths %', 'Reading %', 'Science %', 'Social %']] # read all columns

read1['Use computer'] = read1['Use computer'].map({"Yes":1,"No":0})
read1['Subjects'] = read1['Subjects'].map({'L':1, 'S':2, 'O':3, 'M':4, '0':0})


from sklearn.preprocessing import Imputer # imputer to remove missing value
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(nd)
tx = imp.transform(nd) 
bh=['Gender', 'Age', 'Category',
       'Same language', 'Siblings', 'Handicap', 'Father edu', 'Mother edu',
       'Father occupation', 'Mother occupation', 'Below poverty',
       'Use calculator', 'Use computer', 'Use Internet', 'Use dictionary',
       'Read other books', '# Books', 'Distance', 'Computer use',
       'Library use', 'Like school', 'Subjects', 'Give Lang HW',
       'Give Math HW', 'Give Scie HW', 'Give SoSc HW', 'Correct Lang HW',
       'Correct Math HW', 'Correct Scie HW', 'Correct SocS HW',
       'Help in Study', 'Private tuition', 'English is difficult',
       'Read English', 'Dictionary to learn', 'Answer English WB',
       'Answer English aloud', 'Maths is difficult', 'Solve Maths',
       'Solve Maths in groups', 'Draw geometry', 'Explain answers',
       'SocSci is difficult', 'Historical excursions', 'Participate in SocSci',
       'Small groups in SocSci', 'Express SocSci views',
       'Science is difficult', 'Observe experiments', 'Conduct experiments',
       'Solve science problems', 'Express science views', 'Watch TV',
       'Read magazine', 'Read a book', 'Play games', 'Help in household',
       'Maths %', 'Reading %', 'Science %', 'Social %']
data1 = pd.DataFrame(tx,columns=dc)
math1    = np.array(data1["Maths %"]).astype("float")
reading1 = np.array(data1["Reading %"]).astype("float")
Science1 = np.array(data1["Science %"]).astype("float")
Social1  = np.array(data1["Social %"]).astype("float")
performance1 = (math1+reading1+Science1+Social1) # add all subjects

bestPerformance1 = np.max(performance1) # max marks
poorPerformance1 = np.min(performance1) # min marks
avgPerformance1  = np.average(performance1) # average marks


Threshold1 = bestPerformance1-avgPerformance1 # set threshold
super_threshold_indices = performance1 > Threshold1
h = np.copy(performance1)
h[super_threshold_indices] = 1
h[~super_threshold_indices]= 0

performance1 = pd.DataFrame(performance1,columns=["performance1"])
Stclass1     = pd.DataFrame(h,columns=["Stclass1"])
modDof = pd.concat([data1,performance,Stclass1],axis=1)
lable1 = modDof['Stclass1']
Xdata1 = modDof[['Gender', 'Age', 'Category','Same language', 'Siblings', 'Handicap', 'Father edu', 'Mother edu',
       'Father occupation', 'Mother occupation', 'Below poverty',
       'Use calculator', 'Use computer', 'Use Internet', 'Use dictionary',
       'Read other books', '# Books', 'Distance', 'Computer use',
       'Library use', 'Like school', 'Subjects', 'Give Lang HW',
       'Give Math HW', 'Give Scie HW', 'Give SoSc HW', 'Correct Lang HW',
       'Correct Math HW', 'Correct Scie HW', 'Correct SocS HW',
       'Help in Study', 'Private tuition', 'English is difficult',
       'Read English', 'Dictionary to learn', 'Answer English WB',
       'Answer English aloud', 'Maths is difficult', 'Solve Maths',
       'Solve Maths in groups', 'Draw geometry', 'Explain answers',
       'SocSci is difficult', 'Historical excursions', 'Participate in SocSci',
       'Small groups in SocSci', 'Express SocSci views',
       'Science is difficult', 'Observe experiments', 'Conduct experiments',
       'Solve science problems', 'Express science views', 'Watch TV',
       'Read magazine', 'Read a book', 'Play games', 'Help in household']]

X1 = Xdata1.astype("float") # casting to float
X1 = np.array(X1)
y1 = lable1.astype("float")
y1 = np.array(y1)
from sklearn.ensemble import ExtraTreesClassifier # to improve predicting
np.random.seed(10)
model1 = ExtraTreesClassifier()
model1.fit(X1, y1)
feature_importance1 = model1.feature_importances_
print(model1.feature_importances_)

feature_importance1 = 100.0 * (feature_importance1 / feature_importance1.max())
sorted_idx2 = np.argsort(feature_importance1) # sort an array
pos1 = np.arange(sorted_idx2.shape[0]) + .8 # arrange
plt.barh(pos1, feature_importance1[sorted_idx2], align='center')
plt.yticks(pos1, Xdata1.columns[sorted_idx2])
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.savefig("feature_importance.png")