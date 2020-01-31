from django.db import models

class Doctors(models.Model):
	doctor_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_surname = models.CharField(max_length=50)

class Patients(models.Model):
	pesel = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_surname = models.CharField(max_length=50)

class Conferences(models.Model):
	conference_id = models.AutoField(primary_key=True)
	pesel = models.ForeignKey(Patients, on_delete=models.CASCADE)
	doctor_id = models.ForeignKey(Doctors, on_delete=models.PROTECT)

class TestResults(models.Model):
	result_id = models.AutoField(primary_key=True)
	pesel = models.ForeignKey(Patients, on_delete=models.CASCADE)
	doctor_id = models.ForeignKey(Doctors, on_delete=models.PROTECT)
	result_text = models.TextField()
	result_image = models.BinaryField()
	comment_image = models.BinaryField()
	comment_text = models.TextField()