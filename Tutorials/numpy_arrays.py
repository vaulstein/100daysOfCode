import numpy as np

# Read from CSV
test_2 = np.genfromtxt('test_2.csv', delimiter=',')

# Array operations

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

test_3_fixed = test_3 + 2


test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2

total_grade = test_1 + test_2 + test_3_fixed

final_grade = total_grade / 3

print(final_grade)

coin_toss = np.array([1, 0, 0, 1, 0])

coin_toss_again = np.array([[1, 0, 0, 1, 0],
                           [0, 0, 1, 1, 1]])
# 1D Array
jeremy_test_2 = test_2[-2]

manual_adwoa_test_1 = np.array([test_1[1], test_1[2]])

# 2D Arrays
student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

tanya_test_3 = student_scores[2, 0]

cody_test_scores = student_scores[:,4]

# Logical Operations

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]

hot = porridge[porridge > 80]

just_right = porridge[(porridge > 60) & (porridge < 80)]

# Review

# Create an array temperatures by importing the data in the CSV temperature_data.csv
temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')

print(temperatures)

# You are working on a team of climate scientists and one of your roles is to take the weekly temperature data and input into NumPy arrays for later analysis. The sensor records the temperature 4 times a day, at 0:00, 6:00, 12:00, and 18:00. You are given last weeks data (Monday through Friday) and asked to create a NumPy array.

# One of the researchers noticed that the sensor had been incorrectly zeroed and all of the recorded temperatures are 3.0 degrees too cold.
# Adjust the array so that the temperature readings are accurate and save them to temperatures_fixed
temperatures_fixed = temperatures + 3.0
print(temperatures_fixed)

#Another researcher asked you for the temperature values from Monday. Save them to a new array, monday_temperatures
monday_temperatures = temperatures_fixed[0]

#"Hmmm, interesting" the researcher mumbles, "can you also give me the 6:00 AM data for Thursday and Friday?"
thursday_friday_morning = temperatures_fixed[3:5, 1]
print(thursday_friday_morning)

# Finally, the persistent researcher now wants all the high and low temperatures over the week.
# Select all temperatures that are under 50 degrees or over 60 degrees and save them to a new array temperature_extremes.
temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]
