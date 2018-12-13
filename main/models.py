
from django.db import models
from django.contrib.auth.models import User



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#   B O O K S

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_followers(self):
        activities = Activity.objects.filter(to_user__pk=self.pk, activity_type=Activity.FOLLOW)
        followers = []
        for activity in activities:
            followers.append(activity.from_user)
        return followers

    def get_following(self):
        activities = Activity.objects.filter(from_user__pk=self.pk, activity_type=Activity.FOLLOW)
        following = []
        for activity in activities:
            following.append(activity.to_user)
        return following


class Books(models.Model):

    created =           models.DateTimeField(auto_now_add=True, editable=False)
    last_updated =      models.DateTimeField(auto_now=True, editable=False)

    book_title =        models.CharField(max_length=100, unique=True)
    book_total_pages =  models.IntegerField()


    class Meta:
        ordering = ('-created',)
        verbose_name = "Books"
        verbose_name_plural = "Books"

    def __str__(self):
        return '{0}'.format(self.book_title)


class UserBooks(models.Model):

    user =              models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    books =             models.ForeignKey(Books, on_delete=models.CASCADE, null=False, related_name='userbooks')

    class Meta:
        verbose_name = "UserBooks"
        verbose_name_plural = "UserBooks"

    def __str__(self):
        return '{0}'.format(self.books.book_title)

class LogPages(models.Model):

    user =              models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    # book_title =        models.ForeignKey(Books, on_delete=models.CASCADE, null=False, blank=False)
    userbooks =             models.ForeignKey(UserBooks, on_delete=models.CASCADE, null=True, related_name='logbooks')
    log_date =          models.DateTimeField()
    log_pages =         models.FloatField()

    class Meta:
        verbose_name = "LogPages"
        verbose_name_plural = "LogPages"






class Activity(models.Model):
    FOLLOW = 'F'
    ACTIVITY_TYPES = (
        (FOLLOW, 'Follow'),
    )

    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+", null=True)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

    def __unicode__(self):
        return self.activity_type
