# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:22:29 2018

@author: ankitjha67
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(10)
pd.set_option('chained_assignment',None)

read = pd.read_csv("C:/Users/ankitjha67/Downloads/gramener-usecase-nas/nas-pupil-marks.csv")
definex = read[['STUID', 'State']]

nd = read[['Gender', 'Age', 'Category',
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
       'Maths %', 'Reading %', 'Science %', 'Social %']]

nd['Use computer'] = nd['Use computer'].map({"Yes":1,"No":0})
nd['Subjects'] = nd['Subjects'].map({'L':1, 'S':2, 'O':3, 'M':4, '0':0})


from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(nd)
tx = imp.transform(nd) 
dc=['Gender', 'Age', 'Category',
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
data = pd.DataFrame(tx,columns=dc)
math1    = np.array(data["Maths %"]).astype("float")
reading1 = np.array(data["Reading %"]).astype("float")
Science1 = np.array(data["Science %"]).astype("float")
Social1  = np.array(data["Social %"]).astype("float")
performance1 = (math1+reading1+Science1+Social1)

bestPerformance1 = np.max(performance1)
poorPerformance1 = np.min(performance1)
avgPerformance1  = np.average(performance1)


Threshold1 = bestPerformance1-avgPerformance1
super_threshold_indices = performance1 > Threshold1
h = np.copy(performance1)
h[super_threshold_indices] = 1
h[~super_threshold_indices]= 0

performance1 = pd.DataFrame(performance1,columns=["performance1"])
Stclass1     = pd.DataFrame(h,columns=["Stclass1"])
modDof = pd.concat([data,performance,Stclass1],axis=1)
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

X1 = Xdata1.astype("float")
X1 = np.array(X1)
y1 = lable1.astype("float")
y1 = np.array(y1)
from sklearn.ensemble import ExtraTreesClassifier
np.random.seed(1)
model1 = ExtraTreesClassifier()
model1.fit(X1, y1)
feature_importance1 = model1.feature_importances_
print(model1.feature_importances_)

feature_importance1 = 100.0 * (feature_importance1 / feature_importance1.max())
sorted_idx1 = np.argsort(feature_importance1)
pos1 = np.arange(sorted_idx1.shape[0]) + .8
plt.barh(pos1, feature_importance1[sorted_idx1], align='center')
plt.yticks(pos1, Xdata1.columns[sorted_idx1])
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.savefig("feature_importance.png")