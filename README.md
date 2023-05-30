# BulletinBoard_MMORPG
 SkillFactoryStudy

<h3><strong>Доска объявлений для фанатского MMORPG-сервера</strong></h3>
____________________________________________________________________________________________________________
</p></p></p>
<p><em>Техническое задание:</em></p>
<p><span style="color: #808080;">"Нам необходимо разработать интернет-ресурс для фанатского сервера одной известной MMORPG &mdash; что-то вроде доски объявлений. Пользователи нашего ресурса должны иметь возможность зарегистрироваться в нём по e-mail, получив письмо с кодом подтверждения регистрации. После регистрации им становится доступно создание и редактирование объявлений. Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент. Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём. Также пользователю должна быть доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление). Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.</span></p>
<p><span style="color: #808080;">Также мы бы хотели иметь возможность отправлять пользователям новостные рассылки."</span></p>
____________________________________________________________________________________________________________

</p></p></p>
<p dir="auto"><strong>Для запуска полекта необходимо вам понадобится склонировать его на свой ПК через&nbsp;git clone, активировать виртуальное окружение, установить все необходимый зависмости из&nbsp;requirements.txt, перейти в корень проекта, в трех окнах терминала поочередно запустить: &nbsp;в первом окне - Celery для асинхронной обработки задач по отправке писем (письма будут приходить туда); во втором окне -&nbsp;Celery&nbsp;для&nbsp;обработки периодических задач; и в последнем окне сервер проекта. Не забываем о запуске Redis;)</strong></p>
<p dir="auto"><span style="text-decoration: underline;"><em>Необходимые команды:</em></span></p>
<ul dir="auto">
<li><span style="color: #ff0000;">redis-server</span> - запуск Redis (проверить работу можно через команду redis-cli ping - в ответ вы получите pong, если все работает)</li>
<li><span style="color: #ff0000;">git clone *ссылка на проект*</span> - клонируем проект</li>
<li><span style="color: #ff0000;">venv\scripts\activate</span> - активируем виртуалку</li>
<li><span style="color: #ff0000;">pip install -r requirements.txt</span> - устанавливаем зависимости</li>
<li><span style="color: #ff0000;">cd *имя проекта*</span> - переходим в корень проекта</li>
<li><span style="color: #ff0000;">celery -A BoardSetting worker -l INFO --pool=solo</span> - асинхронная обработка</li>
<li><span style="color: #ff0000;">celery -celery -A BoardSetting beat -l INFO</span> - периодические задачи</li>
<li><span style="color: #ff0000;">py manage.py runserver</span> - запуск сервера <a href="http://127.0.0.1:8000/" rel="nofollow">http://127.0.0.1:8000/</a></li>
</ul>

</p></p></p>

<li><strong>Работа Redis</strong></li>

![Image 1](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-00-16.png)

<li><strong>Работа Celery worker</strong></li>

![Image 2](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-04-29.png)

<li><strong>Работа Celery beat</strong></li>

![Image 3](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-05-32.png)

<li><strong>Работа runserver</strong></li>

![Image 4](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-06-30.png)


![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()
![Image]()

