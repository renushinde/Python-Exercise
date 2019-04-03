# For loops are finite loops, while loops are indefinite loops. 

for i in [5, 4, 3, 2, 1]:
    print(i)
print ("Blastoff")

# Another example
friends = ['Thomas', 'Percy', 'Henry']

for friend in friends:
	print ("Hello", friend)

# find the largest number

largest_so_far = -1
print("before", largest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
	if num > largest_so_far:
		largest_so_far = num
	print(largest_so_far, num)

print ("After", largest_so_far)

# Counting in a loop
count = 0
print ("Before", count)
for thing in [9, 41, 12, 3, 74, 15]:
  	count += 1
  	print (count, thing)
print ("After", count)


# Summing in a loop
total =0
print("Before", total)
for thing in [9, 41, 12, 3, 74,15]:
	total += thing
	print (total, thing)
print ("After", total)

# Finding the average in a loop- average is sum of numbers divided by total numbers
sum = 0
count = 0
print("Before", count, sum)
for thing in [9,41,12,3, 74, 15]:
	count +=1
	sum += thing
	print( count, sum)
print("After", count, sum, sum/count)

# Filtering in a loop