# Django Advanced


### Workshops
- [Petstagram Repo](https://github.com/DiyanKalaydzhiev23/petstagram-2024.git)

### Theory Tests

- [Authentication and Authorization](https://forms.gle/VX4QFtCwmg2NApnx8)

---

- [User Model and Password Management](https://forms.gle/kuLJxNqj3AE2sn9h9)

---

- [Extending User Model](https://forms.gle/yLaStauEmS6iZsKm6)

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

### User Model and Password Management

1. Built-in Django User
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

2. Login
   - Django ни дава готово **LoginView**
   - Когато ползваме LoginView получаваме следните параметри:
     - next - помага ни да редиректнем потребителя към view-то, което се е опитал да достъпи преди да е бил логнат
     - site - url-a на уебсайта
  
3. Register
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

4. Passowords
   - Използват one-way hash
   - Имаме Views за промяна на паролите
  
5. Groups
   - has_perm()
   - PermissionsMixin
   - permission_required() - декоратор

---


---

### Extending the user model

`AUTH_USER_MODEL = 'path.to.my.model'`

 1. Защо наследяваме AbstractUser, а не USER?
    - Както помним от Python ORM, ако наследим неабстрактен модел, то ние получаваме 1-To-1 relationship
    - Докато, ако е абстрактен, получаваме директно полетата в една таблица

2. AbstractUser vs AbstractBaseUser
   - AbstractUser е user-a, който познаваме, този който Django наследява. Той наследява AbstractBaseUser
   - AbstractBaseUser съдържа само 2 полета, password и last_login
  
3. Начини за наследяване
   - Чрез Proxy
     - Pros: 
        - Можем да добавим методи и мета данни продължавайки да използваме модела от Django
        - Няма нужда да пренаписваме Django Auth system
     - Cons:
        - Не можем да добавяме свои полета
          
   - Наследявайки AbstractUser или AbstractBaseUser
     - Pros:
        - Можем да добавяме свои полета
        - Няма нужда да пренаписваме Django Auth system
     - Cons:
        - По-трудна миграция към друг auth model в бъдеще (например, ако искаме да сменим Django Sessions с JWT)
          
   - Наследяваки User в модел Profile
     - Създаваки профил към всеки потребител чрез One-to-One
     - Pros:
        - Можем да добавяме свои полета
        - По-лесна миграция към друг auth model в бъдеще (например, ако искаме да сменим Django Sessions с JWT)
     - Cons:
        - Трябва да пренаписваме Django Auth system
      
      - Може да стане по два начина:
        - Наследявайки built-in user
        - Създавайки наш user
       
      - Ще ни трябва да променим register платформата
     ```py
           class CustomUserCreationForm(UserCreationForm):
             profile_field = forms.FieldType()
     
             class Meta(UserCreationForm.Meta):
                 model = get_user_model()  # Use the custom user model
                 fields = ('username', 'email')

              def save(self, commit=True):
                 user = super().save(commit=commit)

                 profile = Profile(
                     user=user,
                     age=self.cleaned_data["age"]
                 )

                 if commit:
                    profile.save()

              retrun user
     ```

4. User с AbstractBaseUser
   ##### Step 1: Create a model and a manager
   ```py
   from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
   from django.db import models
   from django.utils.translation import gettext_lazy as _

   class CustomUserManager(BaseUserManager):
       def create_user(self, email, password=None, **extra_fields):
           if not email:
               raise ValueError(_('The Email field must be set'))
           email = self.normalize_email(email)
           user = self.model(email=email, **extra_fields)
           user.set_password(password)
           user.save(using=self._db)
           return user
   
       def create_superuser(self, email, password=None, **extra_fields):
           extra_fields.setdefault('is_staff', True)
           extra_fields.setdefault('is_superuser', True)
   
           if extra_fields.get('is_staff') is not True:
               raise ValueError(_('Superuser must have is_staff=True.'))
           if extra_fields.get('is_superuser') is not True:
               raise ValueError(_('Superuser must have is_superuser=True.'))
   
           return self.create_user(email, password, **extra_fields)

   class CustomUser(AbstractBaseUser, PermissionsMixin):
       email = models.EmailField(unique=True)
       first_name = models.CharField(max_length=30, blank=True)
       last_name = models.CharField(max_length=30, blank=True)
       is_active = models.BooleanField(default=True)
       is_staff = models.BooleanField(default=False)
       date_joined = models.DateTimeField(auto_now_add=True)
   
       objects = CustomUserManager()
   
       USERNAME_FIELD = 'email'
       REQUIRED_FIELDS = []
   
       def __str__(self):
           return self.email

   ```

   ##### Step 2: Configure settings
   ```py
   AUTH_USER_MODEL = 'accounts.CustomUser'
   ````

   
   ##### Step 3: Modify the User Creation Form
      - In accounts/forms.py, import get_user_model() and use it to define the form class:
      ```py
      class CustomUserCreationForm(UserCreationForm):
          class Meta:
              model = get_user_model()  # Dynamically get the user model
              fields = ('email', 'first_name', 'last_name')
      ```

   ##### Step 4: Update the Registration View
      - Ensure your registration view is correctly set up to use the CustomUserCreationForm:
      - In accounts/views.py:
      ```py
      class RegisterView(CreateView):
          form_class = CustomUserCreationForm
          template_name = 'accounts/register.html'
          success_url = reverse_lazy('login')

            
      class CustomLoginView(LoginView):
          form_class = CustomUserLoginForm
          template_name = 'accounts/login.html'
      ```

   ##### Step 5: Admin
      After creating a custom user model, you also need to configure the Django admin to manage users via the admin interface. 
      
      In your `accounts/admin.py`, register your custom user model with the Django admin interface. You need to create a custom `ModelAdmin` class to specify how the model should be displayed in the admin interface.
      
      ### `accounts/admin.py`
      
      ```python
         from django.contrib import admin
         from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
         from django.contrib.auth import get_user_model
         from django.utils.translation import gettext_lazy as _
         from .forms import CustomUserCreationForm
         
         CustomUser = get_user_model()
         
         class CustomUserAdmin(BaseUserAdmin):
             add_form = CustomUserCreationForm
             form = CustomUserCreationForm
             model = CustomUser
             list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
             list_filter = ('is_staff', 'is_active')
             fieldsets = (
                 (None, {'fields': ('email', 'password')}),
                 (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
                 (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
                 (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
             )
             add_fieldsets = (
                 (None, {
                     'classes': ('wide',),
                     'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active')}
                 ),
             )
             search_fields = ('email',)
             ordering = ('email',)
         
         admin.site.register(CustomUser, CustomUserAdmin)
      ```

5. Signals
   - Publish-Subscribe Pattern
   - Имаме няколко типа сигнали:
     - model
     - request
     - management
     - etc...
   - Като се случи някакво събитие да се изпълни даден код
   ```py
      # accounts/models.py
      from django.conf import settings
      from django.db import models
      from django.contrib.auth import get_user_model
      
      class Profile(models.Model):
          user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
          bio = models.TextField(blank=True)
          location = models.CharField(max_length=100, blank=True)
      
          def __str__(self):
              return self.user.email

      # accounts/signals.py
   
      from django.db.models.signals import post_save
      from django.dispatch import receiver
      from django.conf import settings
      from .models import Profile
      
      @receiver(post_save, sender=settings.AUTH_USER_MODEL)
      def create_profile(sender, instance, created, **kwargs):
          if created:
              Profile.objects.create(user=instance)

      # accounts/apps.py

      from django.apps import AppConfig
      
      class AccountsConfig(AppConfig):
          default_auto_field = 'django.db.models.BigAutoField'
          name = 'accounts'
      
          def ready(self):
              import accounts.signals
   ```
   
---
