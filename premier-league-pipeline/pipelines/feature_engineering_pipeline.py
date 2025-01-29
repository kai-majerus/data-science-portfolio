
from zenml import pipeline
from zenml.logger import get_logger

from steps.data_loader import data_loader, import_data_offline
from steps.data_splitter import sklearn_splitter

logger = get_logger(__name__)


@pipeline
def feature_engineering(offline: bool):
    """
    Feature engineering pipeline.

    This is a pipeline that loads the data, processes it and splits
    it into train and test sets.

    Args:
        test_size: Size of holdout set for training 0.0..1.0
        drop_na: If `True` NA values will be removed from dataset
        normalize: If `True` dataset will be normalized with MinMaxScaler
        drop_columns: List of columns to drop from dataset
        target: Name of target column in dataset
        random_state: Random state to configure the data loader

    Returns:
        The processed datasets (dataset_trn, dataset_tst).
    """
    # Link all the steps together by calling them and passing the output
    # of one step as the input of the next step.
    if offline:
        raw_data = import_data_offline()
    else:
        raw_data = data_loader()

    # could add a step here that does feature engineering on the whole dataset (e.g. adding new features)

    sklearn_splitter(dataset=raw_data)

    # run data_processor that returns train, test, eval sets with preprocess pipeline
    # preprocess pipeline should be fitted on train set and applied to test and eval sets
