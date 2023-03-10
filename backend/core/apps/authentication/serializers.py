from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.apps.authentication.models import User
from core.apps.finance.models import BankAccount
from core.apps.finance.serializers import BankAccountCreateSerializer, BankAccountListSerializer


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'address',
            'bank_account',
            'birthday',
            'education_level',
            'email',
            'first_name',
            'id_card_image',
            'id_card_number',
            'image',
            'last_name',
            'occupation',
            'phone_number',
            'sex',
        ]


class UserWriteSerializer(UserBaseSerializer):
    bank_account = BankAccountCreateSerializer()
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    id_card_number = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta(UserBaseSerializer.Meta):
        fields = sorted(['password', 'confirm_password'] + UserBaseSerializer.Meta.fields)

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({'password': 'Password did not match'})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        bank_account_data = validated_data.pop('bank_account', None)
        bank_account = BankAccount.objects.create(**bank_account_data) if bank_account_data else None
        return User.objects.create_user(bank_account=bank_account, **validated_data)


class UserReadSerializer(UserBaseSerializer):
    bank_account = BankAccountListSerializer()

    class Meta(UserBaseSerializer.Meta):
        fields = ['id'] + UserBaseSerializer.Meta.fields
