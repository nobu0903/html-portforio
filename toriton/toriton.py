import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import Toplevel, Label, Button

# 寿司の種類
sushi_white = {'玉子握り', 'ハンバーグ', '揚げなす味噌', 'ツナサラダ', 'いかサラダ', 'たこサラダ', 'マヨコーン', '軍艦納豆'}
sushi_blue = {'甘エビ'}
sushi_green = {'本マグロ赤身'}
sushi_orange = {'サーモン'}
sushi_purple = {'うに'}
sushi_red = {'大トロ'}
sushi_gold = {'金目鯛'}

def show_image_messagebox(message, image_path): 
    # 新しいトップレベルのウィンドウを作成
    msg_box = Toplevel()
    msg_box.title("画像付きメッセージ")

    try:
        # 画像を読み込み、表示
        image = Image.open(image_path)
        img = ImageTk.PhotoImage(image)

        # 画像ラベルを作成
        img_label = Label(msg_box, image=img)
        img_label.image = img  # 参照を保持しないと画像が消えてしまう
        img_label.grid(pady=10)

    except Exception as e:
        # 画像が読み込めない場合はエラーメッセージを表示
        error_label = Label(msg_box, text=f"画像を表示できません: {e}")
        error_label.grid(pady=10)

    # テキストラベルを作成
    text_label = Label(msg_box, text=message)
    text_label.grid(pady=10)

    # OKボタンを追加して、ウィンドウを閉じる
    ok_button = Button(msg_box, text="OK", command=msg_box.destroy)
    ok_button.grid(pady=10)

# 寿司の種類に応じた皿の色を判定
def determine_color(player_choice):
    if player_choice in sushi_white:
        return '白'
    elif player_choice in sushi_blue:
        return '青'  
    elif player_choice in sushi_green:
        return '緑'
    elif player_choice in sushi_orange:
        return 'オレンジ'
    elif player_choice in sushi_purple:
        return '紫'
    elif player_choice in sushi_red:
        return '赤'
    elif player_choice in sushi_gold:
        return '金'
    else:
        return '該当なし'
    
def count_dishes(change):
    global counter
    counter += change
    label.config(text=str(counter))


# プレイヤーの選択に応じて色を表示
def player_color():  
    player_choice = entry.get()
    result = determine_color(player_choice)
    messagebox.showinfo(title='結果', message=f'{player_choice}\n{result}')

# ウィンドウの設定
root = tk.Tk()
root.title('皿の色あてマシーン')
root.geometry('1200x800')

# ラベル
label = tk.Label(root, text='寿司の種類')
label.grid(row=0, column=0, pady=10)
label_count = tk.Label(root, text=str(count_dishes), font=("Arial", 24))
label_count.grid(row=0, column=1, pady=20)


# エントリー
entry = tk.Entry(root, width=30)
entry.grid(row=1, column=0, pady=10)

# ボタン
button = tk.Button(root, text='色を判定', command=player_color)
button.grid(row=2, column=0, pady=10)

# 白皿のフレーム　いらない
white_plate = tk.Frame(root, bg="white")
white_plate.grid(row=3, column=0, padx=20, pady=10, sticky='ew')

# 青皿のフレーム　いらない
blue_plate = tk.Frame(root, bg="lightblue")
blue_plate.grid(row=4, column=0, padx=20, pady=10, sticky='ew')

# 緑皿のフレーム 　いらない
green_plate = tk.Frame(root, bg="lightgreen")
green_plate.grid(row=5, column=0, padx=20, pady=10, sticky='ew')

# ボタンを作成してメッセージボックスを表示
button = Button(root, text="玉子握り", 
                 command=lambda: show_image_messagebox("玉子握り", "tamagonigiri.jpg"))
button.grid(row=6, column=0, pady=5, padx=5)

# + ボタン
counter = 0
plus_button = tk.Button(root, text="+", command=lambda: count_dishes(1), font=("Arial", 20))
plus_button.grid(row=1, column=2, padx=20)

# - ボタン
minus_button = tk.Button(root, text="-", command=lambda: count_dishes(-1), font=("Arial", 20))
minus_button.grid(row=1, column=0, padx=20)

button = Button(root, text="ハンバーグ", 
                 command=lambda: show_image_messagebox("ハンバーグ", "hamburg.jpg"))
button.grid(row=7, column=0, pady=5, padx=5)

button = Button(root, text="揚げナス味噌", 
                 command=lambda: show_image_messagebox("揚げナス味噌", "agenasumiso.jpg"))
button.grid(row=8, column=0, pady=5, padx=5)

button = Button(root, text="ツナサラダ", 
                 command=lambda: show_image_messagebox("ツナサラダ", "tunasarada.jpg"))
button.grid(row=6, column=1, pady=5, padx=5, columnspan=3)

