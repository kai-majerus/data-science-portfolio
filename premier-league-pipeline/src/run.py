import logging
from typing import Annotated, Tuple

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from zenml import (ArtifactConfig, Model, get_step_context, log_model_metadata,
                   pipeline, step)

zen_model = Model(
    # The name uniquely identifies this model
    # It usually represents the business use case
    name="iris_classifier",
    # The version specifies the version
    # If None or an unseen version is specified, it will be created
    # Otherwise, a version will be fetched.
    version="0.0.1",
    # Some other properties may be specified
    license="Apache 2.0",
    description="A classification model for the iris dataset.",
)


@step
def training_data_loader() -> Tuple[
    # Notice we use a Tuple and Annotated to return
    # multiple named outputs
    Annotated[pd.DataFrame, ArtifactConfig(name="X_train")],
    Annotated[pd.DataFrame, "X_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"],
]:
    """Load the iris dataset as a tuple of Pandas DataFrame / Series."""
    logging.info("Loading iris...")
    iris = load_iris(as_frame=True)
    logging.info("Splitting train and test...")
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, shuffle=True, random_state=42  # type: ignore
    )
    return X_train, X_test, y_train, y_test


@step
def svc_trainer(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    gamma: float = 0.001,
) -> tuple[
    Annotated[SVC, "trained_model"],
    Annotated[float, "training_acc"],
]:
    """Train a sklearn SVC classifier."""

    model = SVC(gamma=gamma)
    model.fit(X_train.to_numpy(), y_train.to_numpy())

    train_acc = float(model.score(X_train.to_numpy(), y_train.to_numpy()))
    print(f"Train accuracy: {train_acc}")

    get_step_context().model

    log_model_metadata(
        # Model name can be omitted if specified in the step or pipeline context
        model_name="iris_classifier",
        # Passing None or omitting this will use the `latest` version
        model_version=None,
        # Metadata should be a dictionary of JSON-serializable values
        metadata={"accuracy": float(train_acc)}
        # A dictionary of dictionaries can also be passed to group metadata
        #  in the dashboard
        # metadata = {"metrics": {"accuracy": accuracy}}
    )

    return model, train_acc


@pipeline(enable_cache=True, model=zen_model)  # type: ignore
def training_pipeline(gamma: float = 0.002):
    X_train, X_test, y_train, y_test = training_data_loader()
    svc_trainer(gamma=gamma, X_train=X_train, y_train=y_train)


if __name__ == "__main__":

    # Configure the pipeline
    training_pipeline = training_pipeline.with_options(
        config_path='../configs/training.yaml'
    )

    # training_pipeline.write_run_configuration_template(path='../configs/template.yaml')

    # Run the pipeline
    training_pipeline()
