c=0
with open("sub_postandcomment_data.json") as data:
    for line in data:
        c+=1
print "Comment Trees Collected", c
print "Percentage out of total posts", float(c)/150000
