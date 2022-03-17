# Static Files

1. django.contrib.staticfiles가 INSTALLED_APPS에 포함되어 있는지 확인

2. settings.py

   https://docs.djangoproject.com/en/3.2/ref/settings/#static-files

   ```python
   STATICFILES_DIRS = [
       BASE_DIR / 'static',
   ]
   
   STATIC_URL = '/static/'
   
   STATIC_ROOT = BASE_DIR / 'staticfiles'
   ```

3. 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL을 빌드

   ```django
   {% load static %}
   
   <img src="{% static 'my_app/example.jpg'%}" alt="My image">
   ```

4. 앱의 static 디렉토리에 정적 파일을 저장

   ````
   my_app/static/my_app/example.jpg
   ````