using System;
using System.Net.Mail;

namespace MailServer
{
    public class Mail
    {
        public static void Main(string[] args)
        {
            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();
            mail.To.Add("hrscorreia@gmail.com");
            mail.From = new MailAddress("hrscorreia@gmail.com", "Email head", System.Text.Encoding.UTF8);
            mail.Subject = "POC";
            mail.SubjectEncoding = System.Text.Encoding.UTF8;
            mail.Body = "Pacman online challenge";
            mail.BodyEncoding = System.Text.Encoding.UTF8;
            mail.IsBodyHtml = true;
            mail.Priority = MailPriority.High;
            SmtpClient client = new SmtpClient();
            client.Credentials = new System.Net.NetworkCredential("mail", "password");
            client.Port = 587;
            client.Host = "smtp.gmail.com";
            client.EnableSsl = true;
            try
            {
                client.Send(mail);

            }
            catch (Exception ex)
            {
                Exception ex2 = ex;
                string errorMessage = string.Empty;
                while (ex2 != null)
                {
                    errorMessage += ex2.ToString();
                    ex2 = ex2.InnerException;
                }
            }
        }
    }
}