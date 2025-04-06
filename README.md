end to end machine learning project

Project Setup Instructions
1. Opening the Project in Visual Studio Code
Open Anaconda Prompt and navigate to your project folder using the cd command.

Run the following command to open the folder in Visual Studio Code:

code .
2. Creating and Activating the Environment
Create a new environment in your folder by running:

conda create -p venv python==3.8 -y
Activate the environment using:

conda activate venv/
Note: Run the activation command in the command prompt within VS Code.

3. Git and GitHub Integration
Initialize Git:

git init
Create and add the README file:

Create your README.md file.

Add and commit the file:

git add README.md
git commit -m "First Commit"
Check Git status:

git status
Set up the remote repository:

git remote add origin https://github.com/flyingriverhorse/mlproject.git
git remote -v
git branch -M main
Push the changes:

git push -u origin main
Verify the connected Git account:

git config --global user.email
Create a .gitignore file:

Add a Python template to ignore unnecessary files.

Sync any remote changes:

git pull
4. Setting Up the Package Structure
Create packaging files:

setup.py: Responsible for packaging your machine learning application.

requirements.txt: Lists all required dependencies.

Purpose:

These files allow you to build your entire ML application as a package and install it in other projects.

Custom Function:

If you have many packages (e.g., 100), consider creating a function to handle them efficiently.

5. Organizing Your Code
Create the source directory:

Make a folder named src and add an __init__.py file to mark it as a package.

Components for Training:

Within src, create a components folder with its own __init__.py file.

This folder will mainly contain modules related to training, pipeline configuration, and prediction.

6. Managing Dependencies and Setup
Automate dependency reading:

In setup.py, include a function to automatically read the requirements.txt file.

Install Dependencies:

pip install -r requirements.txt
Commit your setup changes:

git add .
git commit -m "SETUP"
git push -u origin main
Tip: You can also commit directly from within Visual Studio Code.

7. Additional Development Setup
Error Handling and Logging:

Implement custom exceptions to handle errors.

Set up a logger to record important information.

Testing the Logger:

Run the following command to ensure logging is set up correctly:

python src/logger.py
8. Installing the IPython Kernel
Install the IPython kernel in your environment with:

conda install -p c:\Users\Murat\mlproject\venv ipykernel --update