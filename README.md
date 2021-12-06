# PaymentInterface

[**YouTube Link**](https://youtu.be/dQpf8tcEXsQ)

# Flow Chart

### RAZORPAY API KEY GENERATION

- Sign Up for Razorpay
- Then go to Razorpay Dashboard > Settings
- Then Enable Test mode
- ![](https://github.com/Soham7-dev/Images-and-GIFS/blob/main/Screenshot%20(238).png)
- Then Generate API Key
- ![](https://github.com/Soham7-dev/Images-and-GIFS/blob/main/Screenshot%20(228).png)

### API KEY AUTHENTICATION AND CREATING A RAZORPAY ORDER FROM SERVER SIDE DJANGO

- We Create a Client Instance with api keys that was previously generated by us
- Later we create a Razorpay Client Order in our Server Side Django inside our index method inside views.py
- ![](https://github.com/Soham7-dev/Images-and-GIFS/blob/main/Screenshot%20(240).png)

### HANDLING PAYMENT IN THE SERVER SIDE

- Now we create another method (**Wrapped by @csrf_exempt decorator**) where we verify our **POST** request
- First we verify our **payment signature**
- if it succeeds we render **success.html** otherwise we render **failure.html**
- ![](https://github.com/Soham7-dev/Images-and-GIFS/blob/main/Screenshot%20(241).png)

### HANDLING PAYMENT IN THE CLIENT SIDE

- We have created a simple form where a person submits his name and donates ₹100
- ![](https://github.com/Soham7-dev/Images-and-GIFS/blob/main/Screenshot%20(229).png)
- After Clicking the donation button Razorpay window pops up
- Here the donor gives his/her email address and phone no.
- ![](https://github.com/Soham7-dev/Images-and-GIFS/blob/main/Screenshot%20(230).png)
- Next the donor chooses the method of payment
- ![](https://github.com/Soham7-dev/Images-and-GIFS/blob/main/Screenshot%20(232).png)
- Waits till Loading Page
- ![](https://github.com/Soham7-dev/Images-and-GIFS/blob/main/Screenshot%20(234).png)

### PAYMENT STATUS PAGE

- if the payment succeeds we render **success.html** otherwise we render **failure.html**
- There is a link that Redirects the user to the First Page
- ![](https://github.com/Soham7-dev/Images-and-GIFS/blob/main/Screenshot%20(236).png)

**You Can Check out my [**YouTube Link**](https://youtu.be/dQpf8tcEXsQ) for this Project**
