from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.urls import reverse



class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=255,blank=True)
    cat_image=models.ImageField(upload_to="photos/category")

    class Meta:
        verbose_name="category"
        verbose_name_plural="categories"

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name


class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError("User must have an email address")

        elif not username:
            raise ValueError("User must have an username")

        user=self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,password,email,username):
        user=self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
        )

        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    phone=models.CharField(max_length=50)

    #required
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','username']

    object=MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True

class Product(models.Model):
    product_name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=1000,blank=True)
    price=models.IntegerField()
    stock=models.IntegerField()
    images=models.ImageField(upload_to="photos/products")
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
