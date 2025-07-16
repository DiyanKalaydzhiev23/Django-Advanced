# Django Advanced


### Workshops
- [Petstagram Repo](https://github.com/DiyanKalaydzhiev23/petstagram-2024.git)
- [Rest Client](https://github.com/DiyanKalaydzhiev23/JWT-Django-REST-FE-Softuni)

### Theory Tests

- [Authentication and Authorization](https://forms.gle/VX4QFtCwmg2NApnx8)

---

- [User Model and Password Management](https://forms.gle/kuLJxNqj3AE2sn9h9)

---

- [Extending User Model](https://forms.gle/yLaStauEmS6iZsKm6)

---

- [Middlewares and Sessions](https://forms.gle/QdK1qzN3qo4HfkU3A)

---

- [Django REST Basics](https://forms.gle/9ou2q8U97LmfQHMs9)

---

- [Django REST Advanced](https://forms.gle/h5TvbecgszVhjfau5)

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


---


### Django Middlewares and Sessions

1. Какво е Middleware?
   - Функционалност, която се изпълнява преди и/или след **всеки** рекуест
   - Доста наподобява това да направим миксин, но с middleware-a няма нужда да го наследяваме никъде. Тоест става абстрактно.
   - Реда на изпълнение е важен
   - Middleware-ите се изпълняват top-down, преди заявката и bottom up след нея.
   - Задава се в `settings.py`
   ```py
   MIDDLEWARES = [
      ...,
      Path.to.your.callable,  # callable - something that overwrites the method __call__
      ...,
   ]
   ```

   - Template for function middleware
   ```py
      def measure_time(get_response):
         def middleware(request, *args, **kwargs): // looks like view
            result = get_response()

            return result

      return middleware
   ```

   - Example
   ```py
      def measure_time(get_response):
         def middleware(request, *args, **kwargs): // looks like view
            start_time = time.time()
            result = get_response(request)
            end_time = time.time()

            print(f"{request.path} executed in {end_time - start_time} seconds.")
   
            return result

      return middleware
   ```

   - С клас
   ```py
   import time

   class RequestTimingMiddleware(MiddlewareMixin):
       """
       Middleware to measure the time taken to process a request using process_request and process_response.
       """

       def __init__(self, get_response):
           self.get_response = get_response
   
       def process_request(self, request):
           # Start time before processing the request
           self.start_time = time.time()
   
       def process_response(self, request, response):
           # End time after processing the request
           end_time = time.time()
   
           # Calculate the duration
           duration = end_time - self.start_time
   
           # Log the duration (you can use any logging mechanism here)
           print(f"Request to {request.path} took {duration:.4f} seconds.")
   
           return response

   ```

   - Освен process_request и process_response, имаме и process_view, което ни позволява да изпълняваме код точно преди view-то да се изпълни
   - С други думи. Всеки middleware се вика три пъти. Преди request, точно преди view и след request.

2. Session
   - HTTP e stateless - не пази никаква информация, всяка заявка е сама за себе си.
   - Сесията е начин по който сървъра може да пази информация за user-a.
   - Сесията в Django е базово имплементирана.
   - Имаме таблица `django_session`, която пази ключ- session key, който се подава на клиента, session_data - стойност с информация за потребителя, и expiration_date - дата, в която тази сесия изтича (default 2 седмици).
   - Ако се логне от два браузъра, ще имаме две сесии за един потребител
   - Сесията в базата е сериализирана, но когато я достъпваме във view тя се десериализира и можем да я третираме като обект
   - Ключовете на обекти в сесията трябва да се string-ове и да нямат специални символи
   ```py
   def view_counter(request): 
    # Check if the 'counter' key exists in the session
    if 'counter' in request.session:
        # Increment the counter
        request.session['counter'] += 1
    else:
        # Initialize the counter if it's the first visit
        request.session['counter'] = 1 

    counter = request.session['counter']

    return HttpResponse(f"View count: {counter}")
   ```

3. Cookies
   - Метаданни за даннте
   - Браузъра ги праща на всяка заявка, към домейна за който са заяазени
   - Пример: cookie sessionId запазено за localhost, всеки път ще праща сесията
   - Cookie-та без дата на изтичане се изтриват на изтичане на сесията на браузъра
   - Няма как да направим вечно куки
   - `request.COOKIES`
   ```py
   from django.http import HttpResponse
   from django.utils.timezone import now
   from django.views import View
   
   class SetTimeCookieView(View):
       def dispatch(self, request, *args, **kwargs):
           # Call the parent dispatch method to get the response
           response = super().dispatch(request, *args, **kwargs)
   
           # Get the current time
           current_time = now()
   
           # Check if the 'last_visit' cookie exists
           last_visit = request.COOKIES.get('last_visit')
           if last_visit:
               # If the cookie exists, add a message about the last visit time
               response.content += f"Your last visit was on: {last_visit}<br>".encode()
           else:
               # If this is the first visit, add a message indicating that
               response.content += "This is your first visit!<br>".encode()
   
           # Set the current time as a cookie named 'last_visit'
           response.set_cookie('last_visit', current_time.strftime('%Y-%m-%d %H:%M:%S'))
   
           # Optionally, set the cookie to expire in a certain number of seconds (e.g., 1 day)
           # response.set_cookie('last_visit', current_time.strftime('%Y-%m-%d %H:%M:%S'), max_age=86400)
   
           # Add a message about setting the cookie
           response.content += f"Setting the current time ({current_time.strftime('%Y-%m-%d %H:%M:%S')}) as a cookie.".encode()
   
           return response

   ```

---



---

### Django REST Basics

1. Какво е API?
   - Application Programing Interface
   - Начин по-който ние можем да се свържем с дадена система, множеството от функционалности, които ние можем да използваме на една система
   - Абстрактен пример: 
     - Порта на телефон и кабел за зареждане. Телефона ни предоставя начин да го зареждаме (с кабел)

2. Какво е REST?
   - ReprEsentational State Transfer
  
3. REST API
   - Множество от ендпойнти чрез, които ние можем да работим с дадена система 
   - Предимно се комуникира с JSON, но реално можем да изпращаме данни под различни формати
   - REST API e stateless, тоест трябва да пазим всичко, което апи-то ни връща на клиента
   - В заключение можем да имаме различни клиенти:
     - Мобилно приложение
     - Уеб приложение
     - Пералня
     - ...
   - Но те всички да изпращат заявки към едно API, и то да им връща резултат като JSON
   - Примери:
     - [Stripe](https://docs.stripe.com/api/connected-accounts)
     - [Swapi](https://swapi.dev/)
     - [PokeApi](https://pokeapi.co/)
     - [Weather API](https://www.visualcrossing.com/weather-api?gad_source=1&gclid=CjwKCAjw59q2BhBOEiwAKc0ijb-nOtbeEpv4Mxv9iJdv6Okno4A4JNJiT1MATH_poGi5PHv2r32z9BoCF34QAvD_BwE)

4. SPA vs MPA
   - SPA - Single Page Application (Client Side Rendering)
     - Приложение често направено с клиент на JS (в контекста на уеб), което за зареждане на нова информация изпраща заявка до API и не ярезарежда страницата.
   - MPA - Multi Page Application (Server Side Rendering)
     - Приложение, което всеки път, в който трябва да изпрати нова информация я рендерира в html на сървъра и врща като отговор този html. Това води до нуждата да презареждаме страницата, всеки път, когато нова информация е нужна или заявка трябва да бъде изпратена.
    
5. Methods
   - В Django ползвахме форми, а формите в html поддържат само post и get
   - Сега имаме възможност да ползваме всички методи
  
6. Django REST Framework
   - Пакет, който ни позволява да създаваме REST API-та
   - Доста близко до Django
   - Дава ни сериализация
     - Начин, по който нашия Django модел да се превърне в JSON обект и обратното
   - Можем и да не го ползваме и да връщаме JSON през нормалното Django, но тогава нещата стават по-сложни, защото трябва да пренапишем всяко Generic view, понеже те връщат темплейт.
   - `pip install djangorestframework`
   ```py
      INSTALLED_APPS = [
         ...,
         'rest_framework
         ...,
      ]
   ```

7. Serializers
   - Начин, по който нашия Django модел да се превърне в JSON обект и обратно
   - Както при формите имаме serializers и ModelSerializers
   ```py
   from rest_framework import serializers
   from .models import Book
   
   class BookSerializer(serializers.ModelSerializer):
       class Meta:
           model = Book
           fields = '__all__'

   from rest_framework import generics
   from .models import Book
   from .serializers import BookSerializer
   
   class BookListCreate(generics.ListCreateAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer

   // or with fbv

   @api_view(['GET', 'POST'])
   def book_list_create(request):
       if request.method == 'GET':
           books = Book.objects.all()
           serializer = BookSerializer(books, many=True)

           return Response(serializer.data)
   
       elif request.method == 'POST':
           serializer = BookSerializer(data=request.data)
   
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)

           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   ```

5. Django Generics vs DRF Generics
   - View
   ```py
      class SimpleView(View):
          def get(self, request, *args, **kwargs):
              context = {
                  'message': 'Hello, this is a simple Django View!'
              }
              return render(request, 'simple_template.html', context)

      class SimpleAPIView(APIView):
          def get(self, request, *args, **kwargs):
              data = {
                  'message': 'Hello, this is a simple APIView response!'
              }
              return Response(data)
   ```
   - ListView
   ```py
      # Django
      from django.views.generic import ListView
      from .models import Book
      
      class BookListView(ListView):
          model = Book
          template_name = 'books/book_list.html'

      # DRF
      from rest_framework import generics
      from .models import Book
      from .serializers import BookSerializer
      
      class BookListAPIView(generics.ListAPIView):
          queryset = Book.objects.all()
          serializer_class = BookSerializer

      @api_view(['GET'])
      def book_list(request):
          books = Book.objects.all()
          serializer = BookSerializer(books, many=True)
          return Response(serializer.data)
   ```

   - DetailView
     ```py
         from django.views.generic import DetailView
         from .models import Book
         
         class BookDetailView(DetailView):
             model = Book
             template_name = 'books/book_detail.html'

        # DRF
         from rest_framework import generics
         from .models import Book
         from .serializers import BookSerializer
         
         class BookDetailAPIView(generics.RetrieveAPIView):
             queryset = Book.objects.all()
             serializer_class = BookSerializer

         @api_view(['GET'])
         def book_detail(request, pk):
             try:
                 book = Book.objects.get(pk=pk)
             except Book.DoesNotExist:
                 return Response(status=status.HTTP_404_NOT_FOUND)
         
             serializer = BookSerializer(book)
             return Response(serializer.data)
     ```

   - CreateView
   ```py
      from django.views.generic import CreateView
      from .models import Book
      from .forms import BookForm
      
      class BookCreateView(CreateView):
          model = Book
          form_class = BookForm
          template_name = 'books/book_form.html'
          success_url = '/books/'

      # DRF
      from rest_framework import generics
      from .models import Book
      from .serializers import BookSerializer
      
      class BookCreateAPIView(generics.CreateAPIView):
          queryset = Book.objects.all()
          serializer_class = BookSerializer

      
      @api_view(['POST'])
      def book_create(request):
          serializer = BookSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   ```

   -UpdateView
   ```py
   from django.views.generic import UpdateView
   from .models import Book
   from .forms import BookForm
   
   class BookUpdateView(UpdateView):
       model = Book
       form_class = BookForm
       template_name = 'books/book_form.html'
       success_url = '/books/'

   # DRF
   from rest_framework import generics
   from .models import Book
   from .serializers import BookSerializer
   
   class BookUpdateAPIView(generics.UpdateAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer

   @api_view(['PUT'])
   def book_update(request, pk):
       try:
           book = Book.objects.get(pk=pk)
       except Book.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
   
       serializer = BookSerializer(book, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   ```

   - DeleteView
   ```py
   class BookDeleteView(DeleteView):
       model = Book
       template_name = 'books/book_confirm_delete.html'
       success_url = '/books/'

   # DRF
   class BookDeleteAPIView(generics.DestroyAPIView):
      queryset = Book.objects.all()

   @api_view(['DELETE'])
   def book_delete(request, pk):
       try:
           book = Book.objects.get(pk=pk)
       except Book.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
   
       book.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   ```
   
---


---

### Django REST Advanced

1. Видове сериалайзъри
   1. Serializer
      - Това е базовият клас за създаване на serializers. В него ръчно дефинирате полетата и начините за обработка на данните.
     ```py
         from rest_framework import serializers
         
         class UserSerializer(serializers.Serializer):
             username = serializers.CharField(max_length=100)
             email = serializers.EmailField()
             is_active = serializers.BooleanField()
         
         # Сериализиране на данни:
         user_data = {
             "username": "john",
             "email": "john@example.com",
             "is_active": True
         }
         serializer = UserSerializer(data=user_data)
         if serializer.is_valid():
             print(serializer.validated_data)
     ```

   2. ModelSerializer
      - ModelSerializer е опростена версия на Serializer, която автоматично създава полетата въз основа на Django модела. Спестява време при сериализация на данни от модели.
      ```py
         from rest_framework import serializers
         from myapp.models import User
         
         class UserSerializer(serializers.ModelSerializer):
             class Meta:
                 model = User
                 fields = ['username', 'email', 'is_active']

      ```
   3. ListSerializer
      - ListSerializer се използва за сериализация на списъци с обекти. Обикновено той се използва вътрешно от Django REST Framework, когато сериализирате множество обекти, но може да бъде дефиниран и ръчно.
      ```py
      from rest_framework import serializers

      class UserSerializer(serializers.Serializer):
          username = serializers.CharField(max_length=100)
      
      class UserListSerializer(serializers.ListSerializer):
          child = UserSerializer()
      
      data = [
          {"username": "john"},
          {"username": "jane"}
      ]
      serializer = UserListSerializer(data=data)
      if serializer.is_valid():
          print(serializer.validated_data)
      ```

   4. HyperlinkedModelSerializer
      - HyperlinkedModelSerializer е подобен на ModelSerializer, но вместо да използва PrimaryKeyRelatedField за релации, използва HyperlinkedIdentityField за URL връзки към други ресурси.
      ```py
      from rest_framework import serializers
      from myapp.models import User
      
      class UserSerializer(serializers.HyperlinkedModelSerializer):
          class Meta:
              model = User
              fields = ['url', 'username', 'email', 'is_active']
      ```
   5. SlugRelatedField
      - SlugRelatedField се използва за релации, като свързва други модели чрез техните уникални полета (например slug поле).
      ```py
      from rest_framework import serializers
      from myapp.models import Post, Category
      
      class PostSerializer(serializers.ModelSerializer):
          category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
      
          class Meta:
              model = Post
              fields = ['title', 'content', 'category']
      ```
   6. PrimaryKeyRelatedField
      - Този сериалайзер използва първичния ключ за релации между модели.
      ```py
      from rest_framework import serializers
      from myapp.models import Post, Category
      
      class PostSerializer(serializers.ModelSerializer):
          category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
      
          class Meta:
              model = Post
              fields = ['title', 'content', 'category']

      ```

   7. StringRelatedField
      - StringRelatedField показва релациите като низове, базирани на __str__() метода на свързания модел.
      ```py
         from rest_framework import serializers
         from myapp.models import Post
         
         class PostSerializer(serializers.ModelSerializer):
             category = serializers.StringRelatedField()
         
             class Meta:
                 model = Post
                 fields = ['title', 'content', 'category']
      ```

   8. SerializerMethodField
      - Този тип поле ви позволява да дефинирате метод в сериалайзера, който връща данни в сериализирана форма.
      ```py
      from rest_framework import serializers
      from myapp.models import User
      
      class UserSerializer(serializers.ModelSerializer):
          full_name = serializers.SerializerMethodField()
      
          class Meta:
              model = User
              fields = ['username', 'email', 'full_name']
      
          def get_full_name(self, obj):
              return f"{obj.first_name} {obj.last_name}"

      ```

   9. HiddenField
      - Поле, което се използва за предаване на стойности, които не се показват в сериализацията (например стойности, които се запълват автоматично).
      ```py
      from rest_framework import serializers
      
      class CommentSerializer(serializers.ModelSerializer):
          created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
      
          class Meta:
              model = Comment
              fields = ['text', 'created_by']
      ```

2. Generic Views
   - Можем да ги комбинираме, тоест можем да имаме RetrieveDestroyView, което има get и delete

3. Actions
   - Шаблон за създаване на urls в REST
   - Пример: Имаме книги и всяка книга може да има коментар
   - Грешно: api/books/4 - където 4 е id-то на книгата
   - Правилно: api/books/4/comment - това наричаме акшън, по този начин няма объркване на какво принадлежи id-то

4. Authentication
   - `rest_framework.authtoken`
   - Апп, който съдържа едно view ObtainAuthToken
     - Тук можем да генерираме токън за съществуващ наш потребител
   - Login
     ```py
     class LoginAPIView(token_views.ObtainAuthToken)
        pass
     ```
   - Register
     ```py
      from django.contrib.auth import get_user_model
      from rest_framework import serializers
      
      UserModel = get_user_model()
      
      class RegisterSerializer(serializers.ModelSerializer):
          password = serializers.CharField(write_only=True)  # Prevent password from being read
      
          class Meta:
              model = UserModel
              fields = ['username', 'email', 'password']  # Adjust fields based on your User model
      
          def create(self, validated_data):
              # Use the create_user method to create a user
              user = UserModel.objects.create_user(
                  username=validated_data['username'],
                  email=validated_data['email'],
                  password=validated_data['password']  # create_user automatically handles hashing
              )
              return user

      from django.contrib.auth import get_user_model
      from rest_framework import generics
      from rest_framework.response import Response
      from rest_framework import status
      
      UserModel = get_user_model()
      
      class RegisterApiView(generics.CreateAPIView):
          queryset = UserModel.objects.all()
          serializer_class = RegisterSerializer
     ```

5. Permissions
   - Можем да използваме mixins от django, но е по-прието да използваме permission classes
      - IsAuthenticated
      - AllowAny
      - IsAdminUser
      - IsAuthenticatedOrReadOnly
      - BasePermission (for creating custom permissions)
   ```py
   from rest_framework.permissions import BasePermission
   
   class IsOwner(BasePermission):
       """
       Custom permission to only allow owners of an object to access or modify it.
       """
       def has_object_permission(self, request, view, obj):
           # Assumes the object has an 'owner' attribute. You can adjust this as needed.
           return obj.owner == request.user

   class MyModelDetailView(generics.RetrieveUpdateDestroyAPIView):
       queryset = MyModel.objects.all()
       serializer_class = MyModelSerializer
       permission_classes = [IsOwner]  # Use the custom permission
   
   ```
    
6. Exceptions
   - Персонализирани грешки
   ```py
      class NotOwnerException(APIException):
          status_code = 403  # HTTP status code for Forbidden
          default_detail = "You do not have permission to perform this action."  # Default error message
          default_code = 'not_owner'
   ```
   - Custom handler
   ```py
   from rest_framework.views import exception_handler  # Import the default DRF exception handler
   from rest_framework.response import Response  # Import DRF's Response class
   from rest_framework.exceptions import APIException  # Import DRF's base API exception
   from rest_framework import status  # Import status codes
   
   def custom_exception_handler(exc, context):
       """
       Custom exception handler to modify the response for exceptions.
       
       Args:
       - exc: The exception instance that was raised.
       - context: A dictionary containing information about the context in which the exception was raised (including the view).
       
       Returns:
       - Response: A DRF Response object that modifies the error response.
       """
   
       # Call DRF's default exception handler first, to get the standard error response.
       response = exception_handler(exc, context)
       
       # If the response is not None, it means DRF has already handled the exception.
       if response is not None:
           # Modify the response for custom behavior (if needed)
           # You can add custom data or wrap the error in a different structure.
           
           # Example: Adding a custom error message or structure to the response
           response.data['status_code'] = response.status_code  # Add status code to the response
           response.data['error_type'] = exc.__class__.__name__  # Add the type of exception to the response
           
           # Optionally, you could modify specific responses for certain exceptions
           if isinstance(exc, APIException):
               # Handle general APIException separately (e.g., add more context)
               response.data['detail'] = str(exc)  # Add the exception message as 'detail'
       
       else:
           # If the response is None, it means DRF's default handler didn't handle this exception.
           # You can create a custom response here.
           
           # Example: Creating a custom response for unhandled exceptions
           return Response({
               "detail": "Something went wrong",  # Custom error message
               "error": str(exc),  # Include the string representation of the exception
               "error_type": exc.__class__.__name__,  # Include the type of the exception
           }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return 500 status for server errors
       
       # Return the modified response or the original response from the default handler.
       return response

   // settings.py
   REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'your_project.your_module.custom_exception_handler',  # Replace with your actual path
   }

   ```
---

