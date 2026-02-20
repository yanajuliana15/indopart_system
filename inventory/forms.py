from django import forms
from .models import Machine, Sparepart, JadwalPreventive, Breakdown

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['code', 'name', 'image']

        labels = {
            'code': 'Kode Mesin',
            'name': 'Nama Mesin',
            'image': 'Foto Mesin',
        }

        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].required = False
        self.fields['name'].required = False
        self.fields['image'].required = False

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
            'min_stock': forms.NumberInput(attrs={'class': 'form-control'}), # <--- PERBAIKAN DI SINI
            'lokasi_drawing': forms.TextInput(attrs={'class': 'form-control'}),
            'lokasi_penyimpanan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: Rak A-03'}),
        }
class JadwalForm(forms.ModelForm):
    class Meta:
        model = JadwalPreventive
        fields = ['machine', 'tgl_jadwal', 'jenis_maintenance', 'keterangan', 'status', 'teknisi']
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'tgl_jadwal': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'jenis_maintenance': forms.Select(attrs={'class': 'form-control'}),
            'keterangan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'teknisi': forms.TextInput(attrs={'class': 'form-control'}),
        }

# --- FORM BARU: BREAKDOWN (SUDAH DIPERBAIKI) ---
class BreakdownForm(forms.ModelForm):
    class Meta:
        model = Breakdown
        
        # PERBAIKAN 1: Indentasi disesuaikan agar sejajar dengan 'model'
        fields = [
            'machine',
            'tanggal',
            'waktu_pengerjaan',
            'kerusakan',
            'penyebab',
            'tindakan',
            'jenis_trouble',
            'sparepart',
            'pic',
            'foto',
        ]
        
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'tanggal': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'waktu_pengerjaan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: 2 Jam'}),
            'kerusakan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'penyebab': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tindakan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'jenis_trouble': forms.Select(attrs={'class': 'form-control'}),
            'sparepart': forms.Select(attrs={'class': 'form-control'}),
            
            # PERBAIKAN 2: Mengubah TextInput menjadi ClearableFileInput agar tombol upload muncul
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            
            'pic': forms.TextInput(attrs={'class': 'form-control'}),
        }