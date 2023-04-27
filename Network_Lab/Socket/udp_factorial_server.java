import java.io.*;
import java.net.*;

public class udp_factorial_server {

    public static void main(String[] args) throws IOException {

        int port = 5005;
        DatagramSocket socket = new DatagramSocket(port);

        while (true) {

            byte[] buf = new byte[1024];
            DatagramPacket packet = new DatagramPacket(buf, buf.length);
            socket.receive(packet);

            int num = Integer.parseInt(new String(packet.getData(), 0, packet.getLength()));

            int result = factorial(num);

            String response = String.valueOf(result);

            byte[] sendData = response.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, packet.getAddress(), packet.getPort());
            socket.send(sendPacket);

        }
    }

    public static int factorial(int n) {
        if (n == 0)
            return 1;
        else
            return (n * factorial(n-1));
    }

}
