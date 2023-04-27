import java.io.*;
import java.net.*;

public class udp_palindrome_server {

    public static void main(String[] args) throws IOException {
        int port = 5005;
        DatagramSocket socket = new DatagramSocket(port);

        while (true) {
            byte[] buf = new byte[1024];
            DatagramPacket packet = new DatagramPacket(buf, buf.length);
            socket.receive(packet);

            String received = new String(packet.getData(), 0, packet.getLength());
            System.out.println("Received message: " + received);

            // Check if the received string is a palindrome and send back the result
            String result;
            if (isPalindrome(received)) {
                result = "Palindrome";
            } else {
                result = "Not Palindrome";
            }

            byte[] sendData = result.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, packet.getAddress(), packet.getPort());
            socket.send(sendPacket);
        }
    }

    public static boolean isPalindrome(String str) {
        int i = 0, j = str.length() - 1;
        while (i < j) {
            if (str.charAt(i) != str.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
