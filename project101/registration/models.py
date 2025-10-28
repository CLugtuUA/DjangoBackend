from django.db import models
from django.core.exceptions import ValidationError

class SignUpRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_registered = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=12, default="")

    def clean(self):
        """
        Custom validation to ensure passwords match and required fields are not empty.
        """
        # Ensure all fields are filled
        required_fields = ['first_name', 'last_name', 'email', 'username', 'password', 'confirm_password', 'date_of_birth']
        for field in required_fields:
            if not getattr(self, field):
                raise ValidationError(f"The {field.replace('_', ' ')} field is required.")

        # Ensure passwords match
        if self.password != self.confirm_password:
            raise ValidationError("Passwords do not match.")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Sign Up Registration"
        verbose_name_plural = "Sign Up Registrations"