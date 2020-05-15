from django.db import models
from rest_framework import serializers


# https://next.json-generator.com/
# [
#   {
#     'repeat(50, 10)': {
#       model: 'api.article',
#       pk: '{{index()+1}}',
#       fields:{
#         name: '{{company()}}',
#         description: '{{lorem(1, "paragraphs")}}',
#         picture: '',
#         price: '{{integer(4, 15)}}',
#         in_stock: '{{bool()}}',        
#       },
#     }
#   }
# ]

class Article(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    picture = models.ImageField()
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0.00)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
