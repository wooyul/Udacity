#!/usr/bin/python

import sys
import pickle

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.feature_selection import SelectKBest
from sklearn.cross_validation import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier

PERF_FORMAT_STRING = "\
\tAccuracy: {:>0.{display_precision}f}\tPrecision: {:>0.{display_precision}f}\t\
Recall: {:>0.{display_precision}f}\tF1: {:>0.{display_precision}f}\tF2: {:>0.{display_precision}f}"
RESULTS_FORMAT_STRING = "\tTotal predictions: {:4d}\tTrue positives: {:4d}\tFalse positives: {:4d}\
\tFalse negatives: {:4d}\tTrue negatives: {:4d}"

def test_classifier(clf, dataset, feature_list, folds = 1000):
    data = featureFormat(dataset, feature_list, sort_keys = True)
    labels, features = targetFeatureSplit(data)
    cv = StratifiedShuffleSplit(labels, folds, random_state = 42)
    true_negatives = 0
    false_negatives = 0
    true_positives = 0
    false_positives = 0
    for train_idx, test_idx in cv:
        features_train = []
        features_test  = []
        labels_train   = []
        labels_test    = []
        for ii in train_idx:
            features_train.append( features[ii] )
            labels_train.append( labels[ii] )
        for jj in test_idx:
            features_test.append( features[jj] )
            labels_test.append( labels[jj] )

        ### fit the classifier using training set, and test on test set
        clf.fit(features_train, labels_train)
        predictions = clf.predict(features_test)
        for prediction, truth in zip(predictions, labels_test):
            if prediction == 0 and truth == 0:
                true_negatives += 1
            elif prediction == 0 and truth == 1:
                false_negatives += 1
            elif prediction == 1 and truth == 0:
                false_positives += 1
            elif prediction == 1 and truth == 1:
                true_positives += 1
            else:
                print "Warning: Found a predicted label not == 0 or 1."
                print "All predictions should take value 0 or 1."
                print "Evaluating performance for processed predictions:"
                break
    try:
        total_predictions = true_negatives + false_negatives + false_positives + true_positives
        accuracy = 1.0*(true_positives + true_negatives)/total_predictions
        precision = 1.0*true_positives/(true_positives+false_positives)
        recall = 1.0*true_positives/(true_positives+false_negatives)
        f1 = 2.0 * true_positives/(2*true_positives + false_positives+false_negatives)
        f2 = (1+2.0*2.0) * precision*recall/(4*precision + recall)
        print PERF_FORMAT_STRING.format(accuracy, precision, recall, f1, f2, display_precision = 5)
        print RESULTS_FORMAT_STRING.format(total_predictions, true_positives, false_positives, false_negatives, true_negatives)
        print ""
    except:
        print "Got a divide by zero when trying out:", clf
        print "Precision or recall may be undefined due to a lack of true positive predicitons."


### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

all_features = ['poi', 'salary', 'deferral_payments', 'total_payments',
               'exercised_stock_options', 'bonus', 'restricted_stock', 'shared_receipt_with_poi',
               'restricted_stock_deferred', 'total_stock_value', 'expenses', 'loan_advances',
               'from_messages', 'other', 'from_this_person_to_poi', 'director_fees',
               'deferred_income','long_term_incentive', 'from_poi_to_this_person' , 'to_messages']

### Remove invalid features due to a large number of missing values
features_removed = ['deferral_payments', 'restricted_stock_deferred','loan_advances',
                    'director_fees', 'deferred_income']

for feature in features_removed:
    all_features.remove(feature)

### Load the dictionary containing the dataset

with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
del data_dict['TOTAL']

### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict

all_features.append('from_poi_to_this_person_rate')
all_features.append('from_this_person_to_poi_rate')
for key in my_dataset.keys():

    ### Create a new feature - from_poi_to_this_person_rate
    if (my_dataset[key]['from_poi_to_this_person'] != 'NaN'
        and my_dataset[key]['to_messages'] != 'NaN'
        and my_dataset[key]['to_messages'] > 0):
        my_dataset[key]['from_poi_to_this_person_rate'] = \
            float(my_dataset[key]['from_poi_to_this_person'])/my_dataset[key]['to_messages']
    else:
        my_dataset[key]['from_poi_to_this_person_rate'] = 'NaN'

    ### Create a new feature - from_this_person_to_poi_rate
    if (my_dataset[key]['from_this_person_to_poi'] != 'NaN'
        and my_dataset[key]['from_messages'] != 'NaN'
        and my_dataset[key]['from_messages'] > 0):
        my_dataset[key]['from_this_person_to_poi_rate'] = \
            float(my_dataset[key]['from_this_person_to_poi'])/my_dataset[key]['from_messages']
    else:
        my_dataset[key]['from_this_person_to_poi_rate'] = 'NaN'

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, all_features, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Split the training data. This is only used in a feature selection.
### Evaluate the classifier at the end using StratifiedShuffleSplit in test_classfier()
### instead of using these data sets
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

###Feature selection
num_features = 6
fs = SelectKBest(k=num_features)
features_selected = fs.fit_transform(features_train, labels_train)
features_list = [all_features[0]]
for i in fs.get_support(indices=True):
    features_list.append(all_features[i+1])
    print all_features[i+1],"=", fs.scores_[i]
print "Selected features by SelectBest(k =", num_features,"), = ", features_list

### Task 4: Try a variety of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

### Decision tree



clf = DecisionTreeClassifier(min_samples_split = 1, min_samples_leaf = 1, random_state=42)

### Random forest
# from sklearn.ensemble import RandomForestClassifier
# clf = RandomForestClassifier(min_samples_split=5, n_estimators=6)

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script.

### Grid search of the best parameters for random forest using test_classifier
# for min_samples_split in range(1,5):
#     for n_estimators in range(1,10):
#         clf = RandomForestClassifier(min_samples_split = min_samples_split, n_estimators=n_estimators)
#         print min_samples_split, n_estimators, test_classifier(clf, my_dataset, features_list, folds = 1000)

### Grid search of the best parameters for decision tree classifier using test_classifier
# for min_samples_split in range(1,2):
#     for min_samples_leaf in range(1,2):
#             clf = DecisionTreeClassifier(min_samples_split = min_samples_split,
#                                          min_samples_leaf = min_samples_leaf)
#             print min_samples_split, min_samples_leaf, test_classifier(clf, my_dataset, features_list, folds = 1000)
#

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)

