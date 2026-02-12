from django.contrib import admin  # <--- Pastikan import ini ada
from django.urls import path
from inventory import views

urlpatterns = [
    # PASTIKAN BARIS INI ADA (Django Admin)
    path('admin/', admin.site.urls),

    # --- DASHBOARD ---
    path('', views.dashboard, name='dashboard'),

    # --- SPAREPART ---
    path('spareparts/', views.sparepart_list, name='sparepart_list'),
    path('spareparts/edit/<int:pk>/', views.sparepart_edit, name='sparepart_edit'),
    path('spareparts/delete/<int:pk>/', views.sparepart_delete, name='sparepart_delete'),

    # --- MESIN ---
    path('machines/', views.machine_list, name='machine_list'),

    # --- JADWAL PREVENTIVE ---
    path('jadwal/', views.jadwal_list, name='jadwal_list'),
    path('jadwal/kalender/', views.jadwal_kalender, name='jadwal_kalender'),
    path('jadwal/kalender-tahunan/', views.jadwal_kalender_tahunan, name='jadwal_kalender_tahunan'),
    path('jadwal/tambah/', views.tambah_jadwal, name='tambah_jadwal'),
    path('jadwal/edit/<int:pk>/', views.jadwal_edit, name='jadwal_edit'),
    path('jadwal/hapus/<int:pk>/', views.jadwal_delete, name='jadwal_delete'),

    # --- EXPORT ---
    path('export-excel/', views.export_excel, name='export_excel'),

    # EXPORT EXEL:
path('export-excel-tahunan/', views.export_excel_tahunan, name='export_excel_tahunan'),
]