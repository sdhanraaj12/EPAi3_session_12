# ASSIGNMENT SESSION 9

1. Use the Faker (Links to an external site.)library to get 10000 random profiles. Using namedtuple, calculate the largest blood type,
   mean-current_location, oldest_person_age, and average age (add proper doc-strings). - 250 (including 5 test cases)
2. Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250 (including 5 test cases)
3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). 
   Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day,
   and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. - 500  (including 10 test cases)

## Approch:
Using Faker library variable 'fake' is instantiated. Calling fake.profile() generates a fake profile with differnt keys. The keys avaliable can be displayed by printing the result of fake.profile().keys(). A namedtuple called Profile can be created with the necessary fields using
```python
   Profile = namedtuple('Profile', fake.profile().keys())
```

Values can be stored in using the profile created in an object by using

```python
   pr_store = Profile(**fake.profile())
```

For initializing 10000 random profiles :

### init_profiles_using_namedtuple(no_profiles: int)
This function is called with the number of profiles to be created as an input. The function returns a list of profiles where each profile is a namedtuple.

## Decorator Used:
@timed --> to evalaute the time taken in executing the functions for calculating the average age, mean-current location, largest
blood type and oldest persons age for both namedtuple and dictionary. This is in order to determine the time taken for executing each and check which is 
faster. 

## FUNCTIONS USED
### Q1
### 1. oldest_person_nt
This function takes in the list of namedtuples and determines the age of the oldest person. Here we use a lambda function to calculate the age. The min birthdate is determmined and subtracted from todays date and the difference in days is determined. This difference value divided by 365 and converted to an integer gives his current age which is returned.

### 2. average_age_nt
This function takes in the list of namedtuples and finds the age for each person. For this we use a lambda function. The individual's age is taken and subtracted from the current year from today's date. If the month and date from today's date is less than the month and date from the birth year +1 is added to the difference obtained above. Using a map function, we calculate the ages for all the profiles. Sum of all these divided by the number of profiles gives the average age.

### 3. average_coordinates_nt
This function takes in a list of namedtuple profiles and finds the average coordinates. We use a lambda function and a map function. The coordinates are taken and the sum of all the coordinates are found which is divided by the number of profiles to get the average coordinates.

### 4. max_blood_group_nt
This function returns the blood group that is occuring maximum number of times. With the help of map and lambda function, we retrieve the blood groups and find
the mode of all the blood groups. The mode provides us with the blood group that occurs maximum number of times.

### 5. time_nt
This function is used to calculate the amount of average time taken to run N calls to each of the functions using a namedtuple.


## Q2
Here we have to perform the operations done above but with a dictionary. First all the 10000 profiles are converted into a dictionary using the following command:
```python
fk_profile_dict = {'Profile'+str(_):t._asdict() for _, t in enumerate(fk_profile_nt)}
```

In the program, we use 'named_tuple_dict' fuction to convert a namedtuple to dictionary.This is done in order to keep all the profiles same and hence check whether the results are the same. 

### 1. oldest_person_dc
This function takes in a dictionary and determines the age of the oldest person. Here we use a lambda function to calculate the age. The
    min birthdate is determmined and subtracted from todays date and the difference in days is determined. This difference value divided by 365 
    and converted to an integer gives his current age which is returned.

### 2. average_age_dc
This function takes in a dictionary of profiles and finds the age for each person. For this we use a lambda function. The individual's age is taken and 
    subtracted from the current year from today's date. If the month and date from today's date is less than the month and date from the birth year +1 is added 
    to the difference obtained above. Using a map function, we calculate the ages for all the profiles. Sum of all these divided by the number of profiles gives 
the average age.

### 3. average_coordinates_dc
This function takes in a dictionary of profiles and finds the average coordinates. We use a lambda function and a map function. The coordinates are 
taken and the sum of all the coordinates are found which is divided by the number of profiles to get the average coordinates.

### 4. max_blood_group_dc
This function returns the blood group that is occuring maximum number of times. With the help of map and lambda function, we retrieve the blood groups and find
the mode of all the blood groups. The mode provides us with the blood group that occurs maximum number of times.

### 5. time_dc
This function is used to calculate the amount of average time taken to run N calls to each of the functions using dictionary.

## Question 3
### 1. symbol
This function generates the symbol for the fake company. The function takes the company name as its input and generates 2 random integers within the length of the string, capitalizes the character in those positions and returns a string by joining all the capitalizd letters. This is done to keep the company symbol unique.

### 2. stock_market
Initially we create a market capital by creating random N values. Then we create random weights which is normalized so that their sum equals 1. Once that is done,we start creating the stock exchange values. The open values for each Company would be the Market capital multiplied by the weights. The high value is obtained by multiplying the open value with a unform random number between 0.85 and 1.15. Similarly, the close value is obtained by multiplying the open value with a uniform random number between 0.75 and 1.15. Conditions are checked whether the open value > high and if the high < close in which case it is assigned to those values. The calculated values are stored in a named tuple and displayed. The start of the day value is given by multiplying each value in open with the weights and finding the sum. Similar procedure is done for obtaining the values for high and close. The function returns a tuple with all the N profiles, start of the day value, highest of the day value and close.

## Tests Cases

* ### Q1 Namedtuples
1.  test_q1_1_number_of_profiles() : Checks profiles created is equal to the number given input
2.  test_q1_2_average_age() : Checks the average age is properly calculated
3.  test_q1_3_oldest_person() : Checks oldest person is being identified properly
4.  test_q1_4_average_coordinates() : Checks average coordinates is being calculated properly
5.  test_q1_5_max_blood_group() : Checks blood group that occurs maximum times

* ### Q2 Dictionary
2.  test_q2_1_average_age() : Checks the average age is properly calculated
3.  test_q2_2_oldest_person() : Checks oldest person is being identified properly
4.  test_q2_3_average_coordinates() : Checks average coordinates is being calculated properly
5.  test_q2_4_max_blood_group() : Checks blood group that occurs maximum times
5.  test_q2_5_fastest() : Checks the fastest in namedtuple and dictionary by calling both 1000 times and finding average

* ### Q3 Fake Stock Market
1.  test_q3_1_num_profiles_generated()  : Checks n profiles generated
2.  test_q3_2_doc_string() : Checks stock_market contains a doc string
3.  test_q3_3_annotations() : Checks stock_market contains annotations
4.  test_q3_4_unique_symbol() : Checks symbols generated for companies are unique
5.  test_q3_5_return_named() : Checks returned value from stock_market is a tuple
6.  test_q3_6_normalized_weigh() : Checks weights are normalized
7.  test_q3_7_high_low() : Checks Highest value of the day is >= to the close
8.  test_q3_8_all_high_low() : Checks each high value generated is >= close
9.  test_q3_9_docstring_namedtuple() : Checks docstring of named tuple
10. test_q3_10_docstring() : Checks docstring in symbol function

## Screenshot of Test Passed

<image src='assets/pass2.png' height='790'>

