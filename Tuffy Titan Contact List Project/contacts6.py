import json


class Contacts:
    """ Contacts Class """

    def __init__(self,*,filename):
        """ """
        self.filename = filename
        self.data = {}
        try:
            with open(self.filename,'r') as openfile:
                self.data = json.load(openfile)
                print("File Acquired:", self.filename)
                #print("BREAK------")
                #print(self.data)
        except FileNotFoundError:
            print("Set File:", self.filename)

    def add_contact(self,*,ID, first_name, last_name):
        """ Adds a contact(key-value pair) to a dictionary """
        if ID in self.data :
            return None
        else:
            self.data[ID] = [first_name, last_name]
            #sorts dictionary items by last name, then first name, then by key while being insensitive to cases
            sorted_data = sorted(self.data.items(), key=lambda x:(x[1][1].lower(), x[1][0].lower(), x[0]))
            self.data = {k: v for k, v in sorted_data}
            #print(self.data)
            with open(self.filename, 'w') as outfile:
                json.dump(self.data, outfile)
            return self.data[ID]
        
    
    def modify_contact(self,*, ID, first_name, last_name):
        """ Modifies a contact in a dictionary """
        if ID in self.data:
            self.data[ID] = [first_name, last_name]
            sorted_data = sorted(self.data.items(), key=lambda x:(x[1][1] ,x[1][0], x[0]))
            self.data = {k: v for k, v in sorted_data}
            
            #print(self.data)
            with open(self.filename, 'w') as outfile:
                json.dump(self.data, outfile)
            return self.data[ID]
        else:
            return None

    def delete_contact(self,*, ID):
        """ Deletes a contact in a dictionary """
        if ID in self.data:
            x = self.data.pop(ID)
            #print(self.data)
            with open(self.filename, 'w') as outfile:
                json.dump(self.data, outfile)
            return x 
        else:
            return None




            
