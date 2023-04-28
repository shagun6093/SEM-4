import java.net.*;
import java.io.*;

public class tcp_vowels_server {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = null;

        try {
            serverSocket = new ServerSocket(12345); // create a server socket on port 12345
        } catch (IOException e) {
            System.err.println("Could not listen on port: 12345.");
            System.exit(1);
        }

        Socket clientSocket = null;

        try {
            clientSocket = serverSocket.accept(); // wait for a client to connect
        } catch (IOException e) {
            System.err.println("Accept failed.");
            System.exit(1);
        }

        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

        String inputLine;

        while ((inputLine = in.readLine()) != null) {
            int count = 0;
            for (int i = 0; i < inputLine.length(); i++) {
                char c = inputLine.charAt(i);
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                    c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                    count++; // count the number of vowels in the input string
                }
            }
            out.println("Number of vowels: " + count);
        }

        out.close();
        in.close();
        clientSocket.close();
        serverSocket.close();
    }
}
