# Generated manually

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rater_id', models.IntegerField()),
                ('rater_name', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='comments.comment_rate')),
            ],
            options={
                'unique_together': {('comment', 'rater_id')},
            },
        ),
    ]