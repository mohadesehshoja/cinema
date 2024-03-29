from django.contrib.auth.models import User
from django.db import models


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="profile")
    mobile= models.CharField("mobile number",max_length=11)
    male=1
    female=2
    gender=models.IntegerField("gender",choices=((male,'male'),(female,'female')),null=True,blank=True)
    birthday=models.DateTimeField("birthday",null=True,blank=True)
    address=models.TextField("address",null=True,blank=True)
    profileimage=models.ImageField("image",upload_to='users/profile_image',null=True,blank=True)
    balance=models.IntegerField("balance",default=0)
    def __str__(self):
        return self.user.get_full_name()

    def deposit(self,amount):
        self.balance+=amount
        self.save()

    def spend(self,amount):
        if self.balance<amount:
            return False
        self.balance-=amount
        self.save()
        return True

class Payment(models.Model):
    myprofile=models.ForeignKey('profile',on_delete=models.CASCADE,verbose_name='your profile')
    amount=models.IntegerField('amount')
    transaction_time=models.DateTimeField('time',auto_now_add=True)
    transaction_id=models.CharField('transaction id',max_length=30)
    def __str__(self):
        return "{} {}".format(self.myprofile,self.amount)

