import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Загружаем датасет
iris = load_iris()
X, y = iris.data, iris.target

# Разбиваем на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2022)

# Начинаем MLflow эксперимент
with mlflow.start_run():

    # Создаем и тренируем модель
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Записываем параметры, метрики и модель
    mlflow.log_param("test_size", 0.3)
    mlflow.log_metric("accuracy", model.score(X_test, y_test))
    mlflow.sklearn.log_model(model, "model")
