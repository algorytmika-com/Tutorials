# running a unittest test
python -m unittest test2

# mock - test calling a method inside another method
## example 1
	def test_add_users_called(self):
		# mock a method to be checked
		# we do not check add_user(...) method here, so the result can be whatever (thus: return_value=True)
		self.user_collection.add_user = Mock(return_value=True)
		# call a level above method - this method calls add_user(...)
		M.load_users(self.FILE_NAME, self.user_collection)

		# assert calling the checked method
		# we check, if load_users(...) calls add_user(...)
		self.user_collection.add_user.assert_called()
## example 2
	import mock_tutorial as MT
	from unittest.mock import Mock
	...	
	def test_get_current_temperature_nice(self):
		# Mock a method inside mock_tutorial module whith a concrete returning value
		# Here MT.get_current_temperature() returns random values, but we mock to return always the same
		MT.temperature_sensor.read_temperature = Mock(return_value=75)
		expected_response = 'Nice temperature, 75F!'
		self.assertEqual(MT.get_current_temperature(), expected_response)
	
# mock - test raising an exception
	## test method - tests raising InsufficientOperands exception
	def test_insufficient_operands(self):
		self.calculator.enter_number(0)
		
		with self.assertRaises(InsufficientOperands):
			self.calculator.add()
	
	## where the Calculator class is:
	from exceptions import InsufficientOperands
	class Calculator(object):
	...
	def __init__(...):
		...
		self.stack = []
	
	def _do_calc(self, operator):
		try:
			result = operator.calc(self.stack[0], self.stack[1])
		except IndexError:
			# in order to test raising an exception it must be raised somewhere
			raise InsufficientOperands
			
# mock - test console input
## if it fails is that sth in the code failed
	import mock_tutorial as MT
	from unittest.mock import Mock
	...
	def test_get_user_info(self):
		# when you see mock_tutorial there is no input function, but it is correct to use MT.input for mocking console input
		MT.input = Mock(return_value = 'Luis')
		self.assertEqual(MT.get_user_info(), 'Luis')

	# where mock_tutorial.py is:
	...
	def get_user_info():
		name = input('What is your name? ')
		return name

# patch - test automaticaly input values with multiple inputs
## example 1 - patch basic
	from unittest import TestCase
	from unittest.mock import patch
	import patch_tutorial as PT

	class TestPatchTutorial(TestCase):

		def test_get_user_input_human(self):
			responses = ('Luis', 'Conejo', '40', 'n')
			expected = "You are Luis Conejo', and you're 40 years old."

			# the side_effect witll be the response tuple
			# here we are overwriting the builtins input function
			with patch('builtins.input', side_effect=responses):
				self.assertEqual(PT.get_user_input(), expected)

## example 2 - patch using queue
	from unittest import TestCase
	from unittest.mock import patch
	import queue
	import patch_tutorial as PT

	class TestPatchTutorial(TestCase):
		def test_get_current_temperature(self):
			responses = (75, 10, -1)
			# When you put things into a queue, you can get them back by doing a get operation.
			exepected_queue = queue.Queue()
			exepected_queue.put("Nice temperature, 75F")
			exepected_queue.put("Tough weather, 10F")

			with patch('patch_tutorial.temperature_sensor.read_temperature', side_effect=responses):
				# The first time I call get temperature, it's going to call the read temperature method within temperature sensor.
				# And we are overwriting it with a 75.	   
				self.assertEqual(PT.get_current_temperature(), exepected_queue.get())
				# For the second one, when I call go get current temperature, it will call read temperature again, 
				# and in this case, you will get a 10.
				self.assertEqual(PT.get_current_temperature(), exepected_queue.get())
				with self.assertRaises(SystemError):
					PT.get_current_temperature()
					
# patch - testing saving into csv file
    @patch('main.csv.DictWriter')
    @patch('main.open', new_callable=mock_open)
    def test_save_users(self, mock_open_csv, mock_dict_writer):
        '''
        Tests the save_users function in the main module.

        This function creates a user, mocks saving it into a file.
        Mock objects are used to replace 'open' and 'csv.DictWriter'
        during the test, and not writing into the actual accounts.csv file.
        '''
        mock_writer = Mock()

        # when the csv.DictWriter class is called, it will
        # return the mock_writer object.
        mock_dict_writer.return_value = mock_writer
        self.user_collection.add_user('1', 'one@email.com', 'User', 'One')
        result = M.save_users(self.FILE_NAME, self.user_collection)
        self.assertTrue(result)
        mock_open_csv.assert_called_once_with(self.FILE_NAME, 'w', newline='')
        mock_dict_writer.assert_called_once_with(mock_open_csv.return_value,
                                                 fieldnames=['USER_ID',
                                                             'EMAIL',
                                                             'NAME',
                                                             'LASTNAME'])
        mock_writer.writerow.assert_called_once_with(
            {'USER_ID': '1',
             'EMAIL': 'one@email.com',
             'NAME': 'User',
             'LASTNAME': 'One'})
			 
# patch - testing reading from a csv file
    @patch('main.csv.DictReader')
    @patch('main.open', new_callable=mock_open)
    def test_load_status_updates(self, mock_open_csv, mock_dict_reader):
        '''
        Tests with mocking the reading from a CSV file and adding the status
        update to the user_status_collection.
        '''
        # Simulate a line from the CSV file
        mock_data = [{'STATUS_ID': 'evmiles97_00001', 'USER_ID': 'evmiles97',
                      'STATUS_TEXT': 'Code is finally compiling'}]

        # mock csv.DictReader object with iterating
        mock_dict_reader.return_value.__iter__.return_value = mock_data

        result = M.load_status_updates(self.FILE_NAME,
                                       self.user_status_collection)

        self.assertTrue(result)
        mock_open_csv.assert_called_once_with(self.FILE_NAME, 'r')
        mock_dict_reader.assert_called_once_with(mock_open_csv.return_value)

				
# integration tests
## just check if all pieces work together
	class ModuleTests(TestCase):
	def test_module(self):
		calculator = Calculator(Adder(), Subtracter(), Multiplier(), Divider())
		
		calculator.enter_number(5)
		calculator.enter_number(2)
		
		calculator.multiply()
		
		calculator.enter_number(46)
		
		calculator.add()
		...
		result = calculator.subtract()
		
		self.assertEqual(6, result)
		
	
		
		