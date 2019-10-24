This demo requires python 3.6+ and a locally installed version of Chrome. Chromedriver is already in the root of the project.

Install:

pip install requirements.txt

Running all the features:

behave

or run individual features

behave features/login.feature
behave features/create_new_account.feature
behave features/find_most_expensive_dress.feature

Please note that the demo site does not seem to persist the shopping cart after logging in and out and so that particular test will fail.
