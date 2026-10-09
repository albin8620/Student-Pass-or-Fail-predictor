
from sklearn.linear_model import LogisticRegression

# 1. Historical data
# Each row contains: [study_hours, attendance_percentage]

X = [
    [1, 46],
    [2, 50],
    [3, 60],
    [4, 70],
    [5, 80],
    [6, 90],
    [1, 45],
    [2, 55],
    [3, 65],
    [5, 95]
]

# 0 means Fail, 1 means Pass
y = [0, 0, 0, 1, 1, 1, 0, 0, 1, 1]

# 2. Create the model
model = LogisticRegression()

# 3. Train the model
model.fit(X, y)

print("\nStudent Pass/Fail Prediction System")
print("-----------------------------------")
print("Training completed successfully!")

# 4. Get details of a new student
while True:
    try:
        hours = float(input("\nEnter study hours per day (0-24): "))
        attendance = float(input("Enter attendance percentage (0-100): "))

        if not 0 <= hours <= 24 or not 0 <= attendance <= 100:
            print("Enter valid values within the given ranges.")
            continue

        break
    except ValueError:
        print("Please enter numbers only.")

# 5. Predict the result
student = [[hours, attendance]]

prediction = model.predict(student)[0]
probability = model.predict_proba(student)[0][1]

# 6. Display the result
print("\n--- Prediction ---")
print(f"Study hours: {hours}")
print(f"Attendance: {attendance}%")
print(f"Estimated probability of passing: {probability * 100:.2f}%")

if prediction == 1:
    print("Predicted result: PASS")
else:
    print("Predicted result: FAIL")