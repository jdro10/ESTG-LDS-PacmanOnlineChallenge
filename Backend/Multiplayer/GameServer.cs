using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace GameServer
{
    public class GameServer
    {
        public static void Main()
        {
            Thread t = new Thread(Teste);
            t.Start();
            try
            {
                IPAddress ipAd = IPAddress.Parse("192.168.1.65");
                // use local m/c IP address, and 
                // use the same in the client

                /* Initializes the Listener */
                TcpListener myList = new TcpListener(ipAd, 8001);

                /* Start Listeneting at the specified port */
                myList.Start();

                Console.WriteLine("The server is running at port 8001...");
                Console.WriteLine("The local End point is  :" +
                                  myList.LocalEndpoint);
                Console.WriteLine("Waiting for a connection.....");

                Socket so = myList.AcceptSocket();
                Console.WriteLine("Connection accepted from " + so.RemoteEndPoint);

                while (true)
                {
                    byte[] b = new byte[100];
                    int k = so.Receive(b);

                    for (int i = 0; i < k; i++)
                        Console.Write(Convert.ToChar(b[i]));
                    Console.Write("Jogador1: ");

                    ASCIIEncoding asen = new ASCIIEncoding();
                    so.Send(asen.GetBytes("The string was recieved by the server."));
                    //Console.WriteLine("\nSent Acknowledgement");

                    
                }
                /* clean up */
                so.Close();
                myList.Stop();

            }
            catch (Exception e)
            {
                Console.WriteLine("Error..... " + e.StackTrace);
            }
        }

        public static void Teste()
        {
            try
            {
                IPAddress ipAd = IPAddress.Parse("192.168.1.65");
                // use local m/c IP address, and 
                // use the same in the client

                /* Initializes the Listener */
                TcpListener myList = new TcpListener(ipAd, 8002);

                /* Start Listeneting at the specified port */
                myList.Start();

                Console.WriteLine("The server is running at port 8002...");
                Console.WriteLine("The local End point is  :" +
                                  myList.LocalEndpoint);
                Console.WriteLine("Waiting for a connection.....");

                Socket s = myList.AcceptSocket();
                Console.WriteLine("Connection accepted from " + s.RemoteEndPoint);

                while (true)
                {
                    byte[] b = new byte[100];
                    int k = s.Receive(b);

                    for (int i = 0; i < k; i++)
                        Console.Write(Convert.ToChar(b[i]));
                    Console.Write("Jogador2: ");


                    ASCIIEncoding asen = new ASCIIEncoding();
                    s.Send(asen.GetBytes("Enviado do jogador 1 para o 2"));
                    //Console.WriteLine("\nSent Acknowledgement");
                }
                /* clean up */
                s.Close();
                myList.Stop();

            }
            catch (Exception e)
            {
                Console.WriteLine("Error..... " + e.StackTrace);
            }
        }

    }
}