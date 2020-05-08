---
title: model_utils
type: doc
---

# model_utils

#### `binary_roc_graph(y_true, y_pred, **kwargs)`

This function plots a ROC graph of a binary-class predictor. AUC calculation are presented as-well.
Data can be either: (1) one dimensional, where the values of y_true represent the true class and y_pred the
predicted probability of that class, or (2) two-dimensional, where each line in y_true is a one-hot-encoding
of the true class and y_pred holds the predicted probabilities of each class.
For example, consider a data-set of two data-points where the true class of the first line is class 0, which
was predicted with a probability of 0.6, and the second line's true class is 1, with predicted probability of
0.8. In the first configuration, the input will be: y_true = [0,1], y_pred = [0.6,0.8]. In the second
configuration, the input will be: y_true = [[1,0],[0,1]], y_pred = [[0.6,0.4],[0.2,0.8]].

Based on sklearn examples (as was seen on April 2018):
http://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html

- **`y_true`** : `list / NumPy ndarray`

   The true classes of the predicted data
- **`y_pred`** : `list / NumPy ndarray`

   The predicted classes
- **`kwargs`** : `any key-value pairs`

   Different options and configurations

#### `roc_graph(y_true, y_pred, micro=True, macro=True, **kwargs)`

Plot a ROC graph of predictor's results (inclusding AUC scores), where each row of y_true and y_pred
represent a single example.
If there are 1 or two columns only, the data is treated as a binary classification, in which
the result is similar to the `binary_roc_graph` method, see its documentation for more information.
If there are more then 2 columns, each column is considered a unique class, and a ROC graph and AUC
score will be computed for each. A Macro-ROC and Micro-ROC are computed and plotted too by default.

Based on sklearn examples (as was seen on April 2018):
http://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html

**Example:** See `roc_graph_example` under `dython.examples`

- **`y_true`** : `list / NumPy ndarray`

   The true classes of the predicted data
- **`y_pred`** : `list / NumPy ndarray`

   The predicted classes
- **`micro`** : `Boolean` 

  _Default = True_

   Whether to calculate a Micro ROC graph (not applicable for binary cases)
- **`macro`** : `Boolean` 

  _Default = True_

   Whether to calculate a Macro ROC graph (not applicable for binary cases)
- **`kwargs`** : `any key-value pairs`

   Different options and configurations

#### `random_forest_feature_importance(forest, features, **kwargs)`

Given a trained `sklearn.ensemble.RandomForestClassifier`, plot the different features based on their
importance according to the classifier, from the most important to the least.

- **`forest`** : `sklearn.ensemble.RandomForestClassifier`

   A trained `RandomForestClassifier`
- **`features`** : `list`

   A list of the names of the features the classifier was trained on, ordered by the same order the appeared
in the training data
- **`kwargs`** : `any key-value pairs`

   Different options and configurations