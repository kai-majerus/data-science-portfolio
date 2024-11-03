

# get dataset by id , otherwise run feature engineering pipeline
# train the model with hp tuning (train on train set with hp grid search, and evaluate on eval set)
# choose the model with the best eval score
# evaluate the model on the test set and log this as the model performance
# if the model performance on the test set is better than the current best model,
# promote the new model (this could happen in my project by adding new features etc, new preprocessing techniques)
