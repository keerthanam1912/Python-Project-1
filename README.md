# Python-Project-1
Generating required number of passwords

ABSTRACT:

Security is one of the most crucial parts of our lives. The importance of security is increasing day by day as most things are going online. Passwords come into light as we talk about security.
Because we can’t think of different patterns of passwords instantly.But, it is not the same case with computers. Computers can generate random and strong passwords based on our customizations in seconds. There are many password generators available.

INTRODUCTION:

     Here,the password is generated in a specific order of 1 uppercase,1 lowercase,1 symbol and 1 digit must be present.length of the password must be greater than 4 and if not password will not sastisfy above condition .Initially a message will be printed before the code excutes.Mainly string and random modules are used for generating password.

STEPS:

1)importing string and random modules.

   ->string module is imported for ascii values and digits
   
   ->random module is used for choosing a random value from sequence data like list

2)Asking user for number of passwords to be generated

3)Asking user for length of password 

4)Using while for generating number of passwords

5)importing lowercase ascii values from string module and storing in list low

6)simliarly,importing uppercase ascii values and digits from string module and storing them in upp and dig lists

7)In sym list the symbols are stored

8)By using choice from random module choosing random uppercase letter,lowercase letter,digit,symbol

9)using for loop  for generating remaining letters for password by subtracting from length of password

10)Finally,password was generated
