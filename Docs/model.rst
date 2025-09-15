Model Used
==========

This project uses several machine learning models to classify student academic success. The following models are used in this project:

1. Feedforward Neural Network (FNN)
=============================

Feedforward Neural Network (FNN) is a simple neural network where data moves in one direction from input to output without loops. It is the most basic neural network model and is used for classification or regression tasks.

Architecture
------------

- **Input layer**: Arranges student data features.
- **Hidden layer**: Uses activation functions like ReLU to capture complex patterns.
- **Output layer**: Produces predictions about the student's academic status (Dropout, Enrolled, Graduate).

Official Website:
-----------------
For more information on Feedforward Neural Networks, visit `TensorFlow - FNN <https://www.tensorflow.org/tutorials/keras/classification>`_.

2. Deep Neural Network (DNN)
=========================

Deep Neural Network (DNN) is a neural network with multiple hidden layers that allows the model to capture more complex patterns in data. DNNs are often used for problems involving very large and complex datasets.

Architecture
------------

- **Input layer**: Organizes student data.
- **Multiple hidden layers**: Uses activation functions to capture more abstract data representations.
- **Output layer**: Presents predictions about the student's academic status.

Official Website:
-----------------
For more information on Deep Neural Networks, visit `TensorFlow - DNN <https://www.tensorflow.org/tutorials/keras/classification>`_.

3. Random Forest
==================

Random Forest is an ensemble algorithm that uses many decision trees to improve model accuracy. Random Forest combines predictions from many tree models trained on different data to produce a more stable and accurate result.

Process
-------

- Many decision trees are built using random samples from the data.
- Predictions from each tree are combined to create the final prediction.

Official Website:
-----------------
For more information on Random Forest, visit `Scikit-learn - Random Forest <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>`_.

Installation
------------

To install TensorFlow, run the following command in your terminal:

.. code-block:: bash

   pip install tensorflow==2.16.2
