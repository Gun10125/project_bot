# นำเข้าโมดูล pytts3 เพื่อให้คอมพิวเตอร์พูดออกมา
# นำเข้าโมดูล speech_recognition เพื่อให้รับข้อความเสียงแล้วแปลงเป็นคำพูด
# นำเข้าโมดูล datetime เพื่อใช้ในการทำงานกับวันที่และเวลา
# ขำเข้าโมดูล os เพื่อกำหนดไฟล์และเส้นทางของไฟล์
# นำเข้าโมดูล wikipedia เพือให้สามารถเข้าถึงข้อมูลจาก Wikipedia และ ใช้ในโปรแกรม
# นำเข้าโมดูล pywahtkit เพื่อให้ทำงานบนเว็บไซต์และการจัดการข้อมูล
# นำเข้าโมดูล pyautogui เพื่อจำลองการคลิกและพิมพ์บนหน้าจอคอมพิวเตอร์
import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui

# สร้างอินสแตนซ์ของ pyttsx3 โดยระบุให้ใช้ SAPI5
# รับรายการเสียงที่พร้อมใช้งานที่มีในระบบ ซึ่งจะถูกเก็บไว้ในตัวแปร voices
# กำหนดเสียงที่จะถูกใช้ในเครื่องพูดเสียง โดยกำหนดให้ใช้เสียงแรกในรายการเสียงที่รับมา ซึ่งเริ่มต้นที่ตำแหน่ง'0'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# สร้างฟังก์ชั่น speak สำหรับเก็บเสียงผ่าน audio
# เพื่อออกเสียงข้อความที่รับเข้ามาผ่านตัวแปร audio
# รันเสียงที่ถูกกำหนด โดยรอจนกว่าเสียงจะถูกออกเสียงเสร็จสิ้น ซึ่งการใช้ runAndWait() ทำให้โปรแกรมรอจนกว่าข้อความจะถูกออกเสียงเสร็จสิ้นก่อนที่จะทำงานถัดไป
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# สร้างฟังก์ชั่น
# รับค่าช่วงเวลาปัจจุบันโดยใช้ คำสั่ง datetime จากนั้นรอมันคืนค่ามันเป็นตัวเลข
# ตรวจสอบเงื่อนไข หาก 00.00 - 11.59 AM จะพูดและแสดวข้อความ
# ตรวจสอบเงื่อนไข หาก 12.00 - 16.59 PM จะพูดและแสดวข้อความ
# ตรวจสอบเงื่อนไข หาก 17.00 - 20.59 PM จะพูดและแสดวข้อความ
# ตรวจสอบเงื่อนไข หาก 21.00 - 23.59 PM จะพูดและแสดวข้อความ
def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Goog Morning Boss")
        speak("Good Morning Boss ")
    elif hour>=12 and hour<17:
        print("Good Afternoon Boss") 
        speak("Good Afternoon Boss ")
    elif hour>=17 and hour<21:
        print("Good Evening Boss") 
        speak("Good Evening Boss ")
    else:
        print("Good Night Boss")    
        speak("Good Night Boss ")

# สร้างฟังก์ชั่น
# สร้างออบเจ็กต์ Recognizer ของไลบรารี speech_recognition และเก็บในตัวแปร r
# เปิดการใช้งานไมโครโฟนของเครื่องคอมพิวเตอร์และเริ่มการรับเสียงผ่านไมโครโฟนโดยใช้คำสั่ง with และเก็บเสียงที่ได้รับไว้ใน source
# กำหนดระยะเวลาที่ระบบรอในระหว่างคำพูดของผู้ใช้ (1 วินาที)
# ลดเสียงรบกวนโดยค่า duration
# รับเสียงที่มาจากไมโครโฟนและเก็บไว้ใน audio
def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

# สร้าง try เพื่อตรวจจับข้อผิดพลาด
# สร้าง exception จัดการข้อผิดพลาดหากเกิดข้อผิดพลาดในขณะแปลงเสียงเป็นข้อความ
    try:
        print("Wait for Few Moments")
        query=r.recognize_google(audio, language='en-EN')
        print(f"You just said : {query}\n")
    except Exception as e:
        print(e)
        speak("Please Tell me again")
        query="none"
    return query

# สร้างฟังก์ชั่นแต่อันนี้จะใช่เพื่อปลุก'EDIT'
# สร้างออบเจ็กต์ Recognizer ของไลบรารี speech_recognition และเก็บในตัวแปร r
# เปิดการใช้งานไมโครโฟนของเครื่องคอมพิวเตอร์และเริ่มการรับเสียงผ่านไมโครโฟนโดยใช้คำสั่ง with และเก็บเสียงที่ได้รับไว้ใน source
# กำหนดระยะเวลาที่ระบบรอในระหว่างคำพูดของผู้ใช้ (1 วินาที)
# ลดเสียงรบกวนโดยค่า duration
# รับเสียงที่มาจากไมโครโฟนและเก็บไว้ใน audio
def wakeup_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Edit is Sleeping...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

# สร้าง try เพื่อตรวจจับข้อผิดพลาด
# สร้าง exception จัดการข้อผิดพลาดหากเกิดข้อผิดพลาดในขณะแปลงเสียงเป็นข้อความ
    try:
        query=r.recognize_google(audio,language='en=EN')
        print(f"User said : {query}\n")
    except Exception as e:
        query="none"
    return query


# if __name__ == "__main__": ใช้ในการตรวจสอบว่าโปรแกรมถูกเรียกใช้โดยตรง หรือ ไม่
if __name__ == "__main__":
    while True:
        query=wakeup_command().lower()
        if 'wake up' in query:
            wishings()
            speak("What can i do for you!")

            while True:
                query=commands().lower()
                if 'wikipedia' in query:
                    speak("Searching in Wikipedia...")
                    try:
                        query=query.replace("wikipedia","")
                        results = wikipedia.summary(query,sentences=1)
                        speak("According to Wikipedia,")
                        print(results)
                        speak(results)
                    except:
                        print("No results found...")
                        speak("No results found...")

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    print(strTime)
                    speak(f"Sir,the time is {strTime}")

                elif 'open youtube' in query:
                    speak("open youtube")
                    pywhatkit.playonyt(query)

                elif 'open browser' in query:
                    speak("Opening Browser Application...")
                    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                    while True:
                        chromeQuery=commands().lower()
                        if "google search" in chromeQuery:
                            Query=chromeQuery
                            Query=Query.replace("google search","")
                            pyautogui.write(Query)
                            pyautogui.press('enter')
                            speak('Searching...')

                        elif "close chrome" in chromeQuery:
                            pyautogui.hotkey('ctrl','w')
                            speak("Closing Google Chrome...")
                            break

                elif "close the application" in query:
                    speak('Closing...')
                    pyautogui.hotkey('ctrl','w')
                
                elif "screenshot" in query:
                    speak("Print Screen...")
                    pyautogui.press('prtSc')

                elif 'stop' in query:
                    speak("Pause...")
                    break
                elif 'exit program' in query:
                    speak("I'm Sleeping...")
                    quit()