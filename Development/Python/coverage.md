# install coverage
pip install coverage

# run our tests using the coverage module instead of directly using the Python interpreter
python -m coverage run test.py

# generate a code coverage report
python -m coverage report

# generate a code coverage report, showing lines not covered
coverage report -m

# run the test_mock.py unittest file under coverage analysis, collecting data only for mock_tutorial.py.
python -m coverage run --include=mock_tutorial.py -m unittest test_mock.py

# run the unit tests in the test module and collects code coverage
coverage run -m unittest test

# run only on some unittest
coverage run -m unittest test.AdderTests testSubstractTests test.CalculatorTests

# run only on some unittest, collecting code coverage data specifically for the calculator module
coverage run --source=calculator -m unittest test.AdderTests testSubstractTests test.CalculatorTests

# generate html report
coverage html