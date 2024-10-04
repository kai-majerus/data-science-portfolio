from typing import Annotated, Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from zenml import step


@step(enable_cache=False)
def sklearn_splitter(
    dataset: pd.DataFrame,
    train_size: float = 0.6,
    test_size: float = 0.2,
    eval_size: float = 0.2,
    random_state: int = 42,
    shuffle: bool = True,
) -> Tuple[Annotated[pd.DataFrame, "dataset_train"],
           Annotated[pd.DataFrame, "dataset_test"],
           Annotated[pd.DataFrame, "dataset_eval"]]:
    """Step responsible for splitting the dataset into train, test and eval.

    Args:
        dataset: Full dataset with all the data.
        config: Configuration for the step.

    Returns:
        Tuple of train, test and eval dataframes.
    """

    if shuffle:
        dataset = dataset.sample(frac=1)

    if (train_size + test_size + eval_size) != 1:
        raise ValueError(
            f"Make sure that the ratios sum up to 1. Current "
            f"ratios: {train_size}, {test_size}, {eval_size}"
        )

    dataset_train, dataset_test = train_test_split(
        dataset, test_size=test_size, random_state=random_state
    )

    dataset_train, dataset_eval = train_test_split(
        dataset_train,
        test_size=(
            eval_size
            / (eval_size + train_size)
        ),
        random_state=random_state,
    )

    return (dataset_train, dataset_test, dataset_eval)
