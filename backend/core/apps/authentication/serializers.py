from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.apps.authentication.models import User
from core.apps.finance.models import BankAccount
from core.apps.finance.serializers import BankAccountCreateSerializer, BankAccountReadSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    bank_account = BankAccountCreateSerializer(required=False)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    id_card_number = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        exclude = [
            'date_joined',
            'groups',
            'id',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'user_permissions',
        ]

    def validate(self, data):
        if data.get('password') != data.pop('confirm_password', None):
            raise serializers.ValidationError({'password': 'Password did not match'})
        return data

    def create(self, validated_data):
        bank_account_data = validated_data.pop('bank_account', None)
        user = User.objects.create_user(**validated_data)
        if bank_account_data:
            BankAccount.objects.create(user=user, **bank_account_data)
        return user


class UserReadSerializer(serializers.ModelSerializer):
    bank_account = BankAccountReadSerializer()

    class Meta:
        model = User
        exclude = [
            'date_joined',
            'groups',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'password',
            'user_permissions',
        ]
