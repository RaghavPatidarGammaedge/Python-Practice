from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import MyUsers
class UsersJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token.get("user_id")
            return MyUsers.objects.get(id=user_id)
        except MyUsers.DoesNotExist:
            return None