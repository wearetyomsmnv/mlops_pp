from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Загрузка датасета
iris = load_iris()
X, y = iris.data, iris.target

# Разбиение на обучающую и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# Обучение модели
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
# Оценка модели
print(f"Accuracy: {clf.score(X_test, y_test)}")
