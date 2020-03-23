import os, sys

# Open a file
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
os.dup2(1, fd)
# Write one string
os.write(fd, "This is test")
print "writing is done..."

# Now duplicate this file descriptor as 1000
# fd2 = 1000

execfile("odd.py")

print "exec is done..."

# Now read this file from the beginning using fd2.

os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print "Read String is : ", str

# Close opened file
os.close( fd )

print "Closed the file successfully!!"