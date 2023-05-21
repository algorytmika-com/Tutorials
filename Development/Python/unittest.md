# running a unittest test
python -m unittest test2

# check calling a method
def test_add_users_called(self):
	# mock a method to be checked
	self.user_collection.add_user = Mock(return_value=True)
	# call a level above method - this method calls add_user(self, user_id, email, user_name, user_last_name)
	M.load_users(self.FILE_NAME, self.user_collection)

	# asser calling the checked method
	self.user_collection.add_user.assert_called()