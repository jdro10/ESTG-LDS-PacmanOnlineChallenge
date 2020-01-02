using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace GameServer
{
    public class NewGameServer
    {
        static string coordenadasJog1 = "255/255/1";
        static string coordenadasJog2 = "355/295";

        static void Main(string[] args)
        {
            Socket socket = null;
            TcpListener myList = null;
            IPAddress ipAd = IPAddress.Parse("127.0.0.1");

            myList = new TcpListener(ipAd, 9000);
            myList.Start();

            int playerNumber = 0;

            while (true)
            {
                Console.WriteLine("Waiting for a connection...");
                socket = myList.AcceptSocket();
                Console.WriteLine("Connection accepted from " + socket.RemoteEndPoint);
                playerNumber++;
                Thread t = new Thread(() => NewPlayer(socket, playerNumber));
                t.Start();
                
                if (playerNumber == 2)
                {
                    playerNumber = 0;
                }
            }
        }

        public static void NewPlayer(Socket socket, int playerIdentifier)
        {
            string data = null;
            byte[] b = new byte[100];

            try
            {
                while (true)
                {
                    if (DetectCollision())
                    {
                        socket.Close();
                        break;
                    }

                    if (playerIdentifier == 1)
                    {
                        int bytesRec = socket.Receive(b);
                        data = Encoding.ASCII.GetString(b, 0, bytesRec);
                        Console.WriteLine("Jogador1: " + data);
                        coordenadasJog1 = data;

                        ASCIIEncoding asen = new ASCIIEncoding();
                        socket.Send(asen.GetBytes(coordenadasJog2));
                    }
                    else
                    {
                        int bytesRec = socket.Receive(b);
                        data = Encoding.ASCII.GetString(b, 0, bytesRec);
                        Console.WriteLine("Jogador2: " + data);
                        coordenadasJog2 = data;

                        ASCIIEncoding asen = new ASCIIEncoding();
                        socket.Send(asen.GetBytes(coordenadasJog1));
                    }
                }
            }
            catch (Exception)
            {
                coordenadasJog1 = "255/255";
                coordenadasJog2 = "355/355";
            }
        }

        public static bool DetectCollision()
        {
            string[] split = coordenadasJog1.Split("/");
            string coords1 = split[0] + "/" + split[1];

            if (coords1.Equals(coordenadasJog2))
            {
                return true;
            }
            return false;
        }
    }
}
