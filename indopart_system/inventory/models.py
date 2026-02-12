from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nama Mesin")
    code = models.CharField(max_length=50, unique=True, verbose_name="Kode Mesin")
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
    # TAMBAHKAN 2 BARIS INI
    lokasi_drawing = models.CharField(max_length=255, blank=True, default='', verbose_name="Lokasi Drawing")
    lokasi_penyimpanan = models.CharField(max_length=100, blank=True, default='', verbose_name="Lokasi Penyimpanan")
    # ------------------------------------------------
    image = models.ImageField(upload_to='sparepart_images/', blank=True, null=True, verbose_name="Foto Sparepart")
    created_at = models.DateTimeField(auto_now_add=True)

def is_low_stock(self):
        return self.stock <= self.min_stock

def __str__(self):
        return self.name

        from django.db import models

# ... (Model Machine dan Sparepart tetap sama) ...

class JadwalPreventive(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Selesai', 'Selesai'),
    ]
    
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="Mesin")
    tgl_jadwal = models.DateField(verbose_name="Tanggal Jadwal")
    keterangan = models.TextField(verbose_name="Keterangan Pekerjaan")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    teknisi = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nama Teknisi")
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.machine.name} - {self.tgl_jadwal}"
class JadwalPreventive(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Selesai', 'Selesai'),
    ]
    # PILIHAN BARU: Internal atau MTC
    JENIS_CHOICES = [
        ('External', 'External'),
        ('MTC', 'MTC'),
    ]
    
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="Mesin")
    tgl_jadwal = models.DateField(verbose_name="Tanggal Jadwal")
    keterangan = models.TextField(verbose_name="Keterangan Pekerjaan")
    
    # TAMBAHKAN 1 BARIS INI
    jenis_maintenance = models.CharField(max_length=20, choices=JENIS_CHOICES, default='Internal', verbose_name="Jenis Maintenance")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', verbose_name="Status")
    teknisi = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nama Teknisi")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.machine.name} - {self.tgl_jadwal}"