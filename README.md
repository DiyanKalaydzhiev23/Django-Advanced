# Theory tests

---

# Plans

### Authentication and Autorization

1. Какво означават?
   - Ауторизация е проверката за това какви права иначе като потребители
   - Аутентикацията е проверката за това кои сме ние (логване в профил)

2. Видове credentials
   - Потребителско име и парола - Single-factor authentication
   - Tелефонен номер, на който се изпраща парола - Multi-factor authentication
 
3. Authentication in Django
   - django.contrib.auth
   - Е допълнителен пакет, както админа
   - Дава ни permissions, groups, users
   - Cookie Based user session handling
      - При логин `Django` създава ключ към сесията и го пази в coоkie, което пази в таблица django_session бекенда и на всяка заявка го изпраща и сравнява със session middleware, за да знае от кой е изпратено
      - SESSION_COOKIE_HTTPONLY = True - позволява изпращането на session_key само през https
      - CSRF_COOKIE_HTTPONLY = True - Не позволява на бразъра да достъпва кукито през document.cookie 
   - AuthMiddleware взима потребителя
   - Работи заедно с django.contrib.contenttypes
  

4. Django Permissions 
   - Имаме таблица с permissions, всеки път когато направим нов модел се добавят нови permissions
   - Те представляват позволения за CRUD операции


5. Built-in Django User
   - User(AbstractUser)
     - Може да бъде намерен в моделите на django.auth app-a
     - таблица auth_users
     - Имаме го във всяка заявка и можем да го достъпим с request.user
     - Django ни позволява да променяме вградения потребителски модел на няколко нива
       - Можем само да го надградим наследявайки AbstractUser или изцяло да го заменим наследявайки AbstractBaseUser
     - Дава ни PermissionsMixin, който вграденият User модел наследява.
       - Той се грижи за това дали потребителя е superuser, какви права има и в какви групи е
       - Дава ни **staff_member_required** декоратор
     - USERNAME_FIELD ни позволява да презапишем полете, което ще се използва за първи креденшъл
     - email_user() ни позволява да изпращаме имейли на потребителите след настройка на SMTP
     - **AnonymusUser**, който не е модел, но клас, който презаписва всички атрибути на базовия клас
     - Дава ни 2 основни функции
       - login - закача cookie за аутентикирания  потребител
       - authenticate - проверява дали креденшълите на потребителя са верни
     - get_user_model() - дава ни модела, който се използва за user в апликацията

6. Login
   - Django ни дава готово **LoginView**
   - Когато ползваме LoginView получаваме следните параметри:
     - next - помага ни да редиректнем потребителя към view-то, което се е опитал да достъпи преди да е бил логнат
     - site - url-a на уебсайта
  
7. Register
   - Нямаме view за регистрация, но имаме форма
   ```py
   class UserRegisterView(CreateView):
       form_class = UserCreationForm
       template_name = 'registration/register.html'
       success_url = reverse_lazy('login')


   # settings.py - optional
   LOGIN_REDIRECT_URL = '/'
   LOGOUT_REDIRECT_URL = '/'

    <form method="post" action="{% url 'login' %}{% if next %}?next={{ next }}{% endif %}">
     {% csrf_token %}
     {{ form.as_p }}
     <button type="submit">Login</button>
    </form>


   ```
   - Формата обаче работи само с User-a от Django, но има как да променим това
   ```py
      class CustomUserCreationForm(UserCreationForm):
          class Meta(UserCreationForm.Meta):
              model = get_user_model()  # Use the custom user model
              fields = ('username', 'email') 
   ```

8. Passowords
   - Използват one-way hash
   - Имаме Views за промяна на паролите
  
9. Groups
   - has_perm()
   - PermissionsMixin
   - permission_required() - декоратор

---
