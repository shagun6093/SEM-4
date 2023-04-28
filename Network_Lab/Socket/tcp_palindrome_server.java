import java.net.*;
import java.io.*;

public class tcp_palindrome_server{
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
            String reverseString = new StringBuilder(inputLine).reverse().toString(); // reverse the input string
            if (inputLine.equals(reverseString)) {
                out.println("String is a palindrome");
            } else {
                out.println("String is not a palindrome");
            }
        }

        out.close();
        in.close();
        clientSocket.close();
        serverSocket.close();
    }
}
