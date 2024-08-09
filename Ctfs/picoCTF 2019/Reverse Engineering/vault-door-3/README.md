# Writeup for picoCTF 2019: Vault Door 3

## Steps:

Opening the Java file in a text editor, we can observe a slightly more complex structure in the `checkPassword` function. However, without delving too deeply into that complexity, all we need to do is provide the program with the required string `jU5t_a_sna_3lpm12g94c_u_4_m7ra41`, formatted with `picoCTF{}` as indicated in the main function: `String input = userInput.substring("picoCTF{".length(), userInput.length()-1);`.

Before compiling the file, we can print out the `s` string at the very end to see the converted flag using `System.out.println(s);`.

Next, compile the file with `javac VaultDoor3.java` and execute it with `java VaultDoor3`.

After providing the input `picoCTF{jU5t_a_sna_3lpm12g94c_u_4_m7ra41}`:

We get:
```
❯ java VaultDoor3
Enter vault password: picoCTF{jU5t_a_sna_3lpm12g94c_u_4_m7ra41}
jU5t_a_s1mpl3_an4gr4m_4_u_c79a21
Access denied!
```

## Flag:
``` picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21} ```