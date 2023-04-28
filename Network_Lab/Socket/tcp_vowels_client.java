import java.net.*;
import java.io.*;

public class tcp_vowels_client {
    public static void main(String[] args) throws IOException {
        if (args.length != 1) {
            System.err.println("Usage: java VowelClient <string>");
            System.exit(1);
        }

        String hostName = "localhost"; // the hostname of the server
        int portNumber = 12345; // the port number of the server

        try (
            Socket socket = new Socket(hostName, portNumber);
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in))
        ) {
            String userInput = args[0];
            out.println(userInput); // send the string to the server
            String response = in.readLine();
            System.out.println("Server: " + response); // print the response from the server
        } catch (UnknownHostException e) {
            System.err.println("Don't know about host " + hostName);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to " + hostName);
            System.exit(1);
        }
    }
}
