from django.db import models
from django.utils.translation import gettext_lazy as _


class Sex(models.TextChoices):
    MALE = 'Male', _('Male')
    FEMALE = 'Female', _('Female')
    OTHER = 'Other', _('Other')


class EducationLevel(models.TextChoices):
    PRIMARY_SCHOOL = 'Primary School', _('Primary School')
    JUNIOR_HIGH_SCHOOL = 'Junior High School', _('Junior High School')
    SENIOR_HIGH_SCHOOL = 'Senior High School', _('Senior High School')
    DIPLOMA_DEGREE = 'Diploma Degree', _('Diploma Degree')
    BACHELOR_DEGREES = 'Bachelor Degrees', _('Bachelor Degrees')
    MASTER_DEGREES = 'Master Degrees', _('Master Degrees')
    DOCTORAL_DEGREES = 'Doctoral Degrees', _('Doctoral Degrees')
    OTHER = 'Other', _('Other')


class Occupation(models.TextChoices):
    AGRICULTURE_AND_FARMING = 'Agriculture and Farming', _('Agriculture and Farming')
    EDUCATION = 'Education', _('Education')
    HEALTHCARE = 'Healthcare', _('Healthcare')
    HOSPITALITY_AND_TOURISM = 'Hospitality and Tourism', _('Hospitality and Tourism')
    ENGINEERING_AND_MANUFACTURING = 'Engineering and Manufacturing', _('Engineering and Manufacturing')
    ENTREPRENEURSHIP_AND_BUSINESS = 'Entrepreneurship and Business', _('Entrepreneurship and Business')
    ARTS_AND_CULTURE = 'Arts and Culture', _('Arts and Culture')
    CONSTRUCTION_AND_ARCHITECTURE = 'Construction and Architecture', _('Construction and Architecture')
    CUSTOMER_SERVICE_AND_SALES = 'Customer Service and Sales', _('Customer Service and Sales')
    FINANCE_AND_ACCOUNTING = 'Finance and Accounting', _('Finance and Accounting')
    OTHER = 'Other', _('Other')
