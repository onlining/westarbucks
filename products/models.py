from django.db import models
# import simplejson as json
# Create your models here.

class Menu(models.Model):
	name=models.CharField(max_length=45)
	class Meta:
		db_table="menu"
	

class Categories(models.Model):
	menu=models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categories')
	name=models.CharField(max_length=45)

	class Meta:
		db_table="categories"
class Allergy(models.Model):
	name=models.TextField(max_length=45)
	allergyed=models.ManyToManyField("Drinks", through='Allergy_drink')


	class Meta:
		db_table="allergy"

	# def __str__(self):
	# 	return self.name
		
class Drinks(models.Model):
	category=models.ForeignKey(Categories, on_delete=models.CASCADE)
	korean_name=models.CharField(max_length=45)
	english_name=models.CharField(max_length=45)
	description=models.TextField()
	# allergyed=models.ManyToManyField(Allergy, through='Allergy_drink')
	class Meta:
		db_table="drinks"

	# def __str__(self):
	# 	return self.name

class Allergy_drink(models.Model):
	allergy=models.ForeignKey(Allergy, on_delete=models.CASCADE, )
	drinks=models.ForeignKey(Drinks, on_delete=models.CASCADE)

	class Meta:
		db_table="allergy_drink"




class Images(models.Model):
	image_url=models.URLField(max_length=2000)
	drink=models.ForeignKey(Drinks, on_delete=models.CASCADE, related_name='images')
	
	class Meta:
		db_table="images"
class Sizes(models.Model):
	name=models.CharField(max_length=45)
	size_ml=models.CharField(max_length=45,null=True)
	size_fluid_ounce=models.CharField(max_length=45,null=True)
	class Meta:
		db_table="sizes"

class Nutritions(models.Model):
	one_serving_kca= models.DecimalField(max_digits = 10, decimal_places =2,null=True)
	sodium_mg= models.DecimalField(max_digits = 10, decimal_places =2,null=True)
	saturated_fat_g= models.DecimalField(max_digits = 10, decimal_places =2,null=True)
	sugars_g= models.DecimalField(max_digits = 10, decimal_places =2,null=True)
	protein_g= models.DecimalField(max_digits = 10, decimal_places =2,null=True)
	caffeine_mg= models.DecimalField(max_digits = 10, decimal_places =2,null=True)
	drink=models.ForeignKey(Drinks,on_delete=models.CASCADE, related_name="nutritions",null=True)
	size=models.ForeignKey(Sizes, on_delete=models.CASCADE, related_name="nutritions",null=True)
	class Meta:
		db_table="nutritions"
