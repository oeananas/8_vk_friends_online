import vk
import getpass

APP_ID = 6440852


def get_user_login():
    login = input('VK Login: ')
    return login


def get_user_password():
    password = getpass.getpass(prompt='VK Password: ')
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline(v=5.52)
    friends_online = api.users.get(v=5.52, user_ids=friends_online_ids)
    return friends_online


def output_friends_to_console(friends_online):
    print('Your VK friends online:')
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    try:
        login = get_user_login()
        password = get_user_password()
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        exit('You entered incorrect login / password')
