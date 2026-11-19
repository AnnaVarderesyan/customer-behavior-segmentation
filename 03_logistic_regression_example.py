"""Ուսուցողական օրինակ. X_train/y_train/X_valid պետք է ստացվեն իրական ժամանակային բաժանումից։"""
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score

def fit_and_evaluate(X_train, y_train, X_valid, y_valid):
    model = make_pipeline(StandardScaler(), LogisticRegression(class_weight="balanced", max_iter=1000))
    model.fit(X_train, y_train)
    scores = model.predict_proba(X_valid)[:, 1]
    return model, average_precision_score(y_valid, scores)
