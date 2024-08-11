# Writeup for picoCTF 2019 : vault-door-6
## Steps:
The given code performs a check on a password by XORing each byte of the password (passBytes[i]) with 0x55 and then subtracting a corresponding byte from myBytes[i].
If the result of this operation is non-zero for any byte, the password check fails.

Our goal is to reverse the operation in order to print the ASCII representation of myBytes, effectively reconstructing the original password.

Since the XOR operation is reversible (i.e., A ^ B ^ B = A), we can retrieve the original characters of the password by XORing each byte in myBytes with 0x55.
The operation to reverse is: passBytes[i] = myBytes[i] ^ 0x55.

Write a Java program that loops through each byte in myBytes.
XOR each byte with 0x55 to retrieve the original character.
Convert the result to a character and collect it to form the original password string.

```java
        char[] passChars = new char[myBytes.length];
        
        for (int i = 0; i < myBytes.length; i++) {
            passChars[i] = (char) (myBytes[i] ^ 0x55);
        }
        
        String flag = new String(passChars);
        System.out.println("The password is: " + flag);

Remember to still pass 32 characters as required in the main function, however, this could also be altered.

```
java VaultDoor6
Enter vault password: 12341234123412341234123412341234
The password is: n0t_mUcH_h4rD3r_tH4n_x0r_3ce2919
Access granted.
```

## Flag:
```picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_3ce2919}```
