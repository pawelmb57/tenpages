
from django.db import models
from django.contrib.auth.models import User



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#   B O O K S

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class BookTitles(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#
#     def __str__(self):
#         return self.name


class Books(models.Model):

    created =           models.DateTimeField(auto_now_add=True, editable=False)
    last_updated =      models.DateTimeField(auto_now=True, editable=False)

    book_title =        models.CharField(max_length=100, unique=True)
    book_total_pages =  models.IntegerField()


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{0}'.format(self.book_title)


class UserBooks(models.Model):

    user =              models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    books =             models.ForeignKey(Books, on_delete=models.CASCADE, null=False, related_name='userbooks')

    def __str__(self):
        return '{0}'.format(self.books.book_title)

class LogPages(models.Model):

    user =              models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    # book_title =        models.ForeignKey(Books, on_delete=models.CASCADE, null=False, blank=False)
    userbooks =             models.ForeignKey(UserBooks, on_delete=models.CASCADE, null=True, related_name='logbooks')
    log_date =          models.DateTimeField(auto_now_add=True, editable=True)
    log_pages =         models.FloatField()
