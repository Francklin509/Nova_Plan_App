from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterSubscriber


# Create your views here.

# View to handle newsletter signup
# This view will handle the form submission for newsletter signup
# It will create a new subscriber if the email is not already subscribed
# If the email is already subscribed, it will inform the user
# If the request method is GET, it will render the signup form template
# If the request method is POST, it will process the form submission
# and redirect the user to a success page or back to the form with a message
# This view is typically used in a Django application to allow users to subscribe to a newsletter
def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            else:
                messages.info(request, 'You are already subscribed to our newsletter.')
        else:
            messages.error(request, 'Please enter a valid email address.')
        return redirect('homepage')  # Redirect to the homepage or any other page
    return render(request, 'newsletter/signup.html')  # Render the signup form template

