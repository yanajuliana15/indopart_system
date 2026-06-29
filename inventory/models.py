from django.db import models

# --- HAPUS BARIS INI ---
# from django.shortcuts import render, redirect, get_object_or_404

class Machine(models.Model):
    code = models.CharField(max_length=100, blank=True, default='') 
    name = models.CharField(max_length=255, blank=True, unique=True,default='')
    image = models.ImageField(upload_to='machine_images/', blank=True, null=True, verbose_name="Foto Mesin")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Sparepart(models.Model):
    CATEGORY_CHOICES = [
        ('Elektrikal', 'Elektrikal'),
        ('Mekanikal', 'Mekanikal'),
        ('Hidrolik', 'Hidrolik'),
        ('Pneumatik', 'Pneumatik'),
        ('Konsumabel', 'Konsumabel'),
    ]
    
    image = models.ImageField(upload_to='sparepart_images/', blank=True, null=True, verbose_name="Foto Sparepart")
    code = models.CharField(max_length=50, verbose_name="Kode Barang")
    name = models.CharField(max_length=200, verbose_name="Nama Sparepart")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Kategori")
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="Mesin")
    stock = models.IntegerField(default=0, verbose_name="Stok Saat Ini")
    min_stock = models.IntegerField(default=1, verbose_name="Min. Stok (Peringatan)")
    lokasi_drawing = models.CharField(max_length=255, blank=True, default='', verbose_name="Lokasi Drawing")
    lokasi_penyimpanan = models.CharField(max_length=100, blank=True, default='', verbose_name="Lokasi Penyimpanan")
    created_at = models.DateTimeField(auto_now_add=True)

    def is_low_stock(self):
        return self.stock <= self.min_stock

    def __str__(self):
        return self.name

class JadwalPreventive(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Selesai', 'Selesai'),
    ]
    JENIS_CHOICES = [
        ('External', 'External'),
        ('MTC', 'MTC'),
    ]
    
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="Mesin")
    tgl_jadwal = models.DateField(verbose_name="Tanggal Jadwal")
    keterangan = models.TextField(verbose_name="Keterangan Pekerjaan")
    jenis_maintenance = models.CharField(max_length=20, choices=JENIS_CHOICES, default='Internal', verbose_name="Jenis Maintenance")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', verbose_name="Status")
    teknisi = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nama Teknisi")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.machine.name} - {self.tgl_jadwal}"

# --- MODEL BARU: BREAKDOWN ---
class Breakdown(models.Model):
    JENIS_TROUBLE_CHOICES = [
        ('Mekanikal', 'Mekanikal'),
        ('Elektrikal', 'Elektrikal'),
        ('Hidrolik', 'Hidrolik'),
        ('Pneumatik', 'Pneumatik'),
        ('Operasional', 'Operasional'),
        ('Lainnya', 'Lainnya'),
    ]

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="Nama Mesin")
    tanggal = models.DateField(verbose_name="Tanggal Perbaikan")
    waktu_pengerjaan = models.CharField(max_length=100, verbose_name="Waktu Pengerjaan", help_text="Contoh: 2 Jam")
    kerusakan = models.CharField(max_length=255, null=True, blank=True)
    
    # --- PERBAIKAN: Hanya satu definisi foto. Saya pilih 'breakdown_images/' agar konsisten dengan Machine & Sparepart ---
    foto = models.ImageField(upload_to='media/breakdown_images/', blank=True, null=True)
    
    penyebab = models.TextField(verbose_name="Penyebab")
    tindakan = models.TextField(verbose_name="Tindakan Perbaikan")
    jenis_trouble = models.CharField(max_length=50, choices=JENIS_TROUBLE_CHOICES, verbose_name="Jenis Trouble")
    sparepart = models.ForeignKey(Sparepart, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Sparepart yang Dipakai")
    pic = models.CharField(max_length=100, verbose_name="Nama PIC (Teknisi)")
    created_at = models.DateTimeField(auto_now_add=True)

    # --- HAPUS BARIS foto yang kedua di sini ---

    def __str__(self):
        # Perbaikan spasi agar tidak nempel: ") -" menjadi ") - "
        return f"{self.machine.name} - {self.tanggal} ({self.jenis_trouble}) - {self.kerusakan}"


class MemberMTC(models.Model):
    nik = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='member_mtc/', blank=True, null=True)

    class Meta:
        ordering = ['nama']
        verbose_name = "Member Maintenance"
        verbose_name_plural = "Member Maintenance"

    def __str__(self):
        return f"{self.nik} - {self.nama}"

class Kaizen(models.Model):

    KATEGORI = [
        ('Safety', 'Safety'),
        ('Quality', 'Quality'),
        ('Cost', 'Cost'),
        ('Delivery', 'Delivery'),
        ('Productivity', 'Productivity'),
        ('Environment', 'Environment'),
    ]

    STATUS = [
        ('Open', 'Open'),
        ('Progress', 'Progress'),
        ('Finish', 'Finish'),
    ]

    tanggal = models.DateField()

    mesin = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE
    )

    tema = models.CharField(
        max_length=200
    )

    kategori = models.CharField(
        max_length=30,
        choices=KATEGORI
    )

    kondisi = models.TextField()

    rencana = models.TextField()

    pic = models.ForeignKey(
        MemberMTC,
        on_delete=models.SET_NULL,
        null=True
    )

    target_selesai = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Open'
    )

    foto_before = models.ImageField(
        upload_to='kaizen/before/',
        blank=True,
        null=True
    )

    foto_after = models.ImageField(
        upload_to='kaizen/after/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.tema