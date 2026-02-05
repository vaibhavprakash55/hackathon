# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# import pickle

# # 1. Data load karna (Google se sample link)
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# data = pd.read_csv(url, names=names)

# # 2. Features (X) aur Target (y) alag karna
# X = data.drop('class', axis=1)
# y = data['class']

# # 3. Model ko train karna
# model = RandomForestClassifier()
# model.fit(X, y)

# # 4. SABSE IMPORTANT: Model ko 'pickle' file mein save karna
# with open('diabetes_model.pkl', 'wb') as f:
#     pickle.dump(model, f)

# print("Model Trained and Saved as diabetes_model.pkl!")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# 1. Data load karna
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
# Asli dataset ke 8 features + 1 target (class)
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigree', 'Age', 'Outcome']
data = pd.read_csv(url, names=columns)

# 2. Features (X) aur Target (y)
X = data.drop('Outcome', axis=1) # Saare 8 columns
y = data['Outcome']

# 3. Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Model Save karna
with open('diabetes_model_v2.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model with 8 features trained and saved successfully!")

# Always remember we add only those features which is necessary for our prediction , we don't add those features which is don't necessary for prediction. Example: name of patients , not necessary for prediction , if we add this then it will confuse what to do . ML is our brain not our frontend to show all features which is not need
# if we directly run app.py then nothing will run . so first run python train.py then streamlit run app.py