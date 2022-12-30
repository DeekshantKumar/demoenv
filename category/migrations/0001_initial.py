from django.db import migrations, models

class Migration (migrations.Migration) :
    initial =True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name= 'Category',
            fields= [
                ('id' , models.AutoField(auto_created = True, primary_key =True, Serialize = False, verbose_name ='ID' ) ),
                ('category_name', models.CharField(max_length=50, unique = True)),
                ('slug' , models.CharField (max_length=100, unique=True)),
                ('description' ,  models.TextField(max_length=255, blank= True))
                ('cat_image' , models.ImageField (upload_to= 'photos/category/', blank =True) )


            ],
        ),
    ]
