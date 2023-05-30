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
<p dir="auto"><strong>Для запуска проекта необходимо вам понадобится склонировать его на свой ПК через&nbsp;git clone, активировать виртуальное окружение, установить все необходимый зависмости из&nbsp;requirements.txt, перейти в корень проекта, в трех окнах терминала поочередно запустить: &nbsp;в первом окне - Celery для асинхронной обработки задач по отправке писем (письма будут приходить туда); во втором окне -&nbsp;Celery&nbsp;для&nbsp;обработки периодических задач; и в последнем окне сервер проекта. Не забываем о запуске Redis;)</strong></p>
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

<h4><strong>Пара слов о сайте и его работе:</strong></h4>

<ul>
<li><strong>На главной странице сайта организован поиск по объявлениям с пагинацией по страницам</strong></li>
</ul>

![Image 5](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-17-14.png)

<ul>
<li><strong>Есть возможность открыть отдельное объявление и оставить комментарий или посмотреть чужие комментарии и их активность. Если кто-то оставит свой комментарий под объявлением, то автору придет оповещение об этом на почту</strong></li>
</ul>

![Image 6](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-19-45.png)
![Image 7](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-20-17.png)
![Image 8](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-23-07.png)

<ul>
<li><strong>Оставлять комментарии или создавать объявления могут только зарегистрированные пользователи, которые ввели код подтверждения. Для остальных переработано исключение 403</strong></li>
</ul>

![Image 9](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-32-33.png)

<ul>
<li><strong>Авторы объявлений могут откликаться на комментарии пользователей в своих объявлениях или удалять их. Также автор имеет возможность редактировать свои объявления или удалять их. Если автор откликниться на комментарий или отклонит его, то пользователю, который оставил комментарий, придет сообщение об этом на почту</strong></li>
</ul>

![Image 10](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-21-47.png)
![Image 11](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-24-12.png)
![Image 12](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-24-51.png)
![Image 13](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-26-25.png)
![Image 14](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-25-24.png)

<ul>
<li><strong>При отсутствие комментариев, будет выводиться соответствующее сообщение</strong></li>
</ul>

![Image 15](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-25-50.png)

<ul>
<li><strong>Для создания объявления у автора есть отдельная страница с подключенным редактором CKeditor, который позволяет прикреплять видео и картинки из сети</strong></li>
</ul>

![Image 16](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-27-31.png)

<ul>
<li><strong>У пользователя есть своя страница с профилем, где он может редактировать его или переходить на личную страницу со списком комментариев к его объявлениям</strong></li>
</ul>

![Image 17](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-28-08.png)
![Image 18](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-28-31.png)
![Image 19](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-29-00.png)

<ul>
<li><strong>На личной странице со списком комментариев к его объявлениям у автора есть возможность поиска и пагинации страниц комментариев, отклика или удаления комментариев, а также возможность открывать комментарии по отдельности</strong></li>
</ul>

![Image 20](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-29-31.png)
![Image 21](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-30-12.png)
![Image 22](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-30-51.png)

<ul>
<li><strong>При регистрации нового пользователя ему придет письмо со ссылкой для подтверждения регистрации. А после подтверждения регистрации, придет код, который дает право быть автором и создавать объявления. Этот код он вводит в соответсующее поле в ЛК</strong></li>
</ul>

![Image 23](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-33-22.png)
![Image 24](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-58-41.png)
![Image 25](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-31-48.png)
![Image 26](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_12-59-40.png)

<ul>
<li><strong>Так же пользователи будут получать рассылку с еженедельным дайджестом новых объявлений</strong></li>
</ul>

![Image](https://github.com/Russiks/BulletinBoard_MMORPG/blob/main/Images/2023-05-30_13-03-11.png)


