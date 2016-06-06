
def names1(dict2):
    for key, value in dict2.iteritems():
        print key
        for  key2, info in enumerate(value):
            print str(key2 + 1) + " - " + info['first_name'] + " " + info['last_name'] + " - " + str(len(info['first_name'] + info['last_name']))
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
names1(users)
