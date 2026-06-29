from django.contrib import admin
from django.urls import path
from inventory import views  # App Anda bernama 'inventory'
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Sparepart
    path('sparepart/', views.sparepart_list, name='sparepart_list'),
    path('sparepart/edit/<int:pk>/', views.sparepart_edit, name='sparepart_edit'),
    path('sparepart/delete/<int:pk>/', views.sparepart_delete, name='sparepart_delete'),
    path('export/excel/', views.export_excel, name='export_excel'),

    # Machine
    path('mesin/', views.machine_list, name='machine_list'),
    path('mesin/edit/<int:pk>/', views.machine_edit, name='machine_edit'),
    path('mesin/delete/<int:pk>/', views.machine_delete, name='machine_delete'),

    # Jadwal Preventive
    path('jadwal/', views.jadwal_list, name='jadwal_list'),
    path('jadwal/tambah/', views.tambah_jadwal, name='tambah_jadwal'),
    path('jadwal/edit/<int:pk>/', views.jadwal_edit, name='jadwal_edit'),
    path('jadwal/delete/<int:pk>/', views.jadwal_delete, name='jadwal_delete'),
    path('jadwal/kalender/', views.jadwal_kalender, name='jadwal_kalender'),
    path('jadwal/kalender-tahunan/', views.jadwal_kalender_tahunan, name='jadwal_kalender_tahunan'),
    path('export/excel-tahunan/', views.export_excel_tahunan, name='export_excel_tahunan'),

    # Breakdown
    path('breakdown/', views.breakdown_list, name='breakdown_list'),
    path('breakdown/tambah/', views.tambah_breakdown, name='tambah_breakdown'),
    path('breakdown/edit/<int:pk>/', views.breakdown_edit, name='breakdown_edit'),
    path('breakdown/delete/<int:pk>/', views.breakdown_delete, name='breakdown_delete'),
    path('breakdown/export/', views.export_excel_breakdown, name='export_excel_breakdown'),
    path('member/', views.member_mtc, name='member_mtc'),
    path('member/tambah/', views.tambah_member, name='tambah_member'),
    path('member/edit/<int:pk>/', views.edit_member, name='edit_member'),
    path('member/delete/<int:pk>/', views.delete_member, name='delete_member'),
    path('kaizen/', views.kaizen_list, name='kaizen_list'),
    path('kaizen/tambah/', views.kaizen_create, name='kaizen_create'),
    path('kaizen/', views.kaizen_list, name='kaizen_list'),
    path('kaizen/tambah/', views.kaizen_create, name='kaizen_create'),
    path('kaizen/edit/<int:pk>/', views.kaizen_edit, name='kaizen_edit'),
    path('kaizen/delete/<int:pk>/', views.kaizen_delete, name='kaizen_delete'),
    path('kaizen/detail/<int:pk>/', views.kaizen_detail, name='kaizen_detail'),
    path('admin/', admin.site.urls),
]

# Konfigurasi untuk mengakses file upload (Foto)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)