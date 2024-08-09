import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.util.*;
class VaultDoor5 {
    public static void main(String args[]) {
        VaultDoor5 vaultDoor = new VaultDoor5();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
  
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	          if (vaultDoor.checkPassword(input)) {
	              System.out.println("Access granted.");
            } else {
                System.out.println("Access denied!");
        }
    }
    // Minion #7781 used base 8 and base 16, but this is base 64, which is
    // like... eight times stronger, right? Riiigghtt? Well that's what my twin
    // brother Minion #2415 says, anyway.
    //
    // -Minion #2414
    public String base64Encode(byte[] input) {
        return Base64.getEncoder().encodeToString(input);
    }

        public byte[] base64Decode(String input) {
        return Base64.getDecoder().decode(input);
    }

    // URL encoding is meant for web pages, so any double agent spies who steal
    // our source code will think this is a web site or something, defintely not
    // vault door! Oh wait, should I have not said that in a source code
    // comment?
    //
    // -Minion #2415
    public String urlEncode(byte[] input) {
        StringBuffer buf = new StringBuffer();
        for (int i=0; i<input.length; i++) {
            buf.append(String.format("%%%2x", input[i]));
        }
        return buf.toString();
    }

    public String urlDecode(String input) {
        StringBuilder output = new StringBuilder();

        // Process the encoded string
        for (int i = 0; i < input.length(); i += 3) {
            // Extract the two hex digits after the '%'
            String hex = input.substring(i + 1, i + 3);

            // Convert the hex string to a byte
            int byteValue = Integer.parseInt(hex, 16);

            // Append the corresponding character to the output string
            output.append((char) byteValue);
        }

        return output.toString();
    }

    public boolean checkPassword(String password) {
        String urlEncoded = urlEncode(password.getBytes());
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1";
        
        

        byte[] decoded = base64Decode(expected);
        String decodedString = new String(decoded, StandardCharsets.UTF_8);
        
        String expected_reversed = urlDecode(decodedString);

        System.out.println(expected_reversed);
        return base64Encoded.equals(expected);
    }
}
