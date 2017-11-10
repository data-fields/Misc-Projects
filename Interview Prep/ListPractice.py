#Create a list
elements = [" "]

#Finds if list is empty using idiom
if not elements:
    print "List is Empty"

#Finds size of list
print len(elements)

#Add to the list
elements.append(obj)

#Removes object from list
elements.remove(obj)

#finds if object is in list
if raw_input()in elements:
    print "Object is in list"
else:
    print "Object is not in list"