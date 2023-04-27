import java.io.*;
import java.net.*;

public class udp_factorial_client {

    public static void main(String[] args) throws IOException {

        String serverHostname = "localhost";
        int serverPort = 5005;

        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
        DatagramSocket clientSocket = new DatagramSocket();

        InetAddress IPAddress = InetAddress.getByName(serverHostname);

        while (true) {

            System.out.print("Enter a number to find factorial: ");
            String input = inFromUser.readLine();

            byte[] sendData = input.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, serverPort);
            clientSocket.send(sendPacket);

            byte[] receiveData = new byte[1024];
            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
            clientSocket.receive(receivePacket);

            String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("Factorial of " + input + " is " + response);
        }
    }

}
