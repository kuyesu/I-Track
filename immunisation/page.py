from django.db import models
from django import forms
from django.db.models.lookups import StartsWith
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from phonenumber_field.modelfields import PhoneNumberField

# import calendar
# ...

# class MyModel(models.Model):
#     ...

#     MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]

#     month = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')


# from model_utils import Choices

# class MyModel(models.Model):
#    MONTH = Choices(
#        (1, 'JAN', _('January')),
#        (2, 'FEB', _('February')),
#        (3, 'MAR', _('March')),
#    )
#    # [..]
#    month = models.PositiveSmallIntegerField(
#        choices=MONTH,
#        default=MONTH.JAN,
#    )


# from django.utils.translation import ugettext_lazy as _
# from model_utils import Choices

# class MyModel(models.Model):
#    MONTH = Choices(
#        ('JAN', _('January')),
#        ('FEB', _('February')),
#        ('MAR', _('March')),
#    )
#    # [..]
#    month = models.CharField(
#        max_length=3,
#        choices=MONTH,
#        default=MONTH.JAN,
#    )




# The cleanest solution is to use the django-model-utils library:



# class Article(models.Model):
#     STATUS = Choices('draft', 'published')
#     status = models.CharField(choices=STATUS, default=STATUS.draft, max_length=20)

# from django.db import models

# class MyModel(models.Model):
#     class Month(models.TextChoices):
#         JAN = '1', "JANUARY"
#         FEB = '2', "FEBRUARY"
#         MAR = '3', "MAR"
#         # (...)

#     month = models.CharField(
#         max_length=2,
#         choices=Month.choices,
#         default=Month.JAN
#     )



class ChildDetails(models.Model):
    """Child Immunization details"""
    title = models.CharField(max_length=100, blank=False, null=True)
    DICTRICT = [
    (1, _("Not relevant")),
    (2, _("Review")),
    (3, _("Maybe relevant")),
    (4, _("Relevant")),
    (5, _("Leading candidate"))
    ]
    child_id = models.AutoField(unique_for_year=True, primary_key=True, blank=False, null=False)
    child_district = models.CharField(choices=DICTRICT, default=1, blank=False, null=True, max_length=50)
    health_facility = models.CharField(choices=DICTRICT, default=1, blank=False, null=True, max_length=50)
    child_name = models.CharField(max_length=100, blank=False, null=True)

    CHOICES = [
        ('M','Male'),
        ('F','Female')
    ]
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    dob = models.DateField(blank=False, null=True)
    
    birth_order = models.IntegerField( blank=False, null=True)
    birth_weight = models.IntegerField( blank=False, null=True)
    sub_county = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    parish = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    lc1 = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    special_care = models.CharField(choices=DICTRICT, default=1, blank=True, null=True, max_length=50)
    other_special_care = models.TextField(max_length=100, blank=True, null=True)

    # class meta
    class Meta:
        pass

    def __str__(self) -> str:
        return super().__str__()

    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        pass

class ParentDetails(models.Model):
    """ Mother of the child """
    # mother's details
    title = models.CharField(max_length=100, blank=False, null=True)
    mother_id = models.CharField(max_length=100, blank=False, null=True)
    mother_name = models.CharField(max_length=100, blank=False, null=True)
    mother_occupation = models.CharField(max_length=50, blank=False, null=True)
    mother_education = models.CharField(max_length=50, blank=False, null=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    # father's details
    father_id = models.CharField(max_length=100, blank=False, null=True)
    father_name = models.CharField(max_length=100, blank=False, null=True)
    father_occupation = models.CharField(max_length=50, blank=False, null=True)
    father_education = models.CharField(max_length=50, blank=False, null=True)
    father_phone = models.    phone = PhoneNumberField(null=False, blank=False, unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    #  child's details
    child_id = models.ForeignKey(ChildDetails, on_delete=models.CASCADE, blank=False, null=True)

    
class Immunization(models.Model):
    # Seven Killer Immunizable diseases
    title = models.CharField(max_length=100, blank=False, null=True)
    time_period = models.CharField(max_length=100, blank=False, null=True)
    where_to_give = models.CharField(max_length=100, blank=False, null=True)
    how_to_give = models.CharField(max_length=100, blank=False, null=True)
    vaccine_date = models.DateField(blank=False, null=True)
    vaccine_name = models.CharField(max_length=100, blank=False, null=True)
    vaccine_comments = models.TextField(max_length=100, blank=False, null=True)
    child_id = models.ForeignKey(ChildDetails, on_delete=models.CASCADE, null=True, blank=False)

    # class meta
    class Meta:
        pass

    def __str__(self) -> str:
        return super().__str__()
    
    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        pass

class VitaminAndDeworming(models.Model):
    # Vitamin A
    title = models.CharField(max_length=100, blank=False, null=True)
    vitamin_a_date = models.DateField(blank=False, null=True)
    vitamin_name = models.CharField(max_length=100, blank=False, null=True)
    vitamin_a_comments = models.TextField(max_length=100, blank=False, null=True)
    
    # Deworming
    deworming_date = models.DateField(blank=False, null=True)
    deworming_status = models.CharField(max_length=100, blank=False, null=True)
    deworming_comments = models.TextField(max_length=100, blank=False, null=True)
    given_at_age = models.CharField(max_length=100, blank=False, null=True)
    child_id = models.ForeignKey(ChildDetails, on_delete=models.CASCADE, blank=False, null=True)

    # class meta
    class Meta:
        pass

    def __str__(self) -> str:
        return super().__str__()
    
    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        pass


class EducationAndCounselling(models.Model):
    # Education
    title = models.CharField(max_length=100, blank=False, null=True)
    education_date = models.DateField(blank=False, null=True)
    next_date = models.DateField(blank=False, null=True)
    education_Info = models.TextField(max_length=100, blank=False, null=True)
    parent_id = models.ForeignKey(ParentDetails, on_delete=models.CASCADE, blank=False, null=True)

    # class meta
    class Meta:
        pass

    def __str__(self) -> str:
        return super().__str__()
    
    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        pass

class InfantGrowth(models.Model):
    #  Infant & Young Child Feeding
    title = models.CharField(max_length=100, blank=False, null=True)
    time = models.CharField(max_length=100, blank=False, null=True)
    CHOICES = [
        (1,'Exclusive Breast Feeding'),
        (2,'Exclusive Replacement Feeding'),
        (3, 'Mixed Feeding'),
        (4, 'Appropriate Complementary Feeding'),
        (5, 'Other, specify'),
        
    ]
    iycf_code = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    child_id = models.ForeignKey(ChildDetails, on_delete=models.CASCADE, blank=False, null=True)
    # class meta
    class Meta:
        pass

    def __str__(self) -> str:
        return super().__str__()
    
    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        pass

class GrowthPromotionChart(models.Model):
    # Groth Promotion Chart
    # birth_weight againt dob
    title = models.CharField(max_length=100, blank=False, null=True)


class Pmtct(models.Model):
    # Mother's PMTCT
    title = models.CharField(max_length=100, blank=False, null=True)
    pmtct_code = models.CharField(max_length=100, blank=False, null=True)
    CHOICES = [
        (1,'Reactive'),
        (2,'Non-Reactive'),
    ]
    result_of_child = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    did_child_initate_treatment = models.BooleanField()
    date_initated = models.DateField(blank=False, null=True)
