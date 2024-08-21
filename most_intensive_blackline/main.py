import numpy as np
import cv2


def count(arr, low, high, x):
 
    # If the subarray is invalid or the
    # element is not found
    if ((low > high) or (low == high and arr[low] != x)):
        return 0
 
    # If there's only a single element
    # which is equal to x
    if (low == high and arr[low] == x):
        return 1
 
    # Divide the array into two parts and
    # then find the count of occurrences
    # of x in both the parts
    return count(arr, low, (low + high) // 2, x) + count(arr, 1 + (low + high) // 2, high, x) 

img = cv2.imread(r"example.jpg")
# convert the input image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# apply thresholding to convert grayscale to binary image
ret,thresh = cv2.threshold(gray,70,255,0)
array = np.array(thresh)

lineIndex = 0
indexCount = 0
tempCount = 0
counter = 0
# n^2 for sequantial method T(n) = n * n so it is O(n^2)
for x in array:
  tempCount = 0
  for y in x :
    if (y == 0): # find the black index and store that
      tempCount+=1
  if (tempCount > indexCount):
    indexCount = tempCount
    lineIndex = counter
  counter+=1


#'at the end time complexity is T(n) = nlogn(for sort) + n*logn(for frequency) so it is O(nlogn)'
array.sort() # nlogn for sort
lineDC=0
rowDC=0
counter2 = 0 

for row in array: # n for traverse
  freq = count(row,0,len(row)-1,0)  # logn for find frequency with divide and conquer 
  if (freq > lineDC):
    lineDC=freq
    rowDC = counter2
  counter2+=1

print('line for sequential:',lineIndex)
print('amount for sequential:', indexCount)

print('line for d&c:',rowDC)
print('amount for d&c:',lineDC)

img = cv2.resize(img, (512, 512 ))
cv2.imshow("RGB Image", img)
img = cv2.resize(thresh, (512, 512 ))
cv2.imshow("B&W Image", img)
img = cv2.resize(array, (512, 512 ))
cv2.imshow("Sorted B&W Image Array", img)
cv2.waitKey(0)
cv2.destroyAllWindows()