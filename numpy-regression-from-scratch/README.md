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

# Installation
[(Back to top)](#table-of-contents)


Create a python3 virtualenv and activate it:

```bash
pyenv virtualenv 3.11.5 numpy-regression-from-scratch
```

Clone the project and install it:

```bash
git clone git@github.com:kai-majerus/data-science-portfolio.git
pyenv virtualenv 3.11.5 numpy-regression-from-scratch
cd numpy_regression_from_scratch
pyenv local numpy-regression-from-scratch
pip install -r requirements.txt
python scripts/numpy_regression_from_scratch-run.py
```

# Footer
[(Back to top)](#table-of-contents)

![footer_video](https://user-images.githubusercontent.com/53292276/156608882-fd58c52c-6aec-4710-9544-54529ba4eba0.gif)
>>>>>>> numpy_regression/master
