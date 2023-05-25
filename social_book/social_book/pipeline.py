# pipeline.py

from allauth.account.models import EmailAddress

def update_user_email(request, response, sociallogin):
    """
    Update user email based on the email returned by the social provider
    """
    if sociallogin.account.provider == 'google':
        email = sociallogin.account.extra_data.get('username')
        if email:
            user = sociallogin.user
            user.email = email
            user.save()
            email_address = EmailAddress.objects.get_or_create(
                user=user,
                email=email,
                verified=True
            )
            sociallogin.account.email_address = email_address
