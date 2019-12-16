using System.Net.Mail;

namespace API.Services
{
    public class EmailService
    {
        public void sendSignupMail(string emailToSend, string username, string password)
        {
            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();

            mail.To.Add(emailToSend);
            mail.From = new MailAddress("no.reply.pacman.online@gmail.com", "Pacman Online Challenge", System.Text.Encoding.UTF8);
            mail.Subject = "Registo";
            mail.SubjectEncoding = System.Text.Encoding.UTF8;
            mail.Body = "Obrigado por jogar PACMAN ONLINE. O seu registo está confirmado.\r\n"
                        + "Username: " + username + "\r\n"
                        + "Password: " + password + "\r\n";
            mail.BodyEncoding = System.Text.Encoding.UTF8;
            mail.IsBodyHtml = true;
            mail.Priority = MailPriority.High;
            SmtpClient client = new SmtpClient();

            client.Credentials = new System.Net.NetworkCredential("no.reply.pacman.online@gmail.com", "LdsPOC20192020");
            client.Port = 587;
            client.Host = "smtp.gmail.com";
            client.EnableSsl = true;

            client.Send(mail);
        }

        public void newPasswordRequest(string emailToSend, string username, string password)
        {
            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();

            mail.To.Add(emailToSend);
            mail.From = new MailAddress("no.reply.pacman.online@gmail.com", "Pacman Online Challenge", System.Text.Encoding.UTF8);
            mail.Subject = "Nova Password";
            mail.SubjectEncoding = System.Text.Encoding.UTF8;
            mail.Body = "Aqui está a sua nova password.\r\n"
                        + "Username: " + username + "\r\n"
                        + "Password: " + password + "\r\n";
            mail.BodyEncoding = System.Text.Encoding.UTF8;
            mail.IsBodyHtml = true;
            mail.Priority = MailPriority.High;
            SmtpClient client = new SmtpClient();

            client.Credentials = new System.Net.NetworkCredential("no.reply.pacman.online@gmail.com", "LdsPOC20192020");
            client.Port = 587;
            client.Host = "smtp.gmail.com";
            client.EnableSsl = true;

            client.Send(mail);
        }
    }
}