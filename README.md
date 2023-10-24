# Run the project on your local machine

## Initial configuration

1: Cloning project on your interest directory --> git clone https://github.com/Reza98Sh/BOM-backend.git  
2: Creating virtual enviroment for isolating the pakages that you need to run the project --> virtualenv venv   
3: Activating the virtual enviroment -->
- if you have windows os : source venv/bin/activate
- if you have linux or mac os : . venv/bin/activate  
                                                                      
## Installation

4: Installing packages that you need to run the project from requirement.txt file --> pip install -r requirements.txt       

## Database

5: Creating the datbase based on the excel file in the data directory and initial migrations --> flask db upgrade                                                

## Usage

6: After creating the database you can run the project by the following commands -->                                                                             
- on the localhost --> flask run                                                                                                                              
- on the localhost and local ip address --> flask run --host=0.0.0.0 --port=5000                                                                              
- if you want to see the bugs use the '--debug' at the end of your command (hint : don't use this on production)  

## API

7: The following URL are for API and documentation of the project --> 
- /api/docs : For example if you run the project on your localhost and default port, you can see the list of APIs and their documentation at the address of "http://127.0.0.1:5000/api/docs/"


# طریقه اجرای پروژه بر روی دستگاه خود

## راه اندازی پیش نیاز های اولیه

1: پروژه را بر روی دستگاه خود کلون کنید --> git clone https://github.com/Reza98Sh/BOM-backend.git           
2: محیط مجازی را بر روی دستگاه خود بسازید برای ایزوله کردن پروژه (از قبل برای شما نصب باشد virtualenv دقت کنید که پکیج) --> virtualenv venv                                                                             
3: فعال کردن محیط مجازی -->
- اگر سیستم عامل شما ویندوز است : source venv/bin/activate
- اگر سیستم عامل شما لینوکس یا مک است : . venv/bin/activate

## نصب پکیج ها

4. نصب کردن پکیج هایی که برای اجرای پروژه به آنها نیاز دارید --> pip install -r requirements.txt

## پایگاه داده

5: ساخت پایگاه داده بر اساس اکسل دیتا ها و مایگریشن های اولیه --> flask db upgrade

## استفاده و اجرای پروژه

6: پس از ساخت پایگاه داده میتوانید پروژه را بر اساس دستور های زیر اجرا کنید -->                                              
- روی هاست دستگاه --> flask run
- روی هاست دستگاه و همچنین روی آدرس آی پی دستگاه --> flask run --host=0.0.0.0 --port=5000
- در انتهای دستور خود وارد کنید '--debug' همچنین اگر مایلید ارور ها و مشکلات پروژه را مشاهد نمایید عبارت 
-  نکته : دقت نمایید که از عیارت بالا در مرحله بهره برداری استفاده ننمایید بعلت مشکلات امنیتی

## داکیومنت و رابط کاربری آدرس های سرور

7. لینک مقابل برای لیست آدرس های سرور در رابط کاربری است --> /api/docs
- برای مثال اگر پروژه را بر روی هاست دستگاه خود و پورت پیشفرض اجرا نمایید میتوانید رابط کاربری آدرس ها و 
 داکیونت های آنها را در آدرس زیر مشاهده نمایید : "http://127.0.0.1:5000/api/docs/"
