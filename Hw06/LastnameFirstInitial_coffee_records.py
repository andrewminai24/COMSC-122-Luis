#This program adds coffee inventory records to
#the coffee.txt file.


def add_coffee():
    #create a variable to control the loop.
    addUser='y'
  
    #Open the coffee.txt file in append mode
    coffee_file=open('coffee.txt','a')

    #Add records to the file.

    while (addUser =='y' or addUser =='Y'):
        #Get the coffee record data.
  
        print('Enter the following coffee data')
        descr=input('Descriptions: ')
        qty=float(input('Quantity (in pounds): '))

        #Append the data to the file.
        coffee_file.write(descr+ '\n')
        coffee_file.write(str(qty)+ '\n')

        #Determine whether the user wants to add
        #another record to the file.
        print('Do you want to enter another record \n Y=yes, anything else= no: ')
        addUser=input("")

    #close the file
    coffee_file.close()
    print('Data appended to coffee.txt.')

def show_coffee():
    #This function display the records in the
    #coffee.txt file.

    #Open the coffee.txt file in append mode
    coffee_file=open('coffee.txt','r')

    #Read the first record's description field.
    descr=coffee_file.readline()

    #Read the rest of the file.

    while descr !='':
        #Read the quantity field.
        qty=float(coffee_file.readline())

        #Strip the \n from the description.
        descr=descr.rstrip('\n')

        #Display the record.
        print('Descriptions:',descr)
        print('Quantity:',qty)

        #Read the next description
        descr=coffee_file.readline()
    #close the file.
    coffee_file.close()
  

def search_coffee():
    #This function allows the user to search the
    #coffee.txt file for records matching a
    #description.

     #Create a bool variable to use as a flag.
    found=False
  
    search=input('Enter a description to search for:')
  

    #Open the original coffee.txt file.
    coffee_file=open('coffee.txt','r')


    #Read the first record's description field.
    descr=coffee_file.readline()

    #Read the rest of the file.

    while descr !='':
        #Read the quantity field.
        qty=float(coffee_file.readline())

        #Strip the \n from the description.
        descr=descr.rstrip('\n')
      
        #Determine whether this record matches
        #the search value.
      
        if descr==search:
            #Display the record.
            print('Description:',descr)
            print('Quantity:',qty)
          
            #Set the found flag to True.
            found=True

        descr=coffee_file.readline()

    #close the file.
    coffee_file.close()

    #If the search value was not found in the file.
    #display a message.

    if not found:
        print('That item was not found in the file.')
      
  

def modify_coffee():
    import os;
    #Create a bool variable to use as a flag.
    found=False
  
    search=input('Enter a description to search for:')
    new_qty=float(input('Enter the new quantity:'))

    #Open the original coffee.txt file.
    coffee_file=open('coffee.txt','r')

    #Open the temporary file.
    temp_file=open('temp.txt','w')

    #Read the first record's description field.
    descr=coffee_file.readline()

    #Read the rest of the file.

    while descr !='':
        #Read the quantity field.
        qty=float(coffee_file.readline())

        #Strip the \n from the description.
        descr=descr.rstrip('\n')
      
        #Write either this record to the temporary file
        #or the new record if this is the one that is
        #to be modified.
        if descr==search:
            #write the modified record to the temp file
            temp_file.write(descr +'\n')
            temp_file.write(str(new_qty)+'\n')

            #Set the found flag to True.
            found=True

        else:
            #write the original record to the temp file.
            temp_file.write(descr+'\n')
            temp_file.write(str(qty)+'\n')

         #Read the next description.
        descr=coffee_file.readline()

    #close the coffee file and the temporary file.
    coffee_file.close()
    temp_file.close()

    #Delete the original coffee.txt file.
    os.remove('coffee.txt')

    #Rename the temporary file.
    os.rename('temp.txt','coffee.txt')

    #If the search value was not found in the file
    #display a message.

    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')
      
          
def delete_coffee():
    import os;
    #This function allows the user to delete
    #a record in the coffee.txt file

    #Create a bool variable to use as a flag.
    found=False

    #Get the coffee to delete
    search=input('Which coffee do you want to delete:')

    #Open the original coffee.txt file.
    coffee_file=open('coffee.txt','r')

    #Open the temporary file.
    temp_file=open('temp.txt','w')

    #Read the first record's description field.
    descr=coffee_file.readline()

    #Read the rest of the file.

    while descr !='':
        #Read the quantity field.
        qty=float(coffee_file.readline())

        #Strip the \n from the description.
        descr=descr.rstrip('\n')

        #If this is not the record to delete,then
        #Write it to the temporary file
      
        if descr!=search:
            #write the modified record to the temp file
            temp_file.write(descr +'\n')
            temp_file.write(str(qty)+'\n')

        else:
            #Set the found flag to True.
            found=True


        #Read the next description.
        descr=coffee_file.readline()

    #close the coffee file and the temporary file.
    coffee_file.close()
    temp_file.close()

    #Delete the original coffee.txt file.
    os.remove('coffee.txt')

    #Rename the temporary file.
    os.rename('temp.txt','coffee.txt')

    #If the search value was not found in the file
    #display a message.

    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')
