# def calculate_rectangle_area(length, width):
#     """
#     This function takes in the length and width of a rectangle and calculates its area.

#     Parameters:
#     length (float): The length of the rectangle.
#     width (float): The width of the rectangle.

#     Returns:
#     float: The area of the rectangle.
#     """
#     area = length * width
#     return area


# length = 5
# width = 10
# area = calculate_rectangle_area(length, width)
# print("The area of the rectangle is:", area.__doc__)

def calculate_rectangle_area(length, width):
    """
    This function takes in the length and width of a rectangle and calculates its area.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    area = length * width
    return area


length = 5
width = 10
area = calculate_rectangle_area(length, width)
print("The area of the rectangle is:", area)
print("Function docstring:", calculate_rectangle_area.__doc__)

