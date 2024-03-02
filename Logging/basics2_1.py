import logging  # Importing logging module for logging functionality

# Creating a logger object specific to the current module.
# getLogger(__name__) retrieves or creates a logger object with the name of the current module.
# This ensures that logs generated by this module are associated with its name.
# If running the current file, the __name__ will change to __main__ in log file, else if 
# importing this file in another file, then __name__ will change to the module name
logger = logging.getLogger(__name__) 

# Setting the logging level to DEBUG for the logger
logger.setLevel(logging.DEBUG)

# Creating a formatter object to define the log message format
formatting = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s",
                               datefmt="%Y-%m-%d %H:%M:%S")

# Creating a file handler to log messages to a file named "student.log"
filehander = logging.FileHandler("student.log")
filehander.setFormatter(formatting)  # Setting the formatter for the file handler

# Adding the file handler to the logger to capture log messages to the file
logger.addHandler(filehander)

class Student:
    def __init__(self, name, branch) -> None:
        """
        Initialize a Student object with name and branch.
        
        Args:
            name (str): The name of the student.
            branch (str): The branch of study of the student.
        """
        self.name = name
        self.branch = branch

        # Logging an informational message when a student is added
        logger.info("Added Student: {} from {}".format(self.name, self.branch))

# Creating instances of the Student class
student_1 = Student("Lucifer", "Computer Science")
student_2 = Student("John", "Electronics")
