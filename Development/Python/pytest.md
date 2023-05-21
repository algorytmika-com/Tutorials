# when proble running pytest
py -m pip install pytest-cov

#pytest - set enviroment ot recogniize modules, put inside test file
# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
# add to contest.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '\\..\\src\\assignment06')

# run pytest at level above scr and tests
python -m pytest

# run pytest without warning concerning the report
python -m pytest --cov

# mocking using decorator
	@mock.patch('patch_tutorial.temperature_sensor.read_temperature', mock.Mock(side_effect=(75, 10, -1)))
	def test_get_current_temperature():
		expected_queue = queue.Queue()
		expected_queue.put("Nice temperature, 75F")
		expected_queue.put("Tough weather, 10F")

		assert PT.get_current_temperature() == expected_queue.get()
		assert PT.get_current_temperature() == expected_queue.get()

		with pytest.raises(SystemError):
			PT.get_current_temperature()

# mock using decorator, checking if method is called inside another method
## check that not only the results are the correct ones, 
## but also the way external functions are being called is also correct.
	@mock.patch('patch_tutorial.temperature_sensor.convert_to')
	def test_perform_conversion_C_to_F(mocked_function):
		# patch_tutorial.temperature_sensor.convert_to is mocked to return allways 32
		mocked_function.return_value = 32
		result = PT.perform_conversion(0, 'Fahrenheit')
		# checks if the return is correct, but not checks if the mocked function has changed and is not correct
		assert result == 'A reading of 0 degrees Celsius is equivalent '\
			'to 32 degrees Fahrenheit'
		# checks the correctness of called, mocked function
		mocked_function.assert_called_with(0, 'Fahrenheit')