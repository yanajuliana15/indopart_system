
INSTRUKSI MENJALANKAN PROYEK:
==============================
1. Buka Terminal/CMD.
2. Masuk ke folder ini: cd IndoPart_System
3. Install Django & Pillow: pip install django pillow
4. Buat Project Django (Jalankan perintah ini DI LUAR folder IndoPart_System):
   django-admin startproject mysite .
5. Ganti nama folder yang dibuat otomatis:
   rename mysite IndoPart_System
6. Pindahkan file 'urls_project_temp.py' ke dalam folder IndoPart_System (satu level dengan settings.py) dan rename jadi 'urls.py'.
7. Edit 'settings.py', tambahkan 'inventory' ke INSTALLED_APPS dan bagian MEDIA (lihat README).
8. Jalankan: python manage.py makemigrations
9. Jalankan: python manage.py migrate
10. Buat superuser: python manage.py createsuperuser
11. Jalankan server: python manage.py runserver
12. Buka browser: http://127.0.0.1:8000
