#https://support.google.com/mail/?p=BadCredentials
#https://github.com/shawwwn/uMail
import umail
smtp = umail.SMTP('smtp.gmail.com', 587,
                  username='koufdell@gmail.com',
                  password='koufdell1983')
smtp.to('boujrida.mohamedoussama@gmail.com')
smtp.send("esp32 mail test")
smtp.quit()