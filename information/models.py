from django.db import models

# Create your models here.
class Information (models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone_no = models.IntegerField()
    photo = models.ImageField(upload_to='pictures')
    video = models.FileField(upload_to='pictures')
    COMPUTER = 'CSE'
    ELECTRICAL = 'ECE'
    MECHANICAL = 'ME'
    CIVIL = 'CIVIL'
    ELECTRONICS = 'EEE'
    BRANCH_CHOICE = [
        (COMPUTER ,'computer '),
        (ELECTRICAL ,'electrical '),
        (MECHANICAL ,'mechanical'),
        (CIVIL, 'civil'),
        (ELECTRONICS ,'electronics'),
    ]
    branch_choice = models.CharField(max_length=15, choices=BRANCH_CHOICE, default=None)


    def __str__(self):
        return self.name

