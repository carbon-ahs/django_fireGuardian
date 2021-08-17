from django.db import models
'''
class newTableName(models.Model):
    clmn_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.clmn_name
'''
class officeDetail(models.Model):
    industrial = 'in'
    residential = 'rs'
    commercial = 'cm'
    office_type_choices = [
        (commercial, 'Commercial'),
        (industrial, 'Industrial'),
        (residential, 'Residential'),
    ]
    office_size = models.IntegerField()
    office_type = models.CharField(max_length=2, choices=office_type_choices)
    present_fire_extinguisher_number = models.IntegerField(default=0)
    present_smoke_detector_number = models.IntegerField(default=0)

    def __str__(self):
        return self.office_type + ' ' + str(self.office_size)
