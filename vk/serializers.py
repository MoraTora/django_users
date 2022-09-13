from vk.models import VkUser


def convert_vk_user_to_dict(user: VkUser) -> dict:
    return {
        'vk_id': user.vk_id,
        'photo': user.photo,
        'last_name': user.last_name,
        'first_name': user.first_name,
        'url': user.url
    }
