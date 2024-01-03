# multiple_languages_project

for multipling your django project langage you should:




	first:
		after creating your project and apps
		create locale directory in every apps
		and directory that you wants to translate
		
	second:
		from django.utils.translation import gettext as _
		then put every text that you want to translate in
		this function _("text")
	
	third:
		add :
			LOCALE_PATHS = (
    			    os.path.join(os.path.dirname(__file__), "locale"),
			)
		in your project settings.py
		and run this command:
 			python manage.py makemessages --ignore="static" --ignore=".env"  -l [language]
	
	fourth:
		now you can see django.po in every locale directory
		in django.po are your texts ready to translate

	fifth:
		add this middleware to setting.py middlewares:
			multiple_languages/core/middleware.py
		to work when you change the accept-language in http header
	
	sixth:
		run this command:
			python3 manage.py compilemessages
		then it's done

note: install the gettext in your system	
