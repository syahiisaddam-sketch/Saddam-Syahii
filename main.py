from pypresence import Presence
import time

CLIENT_ID = "ايدي البوت حقك"
USERNAME = "اكتب اسمك"
PROJECT = "My Awesome Project"#تقدر تكتب لي تحب

rpc = Presence(ايدي البوت حقك)
rpc.connect()

start_time = time.time()

rpc.update(
    #خليها كيف ماهيا عشان ماتجيك خطاء
    details=f"👤 {USERNAME}",
    state=f"🚀 يعمل على {PROJECT}",
    start=start_time,
    #صورة كبيرة
    large_image="https://cdn3.emoji.gg/emojis/3773-active-developer-badge-animated.gif",   
    large_text="🔥 Project in Progress",
    #صورة مصغرة
    small_image="https://cdn3.emoji.gg/emojis/64252-pepediscordmod.png",
    small_text="💻 Coding Time",
    buttons=[
        {"label": " GitHub", "url": "حط رابط حقك "},
        {"label": " Website", "url": "انستجرام او اي شي"}
    ]
)

print("السكريبت شغال 100%")
while True:
    time.sleep(5)  #تقدر تختر وقت التحديث 


