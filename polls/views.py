from django.http import HttpResponse


def index(request):
	# return HttpResponse("Hello, world. You're at the polls index.")
	return HttpResponse('<h1>The Poll Home</h1>'
						'<p1>Everybody is identical in their secret unspoken belief that way deep down they are different from everyone else.</p1>')


def about(request):
	return HttpResponse('<div>'
						'<h1>ABOUT US</h1>'
						'<h3>'
						'Ade.com is a website just W3 schools We are just like W3 schools <br>'
						'We basically provide examples and prototypes for people who do not have full idea of HTML and CSS<br>'
						'We provide introductory examples to learn, such that you can use the Inspect element option to view the source code which is basic'
						'</h3>'
						'</div>')  # Create your views here.


def contact(request):
	return HttpResponse('<h1>CONTACT</h1>'
						'<h3>'
						'<address>'
						'Written by: DAMADE&#8482 <br>'
						'Contact us at: 2, Community Road, Akoka, Yaba <br>'
						'E-mail: damilolaadeoye545@gmail.com, damilolaadeoye545@yahoo.com <br>'
						'Mobile number: +2348100379555'
						'</address></h3>')
