<<<<<<< HEAD
# Data Science Portfolio 🚀
Repository containing data science projects completed by me for self learning and hobby purposes. Projects contained within one notebook are stored directly in this repo. Larger projects with modular code are stored in separate repos. Take a look at the Contents below and follow the link to the repo / location for each project 🙂

## Contents

### Machine Learning 🤖

__Regression__
* [Regression models to predict the 'score' of a football player](https://github.com/kai-majerus/numpy_regression_from_scratch): I built linear, ridge, lasso and tree regression models in NumPy from scratch to predict the score of a player - small dataset. (In Progress)

### Deep Learning 🧠
* [Driver Drowsiness Detection using CNN Model](https://github.com/willgraham29/project_drowsy): I worked on this project in a group at Le Wagon. We detect whether a driver was drowsy using characteristics of yawning and having closed eyes. Try out the app [here](https://share.streamlit.io/patrickarigg/project_drowsy/cloud-app)

### Data Engineering ⚙
* [Taxi Fare Prediction Model](https://github.com/kai-majerus/TaxiFareModel): I trained a model from the Kaggle New York City Taxi Fare Prediction dataset and built a containerized prediction API deployed on Google Cloud Run and then hosted a [small Streamlit application on Heroku](https://ny-taxi-fare-app.herokuapp.com/) 🌍

### Data Analysis and Visualisation 📊
* [Exploratory analysis of Twitch](https://github.com/kai-majerus/data-science-portfolio/tree/master/01-Data-Analysis-Notebooks): Exploratory analysis of a Twitch dataset collected by myself using the [Twitch API](https://dev.twitch.tv/docs/api). (In Progress)
=======
<!-- Add banner here -->
![Red and Black Thompson Soccer Club Logo](https://user-images.githubusercontent.com/53292276/156609919-ca361c36-85d4-46f0-81c0-ace4919d139d.png)


# Regression From Scratch

This aim of this project is to build multiple regression models from scratch using NumPy rather than scikit-learn. I hope to improve my understanding of 4 regression models (namely, Linear Regression, Ridge Regression, Lasso Regression and Decision Tree Regression) and OOP in doing so.

The dataset that I will be using is a small dataset of ~ 200 football players with 12 feature variables and a target variable of the players 'score'.

Tech stack
* Language - Python
* Libraries - Pandas, NumPy

# Demo-Preview
[(Back to top)](#table-of-contents)

Follow the setup/installation instructions below to install the package and then run the command `numpy_regression_from_scratch-run`. This will run main.py, which trains and saves a model for each of linear, lasso, ridge and tree regression. The output will be the MSE and R2 Score of each model (see example output below). 

![image](https://user-images.githubusercontent.com/53292276/157235956-89a91ace-41ca-4797-bbc6-9bf307e1df5c.png)

# Table of contents

- [Project Title](#regression-from-scratch)
- [Demo-Preview](#demo-preview)
- [Table of contents](#table-of-contents)
- [Startup the project](#startup-the-project)
- [Installation](#installation)
- [Footer](#footer)

# Startup the project
[(Back to top)](#table-of-contents)
The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for numpy_regression_from_scratch in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/numpy_regression_from_scratch`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "numpy_regression_from_scratch"
git remote add origin git@github.com:{group}/numpy_regression_from_scratch.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
numpy_regression_from_scratch-run
```

# Installation
[(Back to top)](#table-of-contents)

Go to `https://github.com/{group}/numpy_regression_from_scratch` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/numpy_regression_from_scratch.git
cd numpy_regression_from_scratch
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
numpy_regression_from_scratch-run
```

# Footer
[(Back to top)](#table-of-contents)

![footer_video](https://user-images.githubusercontent.com/53292276/156608882-fd58c52c-6aec-4710-9544-54529ba4eba0.gif)
>>>>>>> numpy_regression/master
