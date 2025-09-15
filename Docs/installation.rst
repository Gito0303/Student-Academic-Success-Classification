Installation Guide
==================

Follow the instructions below to install and set up this project on your local machine.

Prerequisites
-------------

Before starting the installation, make sure you have the following installed:

- **Python**: Version 3.10 or higher is recommended.
  - You can download Python from: `https://www.python.org/downloads/`
  
- **Pip**: A Python package manager for installing dependencies.
  - You can verify if pip is installed by running:
  
    .. code-block:: bash

       pip --version

1. Clone the Repository
-----------------------

First, clone the repository to your local machine using Git:

.. code-block:: bash

   git clone https://github.com/your-username/Student-Academic-Success-Classification.git
   cd Student-Academic-Success-Classification

2. Create a Virtual Environment (Optional but recommended)
---------------------------------------------------------

It's recommended to create a virtual environment to isolate the project dependencies.

- To create a virtual environment, run the following command:

  .. code-block:: bash

     python -m venv venv

- To activate the virtual environment:
  - **On Windows**:

    .. code-block:: bash

       venv\Scripts\activate

  - **On MacOS/Linux**:

    .. code-block:: bash

       source venv/bin/activate

3. Install Dependencies
-----------------------

Once you have activated the virtual environment (or if you are using your system's Python), install the necessary dependencies by running:

.. code-block:: bash

   pip install -r requirements.txt

This will install all the dependencies listed in the **requirements.txt** file.

4. Set Up Configuration Files
-----------------------------

Make sure that the configuration files are properly set up. If any environment variables or special settings are required, follow the instructions in the **README.md** or **config.py** files.

5. Run the Application
-----------------------

After installing all dependencies, you can start the application using **Streamlit**.

- To run the app, use the following command:

  .. code-block:: bash

     streamlit run App.py

The application should now be live on your local server. You can access it in your browser by visiting: `http://localhost:8501`

6. Running the Model from Scratch
---------------------------------

If you want to train the models from scratch, follow these steps:

- Open **Notebook-Model.ipynb** and follow the instructions in the notebook to train the **Feedforward Neural Network (FNN)**, **Deep Neural Network (DNN)**, and **Random Forest** models.

7. Troubleshooting
------------------

If you run into any issues during installation or running the app, check the following:

- Ensure that all dependencies are installed correctly.
- Verify that you're using the correct version of Python (preferably 3.10 or higher).
- Check the **`requirements.txt`** file to make sure all dependencies are included.
- If problems persist, create an issue on the GitHub repository, and we will assist you further.

Thank you for using the Student Academic Success Classification project!
