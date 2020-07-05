from django.db import models

#  Modals

class Allcourse(models.Model) :
    coursename = models.CharField(max_length=250)
    courseid = models.IntegerField(max_length=10)
    isname = models.CharField(max_length=100)

    def __str__(self):
        return self.coursename

class details(models.Model) :
    course = models.ForeignKey(Allcourse, on_delete=models.CASCADE)
    sp = models.CharField(max_length=500)
    il = models.CharField(max_length=500)

    def __str__(self):
        return self.sp

