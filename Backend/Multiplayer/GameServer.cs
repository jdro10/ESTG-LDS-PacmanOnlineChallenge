using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace GameServer
{
    public class GameServer
    {
        static string coordenadasJog1 = "-";
        static string coordenadasJog2 = "-";

        static string data = null;
        public static void Main()
        {
            Thread t = new Thread(Teste);
            t.Start();
            try
            {
                IPAddress ipAd = IPAddress.Parse("192.168.1.65");

                TcpListener myList = new TcpListener(ipAd, 8001);

                myList.Start();

                Console.WriteLine("The server is running at port 8001...");
                Console.WriteLine("The local End point is  :" +
                                  myList.LocalEndpoint);
                Console.WriteLine("Waiting for a connection.....");

                Socket so = myList.AcceptSocket();
                Console.WriteLine("Connection accepted from " + so.RemoteEndPoint);

                data = null;

                byte[] b = new byte[100];
                
                while (true)
                {

                    int bytesRec = so.Receive(b);  
                    data = Encoding.ASCII.GetString(b,0,bytesRec);  
                    Console.WriteLine( "Jogador1: " + data); 
                    coordenadasJog1 = data;
                                    
                    ASCIIEncoding asen = new ASCIIEncoding();
                    so.Send(asen.GetBytes(coordenadasJog2));               
                }

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

                TcpListener myList = new TcpListener(ipAd, 8002);

                myList.Start();

                Console.WriteLine("The server is running at port 8002...");
                Console.WriteLine("The local End point is  :" +
                                  myList.LocalEndpoint);
                Console.WriteLine("Waiting for a connection.....");

                Socket s = myList.AcceptSocket();
                Console.WriteLine("Connection accepted from " + s.RemoteEndPoint);

                data = null;

                byte[] b = new byte[100];
                
                while (true)
                {
                    int bytesRec = s.Receive(b);  
                    data = Encoding.ASCII.GetString(b,0,bytesRec);  
                    Console.WriteLine( "Jogador2:" + data); 
                    coordenadasJog2 = data;
                                    
                    ASCIIEncoding asen = new ASCIIEncoding();
                    s.Send(asen.GetBytes(coordenadasJog1));                    
                }
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