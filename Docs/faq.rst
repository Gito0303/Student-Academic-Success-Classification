Frequently Asked Questions (FAQ)
=================================

1. What is the purpose of this project?
---------------------------------------
The purpose of this project is to develop a system that classifies student academic success based on various factors contributing to academic achievement. This system uses models such as **Feedforward Neural Network (FNN)**, **Deep Neural Network (DNN)**, and **Random Forest** to predict the academic success category of students.

2. What models are used in this project?
----------------------------------------
This project uses three models for academic success classification:
- **Feedforward Neural Network (FNN)**
- **Deep Neural Network (DNN)**
- **Random Forest**

3. Where is the dataset sourced from?
-------------------------------------
The dataset used in this project is sourced from:
- **Kaggle**: *Classification with an Academic Success Dataset*
  - Link: [Kaggle - Playground Series S4E6](https://www.kaggle.com/competitions/playground-series-s4e6)
- **UC Irvine Machine Learning Repository**: *Predict Students Dropout and Academic Success*
  - Link: [UC Irvine - Predict Students Dropout and Academic Success](https://archive.ics.uci.edu/ml/datasets/Predict+Students+Dropout+and+Academic+Success)

4. How do I install the necessary dependencies?
------------------------------------------------
To install the necessary dependencies for the project, run the following command:

.. code-block:: bash

   pip install -r requirements.txt

5. How do I use the classification model?
-----------------------------------------
Once the dependencies are installed, you can run the **Streamlit** application to interact with the model.

To start the app, run:

.. code-block:: bash

   streamlit run App.py

6. How can I train the model from scratch?
-------------------------------------------
To train the model from scratch, open the **`Notebook-Model.ipynb`** file and follow the steps provided for training each model.

7. Where can I find more information about the models used?
---------------------------------------------------------
- For **Feedforward Neural Networks**, visit the `TensorFlow - FNN <https://www.tensorflow.org/tutorials/keras/classification>`_.
- For **Deep Neural Networks**, visit the `TensorFlow - DNN <https://www.tensorflow.org/tutorials/keras/classification>`_.
- For **Random Forest**, visit the `Scikit-learn - Random Forest <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>`_.

8. Can I contribute to this project?
-----------------------------------
Yes! Contributions are welcome. Please follow the guidelines for contributing, or submit a pull request with your improvements.

9. What should I do if I encounter an error during installation or usage?
-------------------------------------------------------------------------
If you encounter an error, please make sure:
- All dependencies are installed correctly using `pip install -r requirements.txt`.
- You are using Python 3.x as required for the project.
- If the issue persists, please report it by creating an issue on the GitHub repository.
