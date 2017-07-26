from __future__ import unicode_literals
from ..login_app.models import User

from django.db import models, IntegrityError

# Create your models here.
class WishManager(models.Manager):
	def createWish(self, postData):
		results  = {'status': True, 'errors': [], 'wish': None}
		if len(postData['name']) < 2:
			results['status'] = False
			results['errors'].append('Item has too few characters...')
		if len(postData['description']) < 8:
			results['status'] = False
			results['errors'].append('Be a little more descriptive...')

		if results['status'] == True:
			print postData['user_id'], '**********'
			userInt = int(postData['user_id'])
			user = User.objects.get(id = userInt)
			results['wish'] = Wish.objects.create(name = postData['name'], description = postData['description'], owner = user)
		return results
    # 
    # def joinWish(self, wish_id, user_id):
    #     results = {'status': True, 'errors' : []}
    #     try:
    #         wish = Wish.objects.get(id=wish_id)
    #         wish.joined.add(user_id)
    #     except IntegrityError as e:
    #         results['status'] = False
    #         results['errors'].append(e.message)
    #
    #     return results



class Wish(models.Model):
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 50)
	owner= models.ForeignKey(User , default= None)

	objects = WishManager()
