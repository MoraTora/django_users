import requests

from vk.models import VkUser


class VKService:
    @staticmethod
    def _get_raw_users(access_token: str) -> list[dict]:
        """
        Получение списка пользователей из API VK
        :param access_token: токен авторизации
        :return: сырые данные из API VK
        """
        url = 'https://api.vk.com/method/users.search'
        params = {
            'sort': 1,
            'count': 1000,
            'fields': 'photo',
            'city': 78,
            'access_token': access_token,
            'v': 5.131
        }
        response = requests.post(url, data=params)
        if response.status_code != 200:
            return []
        data = response.json()
        return data['response']['items']

    @staticmethod
    def _save_response_data_to_database(data: list[dict]):
        """
        Сохранение полученных данных в БД
        :param data: данные для сохранения
        """
        for d in data:
            user, _ = VkUser.objects.get_or_create(vk_id=d['id'])
            user.photo = d['photo']
            user.last_name = d['last_name']
            user.first_name = d['first_name']
            user.save()

    def get_users(self, access_token: str) -> list[VkUser]:
        """
        Получение пользователей из ВК и сохранение в БД
        :param access_token: токен доступа ВК
        """
        data = self._get_raw_users(access_token)
        self._save_response_data_to_database(data)
        return VkUser.objects
