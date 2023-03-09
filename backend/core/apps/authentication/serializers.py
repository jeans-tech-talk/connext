from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.apps.authentication.models import BankAccount, User


class BankAccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['bank', 'branch', 'account_name', 'account_number']


class BankAccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['id', 'bank', 'branch', 'account_name', 'account_number']


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    bank_account = BankAccountCreateSerializer(allow_null=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
            'sex',
            'birthday',
            'id_card_number',
            'id_card_image',
            'image',
            'address',
            'phone_number',
            'education_level',
            'occupation',
            'bank_account',
        ]

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({'password': 'Password did not match'})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        bank_account_data = validated_data.pop('bank_account')
        bank_account = BankAccount.objects.create(**bank_account_data) if bank_account_data else None
        return User.objects.create_user(bank_account=bank_account, **validated_data)


class UserListSerializer(serializers.ModelSerializer):
    bank_account = BankAccountListSerializer()

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'sex',
            'birthday',
            'id_card_number',
            'id_card_image',
            'image',
            'address',
            'phone_number',
            'education_level',
            'occupation',
            'bank_account',
        ]
