# setting logging level - tells the logger to only display log messages with level WARNING and above
logging.basicConfig(level=logging.WARNING)

# The formatting characters to the left and right of the parentheses are borrowed from printf formatting
# For example, %(asctime)s means to include the time string in the log message as a string.
# The -4d in %(lineno)-4d means to include the line number of the log statement as a 4 character integer,
# padding the output on the right with spaces.
log_format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
logging.basicConfig(level=logging.WARNING, format=log_format)

# sending log to a file
logging.basicConfig(level=logging.WARNING, format=log_format, filename='mylog.log')

# sending logging messages to multiple places
## 1. Create a "formatter" using our format string
formatter = logging.Formatter(log_format)

## 2. Create a log message handler that sends output to the file 'mylog.log'
file_handler = logging.FileHandler('mylog.log')

## 3. Set the formatter for this log message handler to the formatter we created above.
file_handler.setFormatter(formatter)

## 4. Get the "root" logger. More on that below.
logger = logging.getLogger()

## 5. Add our file_handler to the "root" logger's handlers.
logger.addHandler(file_handler)

