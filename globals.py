# Konstanta
Nmax = 1000 
Mark = None

# Inisialisasi Matrix 
users = [[Mark for j in range (3)] for i in range (Nmax)]        # Matriks data user
candi = [[Mark for j in range (5)] for i in range (Nmax)]        # Matriks data candi
bahan_bangunan = [[Mark for j in range (3)] for i in range(3)]   # Data bahan bangunan

# Inisialisasi idx kolom 
idx_username = idx_id = idx_nama = 0 
idx_password = idx_pembuat = idx_deskripsi = 1
idx_role = idx_pasir = idx_jumlah = 2
idx_batu = 3
idx_air = 4

# Inisialisasi nilai efektif baris matrix 
users_eff = 0
candi_eff = 0 

# inisialisasi id user
user_id = -1
