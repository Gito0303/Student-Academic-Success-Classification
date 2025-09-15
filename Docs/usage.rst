Usage Guide
============

This guide will help you understand how to use the **Student Academic Success Classification** model.

Interactive Web Application
----------------------------

You can interact with the model through a **Streamlit** web application. The interactive application allows you to input student data and predict the academic success classification.

Access the interactive application at the following link:

**[Student Academic Success Classification App](https://student-academic-success-classification-ga83d9v6nvvbsz7akry2mo.streamlit.app/)**

Running the Application Locally
-------------------------------

To run the application locally on your machine, follow these steps:

1. Clone the repository to your local machine:

   .. code-block:: bash

      git clone https://github.com/your-username/Student-Academic-Success-Classification.git
      cd Student-Academic-Success-Classification

2. Install the necessary dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

3. Start the Streamlit app:

   .. code-block:: bash

      streamlit run App.py

After running the app, open your browser and visit `http://localhost:8501` to interact with the application.

Using the Model
---------------

Once the application is running, follow these steps to classify student academic success:

1. **Input Data**: 
   - You will be prompted to input several features such as marital status, attendance mode, parent's qualification, financial factors, and age during registration.
   
2. **Run Prediction**:
   - Once all the required data is entered, click the **Predict** button to classify the student's academic success. The result will show whether the student is likely to **Dropout**, **Graduate**, or **Be Enrolled**.

3. **Visualizations**:
   - The app also displays visualizations such as graphs and metrics to show the model's prediction confidence and distribution.

Training the Model
------------------

If you want to train the model from scratch, open the **Notebook-Model.ipynb** file in Jupyter and follow the instructions to train the **Feedforward Neural Network (FNN)**, **Deep Neural Network (DNN)**, and **Random Forest** models.

For more information on how the models are trained and the steps involved, please refer to the **Notebook-Model.ipynb**.

Troubleshooting
---------------

If you run into any issues during the usage of the app:

- Ensure all dependencies are installed correctly.
- Make sure you're using the required version of Python.
- If problems persist, refer to the **Troubleshooting** section in **installation.rst** or report the issue on the GitHub repository.
