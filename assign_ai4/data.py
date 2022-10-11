"""
Transforming the categorical data columns with Python script
so that the data can be processed by a deep neural network
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf


class Categorical_Preprocessing:
    def __init__(self):
        self.df = None

    def __getitem__(self, item):
        item = self.df
        return item

    def read_data(self, file_name: str):
        read = pd.read_csv(file_name)
        self.df = pd.DataFrame(read)
        return self.df

    def find_missing(self):
        missing = self.df.isnull().sum()
        return missing

    def missing_mean(self, col_name):
        self.df[col_name] = self.df[col_name].fillna(self.df[col_name].mean())
        return self.df

    def unique_values(self):
        unique_vals = {column: len(self.df[column].unique())
                       for column in self.df.columns if self.df.dtypes[column] == 'object'}
        return unique_vals

    def unique_col_vals(self, col_name):
        return self.df[col_name].unique()

    def replace_mapping(self, col_name, mapping):
        self.df[col_name] = self.df[col_name].replace(mapping)
        return self.df[col_name]

    def boolean_values(self):
        for column in self.df.columns:
            if self.df.dtypes[column] == 'bool':
                self.df[column] = self.df[column].astype(int)
        return self.df

    def onehot_encode(self, columns, prefixes):
        df = self.df.copy()
        for column, prefix in zip(columns, prefixes):
            dummies = pd.get_dummies(df[column], prefix=prefix)
            df = pd.concat([df, dummies], axis=1)
            df = df.drop(column, axis=1)
        return df

    def drop_columns(self, col_name):
        self.df = self.df.drop(col_name, axis=1)
        return self.df

    def remaining_non_numeric(self):
        return print("Remaining non-numeric columns:", (self.df.dtypes == 'object').sum())


car_data = Categorical_Preprocessing()
car_data.read_data("cars.csv")
print(car_data.find_missing())
car_data.missing_mean(["engine_capacity"])
print(car_data.unique_values())
car_data.boolean_values()
car_data.drop_columns(["model_name"])
tran_map = {'automatic': 0, 'mechanical': 1}
car_data.replace_mapping(['transmission'], tran_map)
col_map = {'silver': 3, 'blue': 3, 'red': 3, 'black': 0, 'grey': 3, 'other': 3,
           'brown': 3, 'white': 1, 'green': 3, 'violet': 3, 'orange': 3, 'yellow': 3}
car_data.replace_mapping(['color'], col_map)

onehot_columns = ['manufacturer_name', 'engine_fuel', 'body_type', 'state', 'drivetrain',
                  'location_region', 'engine_type']

onehot_prefixes = ['m', 'e', 'b', 's', 'd', 'l', 'n']
car_data.onehot_encode(onehot_columns, onehot_prefixes)

y = car_data['color'].copy()
X = car_data.drop_columns(['color']).copy()

scaler = StandardScaler()

X = scaler.fit_transform(X)
print(X.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=100)

"""
inputs = tf.keras.Input(shape=(109,))
x = tf.keras.layers.Dense(64, activation='relu')(inputs)
x = tf.keras.layers.Dense(64, activation='relu')(x)
outputs = tf.keras.layers.Dense(3, activation='softmax')(x)

model = tf.keras.Model(inputs, outputs)

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    batch_size=32,
    epochs=100,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=3,
            restore_best_weights=True
        )
    ]
)

final_eval = model.evaluate(X_test, y_test)

print(final_eval)

Processing Categorical Data
Transforming Nominal Data
1. manufacturer_name
2. model_name
3. transmission
4. color
7. engine_fuel
8. engine_has_gas
9. engine_type
11. body_type
12. has_warranty
13. state
14. drivetrain
16. is_exchangeable
17. location_region

Processing Categorical Data
Transforming Ordinal Data
5. odometer_value
6. year_produced
10. engine_capacity
15. price_usd
18. number_of_photos
19.up_counter
20. duration_listed


"""
