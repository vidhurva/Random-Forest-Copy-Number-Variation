from sklearn import RandomForestClassifier
from sklearn import metrics

model = RandomForestClassifier(n_estimators = 100, max_features = 'sqrt')

model.fit(x, y)

#Can implement functions from metrics in order to compare the accuracy of measured to predicted data
 
