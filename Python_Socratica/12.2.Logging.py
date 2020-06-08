import logging 
import math

# Configure logging 
logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)
logger = logging.getLogger()

def quadratic_formula(a, b, c):
    
    """Return the solutions to the equation ax² + bx + c = 0."""
    logger.info("quadratic_formula({}, {},{})".format(a, b, c))
    
    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c
    
    # Compute the two roots
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger.debug("# Return the roots")
    return (root1,root2)

# Execute
roots = quadratic_formula(1, 0, -4)
