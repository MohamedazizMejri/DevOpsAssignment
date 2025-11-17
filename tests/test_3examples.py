import sys
import os


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def test_training_sets_flag_true():
    from src.model import IrisClassifier
    from src.data_loader import load_iris_data

    X_train, X_test, y_train, y_test = load_iris_data()

    clf = IrisClassifier()
    clf.train(X_train, y_train)

    assert clf.is_trained is True, "Model should set is_trained=True after training"


def test_predictions_are_valid_classes():
    from src.model import IrisClassifier
    from src.data_loader import load_iris_data
    import numpy as np

    X_train, X_test, y_train, y_test = load_iris_data()

    clf = IrisClassifier()
    clf.train(X_train, y_train)

    preds = clf.predict(X_test[:5])

    assert isinstance(preds, np.ndarray)
    assert set(preds).issubset({0, 1, 2}), "Predicted labels must be 0,1,2"


def test_dataframe_feature_types():
    import pandas as pd
    from src.data_loader import load_iris_as_dataframe

    df = load_iris_as_dataframe()

    numeric_cols = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]

    for col in numeric_cols:
        assert pd.api.types.is_numeric_dtype(df[col]), f"{col} must be numeric"

    assert df["species"].dtype == object, "species column should be text/categorical"
