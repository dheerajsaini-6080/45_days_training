# This program prints a student introduction using variables and a dictionary.

student={
    'city':'Shrimadhopur','favorite_subject':'machine learning','target_role_varible':'projet manager & python developer'

}
Intro=f'''Hlo , I am Dheeraj Saini currently purshing B.tech Degree From Arya College of Ingennerinf and IT Jaipur.
My home town is {student['city'].upper()}, But currently I stay in Jaipur near my college.
I am intrested in real word AI project so I choose {student['favorite_subject'].title()},as a favorite subject.
I choose target role according to my intrest  so the target role is {student['target_role_varible'].title()}
'''
print(Intro)