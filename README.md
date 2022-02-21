# Twitch-bot-song-info-from-spoify
Twitch bot with a built-in song function. She takes information about the music that is playing now


RU 🇷🇺 :
1. Устанавливаем python3.10 https://www.python.org/downloads/

2. Открываем консоль в папке и пишем команды по очереди 
						pip install twitchio
						pip install spotipy
						
3. Достаём токен spotify и secret. Переходим по ссылке https://developer.spotify.com/dashboard/ и логинимся в аккаунт. Нажимаем create an app ![123](https://user-images.githubusercontent.com/87109163/154803557-08be5cfc-5a15-48b8-8fef-29e6cf769974.png)

И в получивимся приложении берём Client ID и Client Secret ![234](https://user-images.githubusercontent.com/87109163/154803601-95f1f89b-d5e9-48b6-9403-006a47593bac.png)

И вставляем в конфиг

Также тут же заходим в настройки приложения ('EDIT SETTINGS') и в область 'Redirect URIs' вписываем 'https://google.com/' ![Screenshot_1](https://user-images.githubusercontent.com/87109163/154967612-15a90f18-18d3-448e-89f6-b09c808c1e99.png)

И сохраняем

4. Достаём twitch токен из https://twitchtokengenerator.com/
![Screenshot_2](https://user-images.githubusercontent.com/87109163/154968163-8a1e04ec-b768-487c-aa5e-010f104248df.png)

Выбираем bot chat token и логинимся в аккаунт бота

Нужно взять access token

![Screenshot_3](https://user-images.githubusercontent.com/87109163/154968387-757bfcd0-05fc-49e1-9bb7-9b4907dd702a.png)

5. После вставляем все токены в файл config.py и запускаем код main.py -->  py main.py

6. После запуска у вас откроется сайт авторизации spotify. Вам нужно авторизироваться и передать получившуюся ссылку google.com в консоль

7. Всё готово!!!


EN 🇬🇧 :
1. Download python3.10 https://www.python.org/downloads/


2. Open the console in the folder and write commands in turn
						pip install twitchio
						pip install spotipy
						
3. We get the spotify token and secret. Let's follow the link https://developer.spotify.com/dashboard/ and log into the account. Click create an app ![123](https://user-images.githubusercontent.com/87109163/154803557-08be5cfc-5a15-48b8-8fef-29e6cf769974.png)

And in the resulting application we take Client ID and Client Secret ![234](https://user-images.githubusercontent.com/87109163/154803601-95f1f89b-d5e9-48b6-9403-006a47593bac.png)

And paste in the config

Also immediately go to the application settings ('EDIT SETTINGS') and in the 'Redirect URIs' area enter 'https://google.com/' ![Screenshot_1](https://user-images.githubusercontent.com/87109163/154967612-15a90f18-18d3-448e-89f6-b09c808c1e99.png)

And save

4. Get a twitch token https://twitchtokengenerator.com/
![Screenshot_2](https://user-images.githubusercontent.com/87109163/154968163-8a1e04ec-b768-487c-aa5e-010f104248df.png)

Select bot chat token and log in to the bot account

You need to take an access token

![Screenshot_3](https://user-images.githubusercontent.com/87109163/154968387-757bfcd0-05fc-49e1-9bb7-9b4907dd702a.png)

5. After we insert all the tokens into the config.py file and run the code main.py --> py main.py

6. Once launched, you will have the spotify authorization site open. You need to log in and pass the resulting google.com link to the console 

7. Everything is ready!!
