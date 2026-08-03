name = "Indra"
age = 16
school = "information technology vocational high school denpasar"
school = school.title()
money = 1500.789

print (f"My name is {name}, I am {age} years old, and i am a student at {school}, and I have ${money:,} dollars. ")
print ("My name is {}, I am {} years old, and i am a student at {}, and I have ${:.2f} dollars.".format(name,age,school,money))
print ("My name is %s, I am %s years old, and i am a student at %s, and I have $.%1f dollars." % (name, age, school, money))