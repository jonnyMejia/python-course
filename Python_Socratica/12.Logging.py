import logging

# DEBUG: Detalled information. typically of interest only when diagnosting problems.
# Info: Confirmation that things are working as excpected
# Warning: An indication that something unexpected hapenned, or indicative of some problem in the near future. The software is still working as expected
# Error: Due to a more serious problem, the software has not been able to perfore some function
# Critical: A serious error, indicating that program itself may be unable to continue running

# Create and configure logger
logging.basicConfig(filename="test.log",
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger()

# test messages
logger.debug("This is a harmiess debug message.")
logger.info("Just some useful info")
logger.warning("I'm sorry, but I can't do that, Dave")
logger.error("Did you try divide by zero")
logger.critical("The entire internet is down.")