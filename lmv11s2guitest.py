import os
import pickle
import tkinter as tk
from tkinter import messagebox, simpledialog

# DEĞİŞKENLER VE LİSTELER

liste = []
liste_counter = 1
root = tk.Tk()

# FONKSİYONLAR

class functions:
    def Check():
        return messagebox.askyesno("Onay", "Bu işlemi gerçekleştirmek istediğinize emin misiniz?")

    def ProgramErrorLog(message):
        with open("program_error_logs.txt", "a") as log_file:
            log_file.write(f"{message}\n")

    def ErrorLog(message):
        with open("error_logs.txt", "a") as log_file:
            log_file.write(f"{message}\n")

    def save(liste_name="liste"):
        try:
            with open(f"{liste_name}.pkl", "wb") as file:
                pickle.dump(liste, file)
        except:
            errors.SavingListError()

    def load(liste_name="liste"):
        global liste
        try:
            with open(f"{liste_name}.pkl", "rb") as file:
                liste = pickle.load(file)
        except FileNotFoundError as e:
            functions.ProgramErrorLog(f"FileNotFoundError: {str(e)}")
            errors.LoadingListError()
            liste = []
        except EOFError as e:
            functions.ProgramErrorLog(f"EOFError: {str(e)}")
            errors.LoadingListError()
            liste = []
        except Exception as e:
            functions.ProgramErrorLog(f"Unknown error: {str(e)}")
            errors.LoadingListError()
            liste = []

    def save_counter():
        with open("counter.pkl", "wb") as file:
            pickle.dump(liste_counter, file)

    def load_counter():
        global liste_counter
        try:
            with open("counter.pkl", "rb") as file:
                liste_counter = pickle.load(file)
        except FileNotFoundError as e:
            functions.ProgramErrorLog(f"FileNotFoundError: {str(e)}")
            liste_counter = 1
        except EOFError as e:
            functions.ProgramErrorLog(f"EOFError: {str(e)}")
            liste_counter = 1
        except Exception as e:
            functions.ProgramErrorLog(f"Unknown error: {str(e)}")
            errors.LoadingCounterError()
            liste_counter = 1

    def autosave(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            functions.save(f"liste{liste_counter}")
            return result
        return wrapper

    def autosave_counter(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            functions.save_counter()
            return result
        return wrapper

    def clear():
        pass

    def exporting():
        return "\n".join(liste)

    def helping():
        help_text = """
Ekle: Yazıldıktan sonra istenen kısma yazılanı listeye ekler.
Sil: Yazıldıktan sonra istenen kısma yazılan listede bulunuyorsa siler.
Listele: Listede bulunan tüm elemanları listeler.
Temizle: Listede bulunan tüm elemanları siler.
Sırala: Listede bulunan tüm elemanları sıralar.
Yeni: Yeni bir liste oluşturur.
Versiyon: Programın versiyonu hakkında bilgi verir.
Listeler: Oluşturulan listeleri listeler.
Dışa aktar: Listeyi dışa aktarır.
Yardım: Bu menüyü gösterir.
Çıkış: Programı sonlandırır ve listeyi kaydeder.
Küçük bir not: 10.0 versiyonundan itibaren eski sürümlerde kaydedilmiş listeleri yükleyemezsiniz. Çünkü eski kaydetme sisteminde şu şekilde kaydediliyordu: liste.pkl. Yeni kaydetme sisteminde ise şu şekilde kaydediliyor: liste1.pkl, liste2.pkl, liste3.pkl... gibi.
        """
        messagebox.showinfo("Yardım", help_text)

    def reset():
        main()

    def show_code():
        with open(__file__, "r", encoding="utf-8") as file: 
            code = file.read()
        code_window = tk.Toplevel()
        code_window.title("Kod")
        text = tk.Text(code_window)
        text.insert(tk.END, code)
        text.pack()

    def about_version():
        with open(__file__, "r", encoding="utf-8") as file:
            lns = len(file.readlines())
        version_info = f"""
Versiyon = 11s2
Yenilikler:
- 2 yeni hata eklendi.
Mutlu Edici Özellikler:
Kod 384 satırdan {lns} satıra yükseldi!

İyi Kullanımlar!
        """
        messagebox.showinfo("Versiyon", version_info)

    def exiting():
        functions.save(f"liste{liste_counter}")
        functions.save_counter()
        root.destroy()

# İŞLEM FONKSİYONLARI

@functions.autosave
def add():
    eleman = simpledialog.askstring("Ekle", "Eklenecek eleman:")
    if eleman:
        if eleman in liste:
            errors.AlreadyExistsError()
        else:
            liste.append(eleman)
            messagebox.showinfo("Başarılı", "Ekleme işlemi başarılı!")
    else:
        errors.EmptyInputError()

@functions.autosave
def delete():
    if liste:
        eleman = simpledialog.askstring("Sil", "Silinecek eleman:")
        if eleman:
            if eleman in liste:
                liste.remove(eleman)
                messagebox.showinfo("Başarılı", "Silme işlemi başarılı!")
            else:
                errors.ItemIsNotOnListError()
        else:
            errors.EmptyInputError()
    else:
        errors.EmptyListError()

def show():
    if liste:
        show_window = tk.Toplevel()
        show_window.title("Liste")
        for sayi, eleman in enumerate(liste, start=1):
            tk.Label(show_window, text=f"{sayi}. {eleman}").pack()
    else:
        errors.EmptyListError()

@functions.autosave
def clean():
    if liste:
        if functions.Check():
            liste.clear()
            messagebox.showinfo("Başarılı", "Liste başarıyla temizlendi!")
    else:
        errors.EmptyListError()

def sort(item):
    return item

@functions.autosave
def sort_list():
    if liste:
        if functions.Check():
            liste.sort(key=sort)
            messagebox.showinfo("Başarılı", "Liste başarıyla sıralandı!")
    else:
        errors.EmptyListError()

@functions.autosave_counter
def new_list():
    global liste, liste_counter
    functions.save(f"liste{liste_counter}")
    liste_counter += 1
    liste = []
    messagebox.showinfo("Yeni Liste", f"Yeni liste oluşturuldu: liste{liste_counter}")
    functions.save(f"liste{liste_counter}")

def show_lists():
    if liste_counter > 1:
        lists_window = tk.Toplevel()
        lists_window.title("Listeler")
        for i in range(1, liste_counter):
            tk.Label(lists_window, text=f"liste{i}").pack()
    else:
        errors.NoListsError()

def export():
    try:
        with open(f"liste{liste_counter}.txt", "w") as list_file:
            list_file.write(functions.exporting())
        messagebox.showinfo("Başarılı", f"Liste, liste{liste_counter}.txt adıyla dışa aktarıldı!")
    except:
        errors.ExportingError()

# HATALAR VE UYARILAR

class errors:
    def EmptyListError():
        messagebox.showerror("Hata", "Listede eleman bulunmuyor!")

    def AlreadyExistsError():
        messagebox.showerror("Hata", "Eleman listede zaten bulunuyor!")

    def EmptyInputError():
        messagebox.showerror("Hata", "Lütfen bir şey yazınız!")

    def ItemIsNotOnListError():
        messagebox.showerror("Hata", "Eleman listede bulunmuyor!")

    def LoadingListError():
        messagebox.showerror("Hata", "Liste yükleme başarısız oldu!")

    def InvalidInputError():
        messagebox.showerror("Hata", "Lütfen geçerli bir komut giriniz!")

    def NoListsError():
        messagebox.showerror("Hata", "Yeni bir liste oluşturmadınız!")

    def LoadingCounterError():
        messagebox.showerror("Hata", "Sayaç yükleme başarısız oldu!")

    def ExitingError():
        messagebox.showerror("Hata", "Programdan çıkılırken bir hata oluştu!")

    def SavingListError():
        messagebox.showerror("Hata", "Liste kaydetme başarısız oldu!")

    def SavingCounterError():
        messagebox.showerror("Hata", "Sayaç kaydetme başarısız oldu!")

    def AutosavingError():
        messagebox.showerror("Hata", "Otomatik kaydetme başarısız oldu!")

    def AutosavingCounterError():
        messagebox.showerror("Hata", "Otomatik sayaç kaydetme başarısız oldu!")

    def ExportingError():
        messagebox.showerror("Hata", "Dışa aktarma başarısız oldu!")

    def ResettingError():
        messagebox.showerror("Hata", "Sıfırlama başarısız oldu!")

    def ShowingCodeError():
        messagebox.showerror("Hata", "Kod gösterme başarısız oldu!")

    def TooManyErrors():
        messagebox.showerror("Hata", "Çok fazla hata oluştu!")

    def CodeError():
        messagebox.showerror("Hata", "Program kodunda bir hata oluştu!")

    def UnknownError():
        messagebox.showerror("Hata", "Bilinmeyen bir hata oluştu!")

# HATA KONTROLÜ

def error_control(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            functions.ProgramErrorLog(f"Error: {str(e)}")
            errors.UnknownError()
    return wrapper

# PROGRAM

@error_control
def main():
    functions.load_counter()
    functions.load(f"liste{liste_counter}")

    root = tk.Tk()
    root.title("Liste Yöneticisi")

    tk.Button(root, text="Ekle", command=add).pack()
    tk.Button(root, text="Sil", command=delete).pack()
    tk.Button(root, text="Listele", command=show).pack()
    tk.Button(root, text="Temizle", command=clean).pack()
    tk.Button(root, text="Sırala", command=sort_list).pack()
    tk.Button(root, text="Yeni", command=new_list).pack()
    tk.Button(root, text="Listeler", command=show_lists).pack()
    tk.Button(root, text="Dışa aktar", command=export).pack()
    tk.Button(root, text="Yardım", command=functions.helping).pack()
    tk.Button(root, text="Çıkış", command=functions.exiting).pack()

    root.mainloop()

# PROGRAMI ÇALIŞTIRMA

if __name__ == "__main__":
    main()
