# #We need to distribute math and history textbooks to students.
# There are 2 class sections: the first section has 18 pupils, and the second one has 19. 
# The total number of books available for distribution is 76.
# Write a program to calculate and output how many books will be left after each student receives both books.

classOne = 18
classTwo = 19


result = (classOne + classTwo)*2

nextResult = 76 - result

print(nextResult)