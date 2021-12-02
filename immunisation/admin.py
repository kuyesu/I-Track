from django.contrib import admin
from .models import ChildDetails, ParentDetails, Immunization, VitaminAndDeworming, EducationAndCounselling, InfantGrowth, GrowthPromotionChart, Pmtct
# Register your models here.
@admin.register(ChildDetails)
class AddChild(admin.ModelAdmin):
    list_display = ('title', 'child_id', 'child_district', 'health_facility', 'child_name', 'gender', 'dob', 'birth_order', 'birth_weight', 'sub_county', 'parish', 'lc1', 'special_care', 'other_special_care')
    list_filter = ('title', 'child_id', 'child_district', 'health_facility', 'child_name',)
    search_fields = ('title', 'child_id', 'child_district', 'health_facility', 'child_name',)
    
    
    
    ordering = ('child_id', 'child_name')
    


@admin.register(ParentDetails)
class AddParent(admin.ModelAdmin):
    list_display = ('title',  'mother_name', 'father_name')
    list_filter = ('title',  'mother_name', 'father_name')
    search_fields = ( 'title',  'mother_name', 'father_name')
    
    
    # date_hierarchy = 'publish'
    

@admin.register(Immunization)
class AddImmunization(admin.ModelAdmin):
    list_display = ('title','vaccine_name',  'time_period')
    list_filter = ('vaccine_name', 'time_period')
    search_fields = ( 'vaccine_name', 'title','time_period')
    
    
    # date_hierarchy = 'vaccine_name'
    

@admin.register(VitaminAndDeworming)
class AddVitaminAndDeworming(admin.ModelAdmin):
    list_display = ('title',  'vitamin_a_date', 'deworming_date', 'deworming_status')
    list_filter = ('vitamin_a_date',  'deworming_date', 'deworming_status')
    search_fields = ( 'vitamin_a_date',  'deworming_date', 'deworming_status')
    
    
    # date_hierarchy = 'vitamin_a_date'
    

@admin.register(EducationAndCounselling)
class AddEducationAndCounselling(admin.ModelAdmin):
    list_display = ('education_date', 'next_date')
    list_filter = ()
    search_fields = ( 'title', 'next_date')
    
    
    # date_hierarchy = 'next_date'
    

@admin.register(InfantGrowth)
class AddInfantGrowth(admin.ModelAdmin):
    list_display = ('time', )
    list_filter = ('time', )
    search_fields = ( 'title', 'time', )
    
    
    # date_hierarchy ='time',
    

@admin.register(GrowthPromotionChart)
class AddGrowthPromotionChart(admin.ModelAdmin):
    pass
@admin.register(Pmtct)
class AddPmtct(admin.ModelAdmin):
    list_display = ('title', 'pmtct_code', )
    list_filter = ('title', 'pmtct_code', )
    search_fields = ( 'title', 'pmtct_code', )

    # date_hierarchy = 'pmtct_code'
    