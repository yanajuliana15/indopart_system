
from django import forms
from .models import Machine, Sparepart
from django import forms
from .models import Machine, Sparepart, JadwalPreventive

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['code', 'name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: CNC Milling'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: M-01'}),
        }

class SparepartForm(forms.ModelForm):
    class Meta:
        model = Sparepart
        fields = ['code', 'name', 'category', 'machine', 'stock', 'min_stock', 'lokasi_drawing', 'lokasi_penyimpanan', 'image']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'min_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'lokasi_drawing': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'lokasi_penyimpanan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: Rak A-03'}),
        }
# ... (Form Machine dan Sparepart Anda yang lain) ...

class JadwalForm(forms.ModelForm):
    class Meta:
        model = JadwalPreventive
        fields = ['machine', 'tgl_jadwal', 'keterangan', 'status', 'teknisi']
        widgets = {
            'tgl_jadwal': forms.DateInput(attrs={'type': 'date'}), # Agar muncul kalender di HTML
        }

class JadwalForm(forms.ModelForm):
    class Meta:
        model = JadwalPreventive
        fields = ['machine', 'tgl_jadwal', 'jenis_maintenance', 'keterangan', 'status', 'teknisi'] # <--- Tambah 'jenis_maintenance' di sini
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'tgl_jadwal': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'jenis_maintenance': forms.Select(attrs={'class': 'form-control'}), # <--- Tambah ini
            'keterangan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'teknisi': forms.TextInput(attrs={'class': 'form-control'}),
        }
