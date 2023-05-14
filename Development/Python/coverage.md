
# install coverage
pip install coverage

# run our tests using the coverage module instead of directly using the Python interpreter
python -m coverage run test.py

# generate a code coverage report using the command
python -m coverage report

# run the test_mock.py unittest file under coverage analysis, collecting data only for mock_tutorial.py.
python -m coverage run --include=mock_tutorial.py -m unittest test_mock.py