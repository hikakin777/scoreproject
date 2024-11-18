from django.db import models
 
class Category(models.Model):#追加
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )
 
    def __str__(self):
        return self.title
class Condition(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Day(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

 

 

class ShopPost(models.Model):
    title = models.CharField(
        verbose_name='名前',
        max_length=200
    )
 
    category = models.ForeignKey(
        Category,
        verbose_name='性別',
        on_delete=models.PROTECT
    )

    condition = models.ForeignKey(
        Condition, 
        on_delete=models.CASCADE, 
        null=True, blank=True
        )  
    
    day = models.CharField(
        verbose_name='教科',
        max_length=10, default=" ")
    

    
    price = models.CharField(
        verbose_name='点数',
        max_length=10, default=" ")
    
    
    
 
    
 
    
    
 
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
 
    def __str__(self):
        return self.title
   
