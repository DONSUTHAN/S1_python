text = input("enter a string:")
occurrence = {}
for char in text:
    if char in occurrence:
        occurrence[char] += 1
    else:
        occurrence[char] = 1
        print ("occurrence ",occurrence)