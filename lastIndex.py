# LastLinearSearchIndex.py
#
# Description: Program returns the index of the last occurence of target in a given set of data
#
# Author: Vatsal Parmar
# Date: 18th July, 2019


################# Index Finding function #################

def linearSearchLastIndex(arr, target, length):
	
	for i in reversed(range(0, length)):
		if(arr[i] == target):
			return i;
	return -1;


################# TestCase 1: Repeated Target #################

data1 = [2, 10, 4, 10, 40];
target1 = 10;
length1 = len(data1);

result1 = linearSearchLastIndex(data1, target1, length1)

if result1 == -1:
	print("Element not found !!!")
else:
	print("Element is present at index, ", result1);

################# Test Case 2 : Strings #################

data2 = ["p", "y", "t", "h", "p", "n", "h"]
target2 = "p"
length2 = len(data2)
result2 = linearSearchLastIndex(data2, target2, length2)
if result2 == -1:
	print("Element not found !!!")
else:
	print("Element is present at index, ", result2);

################# Test Case 3 : Empty Data #################

data3 = []
target3 = 10
length3 = len(data3)
result3 = linearSearchLastIndex(data3, target3, length3)
if result3 == -1:
	print("Element not found !!!")
else:
	print("Element is present at index, ", result3);
