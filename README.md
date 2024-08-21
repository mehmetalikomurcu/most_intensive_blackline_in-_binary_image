Project Overview

This project aims to find the row with the most intensive black color in a binary image. Two algorithms have been implemented to achieve this:

    Sequential Method: This method iteratively scans through each row of the binary image and counts the number of black pixels (represented as 0). The row with the maximum count of black pixels is identified.

    Divide and Conquer Method: This method recursively divides the rows of the binary image to find the row with the maximum count of black pixels. This approach uses a divide-and-conquer strategy to optimize the counting process.

Project Files

    main.py: This file contains the implementation of the two algorithms along with image processing and comparison logic.
    example.jpg: An example RGB image that will be processed by the code.

Dependencies

    Python 3.x
    OpenCV (cv2): For image processing tasks such as reading images, converting them to grayscale, and applying thresholding.
    NumPy: For array manipulations and numerical operations.

How It Works

    Image Preprocessing:
        The input RGB image is read and converted to a grayscale image.
        The grayscale image is then thresholded to produce a binary image, where pixels are either black (0) or white (255).

    Sequential Method:
        The binary image is traversed row by row.
        The count of black pixels in each row is calculated.
        The row with the highest count is identified and stored.

    Divide and Conquer Method:
        The binary image is sorted row-wise.
        A recursive function is used to divide the array and count the frequency of black pixels in each part.
        The row with the highest frequency is identified.

    Results:
        The program prints the line index and the amount of black pixels for both the sequential method and the divide-and-conquer method.
        It also displays three images for visual verification.

Time Complexity Analysis

    Sequential Method: The time complexity is O(n^2) since each pixel in the binary image (of size n x n) is scanned.
    Divide and Conquer Method: The time complexity is O(n log n). This includes sorting the rows (O(n log n)) and finding the frequency of black pixels using a divide-and-conquer strategy (O(log n)).

Notes

    Ensure that the example.jpg image used is suitable for binary conversion and has distinguishable black and white areas.
    The code has been tested with an example image, but performance may vary based on the image resolution and content.
