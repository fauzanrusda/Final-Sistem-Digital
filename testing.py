# Menampilkan header/judul "SEVEN SEGMENT DISPLAY" dan informasi identitas pengguna
print("\n\033[1;34m∞∞∞∞∞ SEVEN SEGMENT DISPLAY ∞∞∞∞∞\033[0m")
print("\033[1;34mName     : Muhammad Fauzan Rusda\033[0m")
print("\033[1;34mNIM      : D121231035\033[0m")
print("\033[1;34mClass    : B_Informatika\033[0m\n")

# Mendefinisikan beberapa kode ANSI escape sequence untuk warna teks dalam terminal
COLOR_WHITE = "\033[1;37m"
COLOR_BLUE = "\033[1;34m"
COLOR_PURPLE = "\033[1;35m"
COLOR_RESET = "\033[0m"

# segmen: 1 (menyala), 0 (mati)
def Decimal_to_Binary(decimal):
    return bin(decimal)[2:]  # Mengonversi angka desimal ke biner dengan menggunakan fungsi 'bin()'

# Matriks 2D yang merepresentasikan tampilan SevenSegment
def Decimal_to_SevenSegment(decimal):
    segment = [
        [1, 1, 1, 0, 1, 1, 1],  # 0
        [0, 0, 1, 0, 0, 1, 0],  # 1
        [1, 0, 1, 1, 1, 0, 1],  # 2
        [1, 0, 1, 1, 0, 1, 1],  # 3
        [0, 1, 1, 1, 0, 1, 0],  # 4
        [1, 1, 0, 1, 0, 1, 1],  # 5
        [1, 1, 0, 1, 1, 1, 1],  # 6
        [1, 0, 1, 0, 0, 1, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 1, 0, 1, 1]   # 9
    ]
    return segment[decimal]

# Menampilkan/mencetak angka desimal, biner, dan tampilan SevenSegment dengan nama segmen (a, b, c, d, e, f, g) dan nilai setiap segmen (1/0)
def Draw_Table(decimal, binary, seven_segment):
    print(f"\n{COLOR_WHITE}Angka Desimal: {decimal}{COLOR_RESET}")
    print(f"{COLOR_WHITE}Bilangan Biner: {binary}{COLOR_RESET}")
    print(f"{COLOR_WHITE}Seven Segment : {seven_segment}{COLOR_RESET}")

# Menampilkan karakter ASCII untuk Seven-Segment 
def Print_SevenSegment(Segment):
    horizontal = f"{COLOR_BLUE}∞∞∞∞{COLOR_PURPLE}\n"  # Baris
    vertical = f"{COLOR_BLUE}◊ {COLOR_PURPLE}"      # Kolom

    for i in range(len(Segment)):
        if i % 3 == 0 or i == 0:
            if Segment[i] == 1:
                print(horizontal, end="")
            else:
                print()
        else:
            if Segment[i] == 1:
                print(vertical, end="")
            else:
                print("   ", end="")
            if i == 2 or i == 5:
                print()

exit_program = False  # Membuat loop utama untuk meminta input pengguna dan menampilkan karakter ASCII Seven-Segment sesuai dengan angka yang dimasukkan
while not exit_program:
    number = int(input("Masukkan angka (0-9): "))
    if 0 <= number < 10:
        segment = Decimal_to_SevenSegment(number)
        print(f"\n\033[1;35mTampilan seven segment dari {number} :\033[0m\n")
        Print_SevenSegment(segment)
        Draw_Table(number, Decimal_to_Binary(number), segment)
    else:
        exit_program = True
        print("\n\033[1;31mRentang angka (0-9)\033[0m\n")
