# Writeup for picoCTF 2019 : vault-door-4
## Steps:
In the java code we can simply replace the check in the `checkPassword` function with a loop that appends the converted character of every byte in `myBytes` to a string and then print that out.

```java
39         StringBuilder result = new StringBuilder();
40         for (byte b : myBytes) {
41             result.append((char) b);
42         }
43 
44         String myString = result.toString();
45         System.out.println(myString);
```
## Flag:
``` picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e} ```
