from django.db import models
from django.utils import timezone
from datetime import datetime

class comment_rate(models.Model):
    two_dish_rice_id = models.IntegerField()
    foodie_name_id = models.IntegerField()
    restaurant_name = models.CharField(max_length=200)
    foodie_name = models.CharField(max_length=200)
    list_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateField(blank=True)
    comment = models.TextField(blank=True)
    comment_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    comment_photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    comment_photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    comment_photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    comment_photo5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    comment_photo6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    restaurant_rating = models.IntegerField(blank=True , null=True)
    comment_rating = models.IntegerField(blank=True , null=True)
    
    def __str__(self):
        return self.foodie_name

class CommentRating(models.Model):
    comment = models.ForeignKey(comment_rate, on_delete=models.CASCADE, related_name='ratings')
    rater_id = models.IntegerField()  # 評分者ID
    rater_name = models.CharField(max_length=200)  # 評分者姓名
    rating = models.IntegerField()  # 0-5的評分
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('comment', 'rater_id')  # 確保每個用戶只能對同一評論評分一次
    
    def __str__(self):
        return f"{self.rater_name} rated {self.comment.foodie_name}'s comment: {self.rating}/5"

# Create your models here.
