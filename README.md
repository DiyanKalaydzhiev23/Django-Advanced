# Django-Advanced

---

### Workshops
- [Petstagram Repo](https://github.com/DiyanKalaydzhiev23/petstagram-2024.git)

---

### Theory Tests

- [Authentication and Authorization](https://forms.gle/VX4QFtCwmg2NApnx8)

---

# Plans


### Authentication and Autorization

1. Какво означават?
   - Ауторизация е проверката за това какви права инане като потребители
   - Аутентикацията е прое=верката за това кои сме ние (логване в профил)

2. Видове credentials
   - Потребителско име и парола - Single-factor authentication
   - телефонен номер, на който се изпраща парола - Multi-factor authentication
 
3. Authentication in Django
   - django.contrib.auth
   - Е допълнителен пакет, както админа
   - Дава ни permissions, groups, users
   - Cookie Based user session handling
      - При логин Django създава ключ към сесията и го пази в coоkie, което пази в таблица django_session бекенда и на всяка заявка го изпраща и сравнява със session middleware, за да знае от кой е изпратено
      - SESSION_COOKIE_HTTPONLY = True - позволява изпращането на session_key само през https
      - CSRF_COOKIE_HTTPONLY = True - Не позволява на бразъра да достъпва кукито през document.cookie 
   - AuthMiddleware взима потребителя
   - Работи заедно с django.contrib.contenttypes
  

4. Django Permissions 
   - Имаме таблица с permissions, всеки път когато направим нов модел се добавят нови permissions
   - Те представляват позволения за CRUD операции

5.  Web security
   1. SQL инжекция (SQL Injection)
      - SQL инжекцията е атака, при която злонамерен потребител въвежда зловреден SQL код в полета за въвеждане на данни (като форми за логин), с цел да манипулира или извлече данни от базата данни. Тази уязвимост възниква, когато приложението не валидира или не пречиства потребителския вход правилно.
      
   2. Кроссайт скриптиране (XSS)
      - Кроссайт скриптирането е атака, при която злонамерен потребител вкарва зловреден скрипт (обикновено JavaScript) в уебсайт, който след това се изпълнява от браузъра на други потребители. Това може да доведе до кражба на бисквитки, манипулация на съдържание или пренасочване към зловредни сайтове.
   
   3. URL/HTTP манипулационни атаки (Промяна на параметри - Parameter Tampering)
      - При този вид атака, нападателят манипулира URL и ли параметри в HTTP заявка, за да получи неоторизиран достъп до ресурси или да промени поведението на приложението. Например, промяна на параметър в URL, който определя цената на продукт, за да се закупи нещо на по-ниска цена.
   
   4. Кроссайт заявка за фалшификация (CSRF)
      - CSRF атаката принуждава потребител, който е логнат в уеб приложение, да извърши неволно действие (като изпращане на форма или извършване на плащане), без неговото знание. Това се постига чрез изпращане на специално създадена връзка или форма към потребителя.
   
   5. Атаки с груба сила (Brute Force Attacks) и DDoS (Разпределени атаки за отказ от услуга)
      - При атака с груба сила, нападателят автоматично опитва множество комбинации от пароли или ключове, докато не намери правилната. DDoS атаките целят да претоварят уебсайт или услуга с огромен брой заявки, което да доведе до забавяне или пълно прекъсване на услугата.
   
   6. Недостатъчен контрол на достъпа (Insufficient Access Control)
      - Недостатъчният контрол на достъпа е уязвимост, при която потребители или системи получават достъп до ресурси или функционалности, за които нямат разрешение. Това може да доведе до изтичане на конфиденциална информация или изпълнение на неоторизирани действия.
   
   7. Липса на SSL (HTTPS) / Атаки Човек в средата (MITM)
      - Липсата на SSL (HTTPS) прави връзката между потребителя и уебсайта незащитена, което позволява на нападател да прихване, промени или открадне данни (като пароли или лична информация) по време на предаването. MITM атаката възниква, когато нападателят се позиционира между комуникиращите страни и тайно следи или манипулира комуникацията.
   
   8. Фишинг/Социално инженерство (Phishing/Social Engineering)
      - Фишингът и социалното инженерство са методи, при които нападателят измамно убеждава потребителя да разкрие чувствителна информация (като пароли или номера на кредитни карти) или да извърши определено действие (като инсталиране на зловреден софтуер), като се представя за доверено лице или организация.
   
---