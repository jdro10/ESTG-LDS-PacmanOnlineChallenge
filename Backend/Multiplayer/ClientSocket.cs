using System;  
using System.Net;  
using System.Net.Sockets;  
using System.Text;  
  
public class SynchronousSocketClient {  
  
    public static void StartClient() {  
        byte[] bytes = new byte[1024];  
  
        try {  
            IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());  
            IPAddress ipAddress = ipHostInfo.AddressList[1];  
            IPEndPoint remoteEP = new IPEndPoint(ipAddress,65432);  
  
            Socket sender = new Socket(ipAddress.AddressFamily,   
                SocketType.Stream, ProtocolType.Tcp );
    
            try {  
                sender.Connect(remoteEP);  
  
                Console.WriteLine("Socket connected to {0}",  
                    sender.RemoteEndPoint.ToString());  
  
                byte[] msg = Encoding.ASCII.GetBytes("This is a test<EOF>");  
  
                int bytesSent = sender.Send(msg);  
  
                int bytesRec= sender.Receive(bytes);
                
                Console.WriteLine("Received: {0}",  
                Encoding.ASCII.GetString(bytes,0,bytesRec)); 

                while(Encoding.ASCII.GetString(bytes,0,sender.Receive(bytes)) != null){
                    
                    Console.WriteLine("Received: {0}",  
                    Encoding.ASCII.GetString(bytes,0,bytesRec)); 
                    
                    bytesRec = sender.Receive(bytes);
	            }  
  
                sender.Shutdown(SocketShutdown.Both);
                sender.Close();  
  
            } catch (ArgumentNullException ane) {  
                Console.WriteLine("ArgumentNullException : {0}",ane.ToString());  
            } catch (SocketException se) {  
                Console.WriteLine("SocketException : {0}",se.ToString());  
            } catch (Exception e) {  
                Console.WriteLine("Unexpected exception : {0}", e.ToString());  
            }  
  
        } catch (Exception e) {  
            Console.WriteLine( e.ToString());  
        }  
    }  
  
    public static int Main(String[] args) {  
        StartClient();  
        return 0;  
    }  
}  