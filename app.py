import streamlit as st
from streamlit_option_menu import option_menu
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sm

def main():
    st.set_page_config(page_title='تکمیلی ریاضی هفتم', page_icon='logomath.jpg', layout='wide', initial_sidebar_state='auto')
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #fff;
            secondary-background-color: #2ae659;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
main()
titleasli = 'به نام خدا'
st.write(f'<div style="text-align:center">{titleasli}</div>', unsafe_allow_html=True)
headerasli = 'برنامه تکمیلی ریاضی هفتم'
st.write(f'<div style="text-align:center">{headerasli}</div>', unsafe_allow_html=True)
jomle = 'سریع و مطمئن، برس به جواب!'
st.write(f'<div style="text-align:center">{jomle}</div>', unsafe_allow_html=True)
placeholder = st.empty()
add_selectbox = st.sidebar.selectbox(
    'کدام فصل را میخواهید؟',
    ('صفحه اصلی','فصل 1','فصل 2','فصل 3','فصل 5','فصل 6','فصل 7','فصل 8','فصل 9','راهنمای برنامه','درباره ما'),
)


# راهنمای برنامه
if add_selectbox == 'راهنمای برنامه':
    with placeholder.container():
            text1 = 'سلام دوستان'
            st.write(f'<div style="text-align:right">{text1}</div>', unsafe_allow_html=True)
            text2 = 'ما اینجا 8 تا فصل داریم که فصل های کتاب ریاضی هستند ما برای اینکه شما بهتر بتوانید از برنامه ما استفاده کنید اینجا هر فصل را برایتان توضیح دادیم.'
            st.write(f'<div style="text-align:right">{text2}</div>', unsafe_allow_html=True)
            text3 = 'فصل ۱: در این فصل ۵ تا سرفصل داریم که الگو مثلثی، الگو مربعی، الگو مکعبی، دنباله فیبوناچی و فاکتوریل هستند.'
            st.write(f'<div style="text-align:right">{text3}</div>', unsafe_allow_html=True)
            text4 = 'فصل ۱: در این فصل ۵ تا سرفصل داریم که الگو مثلثی، الگو مربعی، الگو مکعبی، دنباله فیبوناچی و فاکتوریل هستند.'
            st.write(f'<div style="text-align:right">{text4}</div>', unsafe_allow_html=True)
            text5 = 'اگر شما الگو ها یا دنباله فیبوناچی را انتخاب کنید تا یک میلیون اعداد آن الگو یا دنباله فیبوناچی برایتان به نمایش در می آید.'
            st.write(f'<div style="text-align:right">{text5}</div>', unsafe_allow_html=True)
            text6 = 'اگر فاکتوریل رو انتخاب کنید هر عددی که بزنید فاکتوریل اون عدد برایتان به نمایش در می آید.'
            st.write(f'<div style="text-align:right">{text6}</div>', unsafe_allow_html=True)
            text7 = 'فصل ۲: ما دو تا سرفصل اینجا داریم که جمع و تفریق و ضرب و تقسیم هستند. اگر شما جمع و تفریق را بخواهید گزینه جمع و تفریق را انتخاب کنید و اگر ضرب و تقسیم می خواهید گزینه ضرب و تقسیم را انتخاب کنید. توجه داشته باشید که در هر گزینه از شما می پرسیم که کدام یک را می خواهید جمع یا تفریق و ضرب یا تقسیم.'
            st.write(f'<div style="text-align:right">{text7}</div>', unsafe_allow_html=True)
            text8 = 'فصل ۳: در اینا ما دو تا سرفصل داریم که مقدار عددی عبارت جبری و ساده کردن عبارت جبری هستند. اگر شما مقدار عددی عبارت جبری را بخواهید اعداد مورد نظر خود را وارد می کنید، بعد عبارت جبری خود را وارد می کنید و جواب رو تحویل می گیرید.'
            st.write(f'<div style="text-align:right">{text8}</div>', unsafe_allow_html=True)
            text9 = 'اگر هم ساده کردن عبارت جبری رو بخواهید عبارت جبری خودتان را وارد می کنید و ساده شده‌ آن را تحویل می گیرید.'
            st.write(f'<div style="text-align:right">{text9}</div>', unsafe_allow_html=True)
            text10 ='فصل ۵: اینجا سه سرفصل مهم داریم که اعداد اول، ب.م.م و ک.م.م هستند.'
            st.write(f'<div style="text-align:right">{text10}</div>', unsafe_allow_html=True)
            text11 ='اگر اعداد اول رو انتخاب کنید از شما می پرسیم که اعداد اول را تا عدد ۱۰۰ می خواهید یا ۱۰۰۰ هر کدام را که انتخاب کنید تا آن عدد برایتان اعداد اول به نمایش در می آیند.'
            st.write(f'<div style="text-align:right">{text11}</div>', unsafe_allow_html=True)
            text12 ='اگر شما دوستان عزیز ب.م.م را انتخاب کنید دو عدد را وارد می کنید و ب.م.م آن را برایتان به دست می آوریم.'
            st.write(f'<div style="text-align:right">{text12}</div>', unsafe_allow_html=True)
            text13 ='در قسمت ک.م.م هم شما دو عدد را وارد می کنید و ک.م.م آن را برایتان به دست می آوریم.'
            st.write(f'<div style="text-align:right">{text13}</div>', unsafe_allow_html=True)
            text14 ='فصل ۶: اینجا از شما می پرسیم که چند وجهی می خواهید، حالا چرا؟در این فصل که مربوط به هندسه هست ما برایتان یال ها، رئوس، وجه های جانبی و وجه های کل آن چند وجهی که وارد می کنید را برایتان محاسبه می کنید. البته به انتخاب خودتان هر کدام را که بخواهید محاسبه میکنیم.'
            st.write(f'<div style="text-align:right">{text14}</div>', unsafe_allow_html=True)
            text15 ='فصل ۷: فصل توان و رادیکال؟ بله، در این فصل ما چهار تا سرفصل برایتان گذاشتیم که اعداد مربعی، رادیکال، جمع توان و تفریق توان ها هستند. قبل از اینکه سرفصل ها رو توضیح بدهم شما بعد از انتخاب سرفصل، دو عدد رو وارد می کنید.'
            st.write(f'<div style="text-align:right">{text15}</div>', unsafe_allow_html=True)
            text16 ='در سرفصل اعداد مربعی چیکار می کنیم؟ اینجا دوباره سرفصل داریم اما سه تا. عدد اول به توان دوم، مجذور و عدد دوم به توان عدد اول.'
            st.write(f'<div style="text-align:right">{text16}</div>', unsafe_allow_html=True)
            text17 ='حالا در این عدد اول به توان عدد دوم یا عدد دوم به توان عدد اول چیکار می‌ کنیم؟ آن دو عددی را که وارد کرده بودید رو به توان هم می رسانیم به این شکل که عدد اولی که وارد می کنید به عنوان عدد اول برایتان ثبت می شود و عدد دوم هم به عنوان عدد دوم. در مجذور هم که شما از آن دو عددی که وارد کرده بودید یکی را انتخاب می کنید و ما آن را به توان دو می رسانیم.'
            st.write(f'<div style="text-align:right">{text17}</div>', unsafe_allow_html=True)
            text18 ='در قسمت رادیکال شما دو عدد را انتخاب می کنید و ما از شما می پرسیم که از کدام رادیکال بگیریم عدد اول یا عدد دوم. هر کدام را که انتخا کردید را از آن رادیکال می‌ گيريم.'
            st.write(f'<div style="text-align:right">{text18}</div>', unsafe_allow_html=True)
            text19 ='در جمع توان شما دو عدد را وارد می کنید و برای هر کدام یک توان انتخاب می کنید و ما آن دو عدد را با هم جمع می‌ کنیم.'
            st.write(f'<div style="text-align:right">{text19}</div>', unsafe_allow_html=True)
            text20 ='در قسمت تفریق توان ها هم شما دوستان عزیز دو عدد با توان هایشان را مانند قسمت جمع توان انتخاب می کنید و ما آنها را از هم کم می کنیم.'
            st.write(f'<div style="text-align:right">{text20}</div>', unsafe_allow_html=True)
            text21 ='فصل ۸: در این فصل ما مختصات را داریم.'
            st.write(f'<div style="text-align:right">{text21}</div>', unsafe_allow_html=True)
            text22 ='ما از شما می خواهیم که دو عدد را برای محور های x و y وارد کنید و ما برای شما مختصات آن نقطه را در صفحه مختصات به نمایش در می آوریم.'
            st.write(f'<div style="text-align:right">{text22}</div>', unsafe_allow_html=True)
            text23 ='فصل ۹: اینجا چی داریم؟ انواع نمودار و یک قسمت مخصوص که در کتاب ریاضی هفتم نیست '
            st.write(f'<div style="text-align:right">{text23}</div>', unsafe_allow_html=True)
            text24 ='به نظرتان چه چیزی می تواند باشد؟ پیدا کردن وتر مثلث از روی دو ضلع دیگرش.'
            st.write(f'<div style="text-align:right">{text24}</div>', unsafe_allow_html=True)
            text25 ='ما در این فصل سه نمودار داریم که نمودار خطی دایره ای و ستونی هستند.'
            st.write(f'<div style="text-align:right">{text25}</div>', unsafe_allow_html=True)
            text26 ='در نمودار خطی شما اعداد مورد نظر خود را وارد می کنید و یک نمودار خطی تحویل می گیرید. فقط به یک نکته توجه داشته باشید که لطفا اعداد را به هم ریخته ندهید یا از کوچک به بزرگ بدهید یا برعکس.'
            st.write(f'<div style="text-align:right">{text26}</div>', unsafe_allow_html=True)
            text27 = 'در نمودار دایره ای شما چهار موضوع و چهار عدد را وارد می‌ کنید و نمودار دایره ای را تحویل می گیرید.'
            st.write(f'<div style="text-align:right">{text27}</div>', unsafe_allow_html=True)
            text28 = 'در نمدار ستونی هم اعداد مورد نظر خود را وارد می کنید این نمودار را بزایتان به نمایش در می آوریم.'
            st.write(f'<div style="text-align:right">{text28}</div>', unsafe_allow_html=True)
            text29 = 'حالا می رسیم به بخش، وتر مثلث.'
            st.write(f'<div style="text-align:right">{text29}</div>', unsafe_allow_html=True)
            text30 = 'در این قسمت شما دو عدد را وارد می کنید و ما آن دو را به توان دو می رسانیم و با هم جمع می‌ کنيم و از آن رادیکال می گیریم. در آن هنگام وتر مثلث را به سادگی به دست می آورید.'
            st.write(f'<div style="text-align:right">{text30}</div>', unsafe_allow_html=True)
            text31 = 'امیدواریم این توضیحات برایتان مفید بوده باشد تا به راحتی بتوانید از برنامه ما استفاده کنید.'
            st.write(f'<div style="text-align:right">{text31}</div>', unsafe_allow_html=True)
# درباره ما

if add_selectbox == 'درباره ما':
    with placeholder.container():
        tozih = 'برنامه تکمیلی ریاضی هفتم چیست؟'
        darbarehma = 'برنامه <تکمیلی ریاضی هفتم> را میتوان به عنوان یک اپلیکیشن کمک آموزشی برای دانش آموزان پایه هفتم دانست. میتوان گفت این برنامه جزو کامل ترین برنامه ها اعم از تقریبا تمامی سرفصل های کتاب ریاضی هفتم و فراتر از آن است. این برنامه توسط آقایان یونا تدین و رادین اردیبهشت، دانش آموزان دبیرستان علامه حلی 6 ساخته شده است. این برنامه به کمک زبان برنامه نویسی پایتون و در محیط ویژوآل استودیو کد و به کمک 10 کتابخانه پایتون نوشته شده است. همجنین این برنامه دارای 8 فصل کتاب ریاضی هفتم است.'
        ertebat = 'برای برقراری ارتباط با طراحان این برنامه میتوانید با ایمیل زیر ارتباط برقرار کنید: '
        email = 'younatadayon.work@gmail.com'
        linkedin = 'https://www.linkedin.com/in/youna-tadayon-717b35250/'
        st.write(f'<div style="text-align:right">{tozih}</div>', unsafe_allow_html=True)
        st.write(f'<div style="text-align:right">{darbarehma}</div>', unsafe_allow_html=True)
        st.write(f'<div style="text-align:right">{ertebat}</div>', unsafe_allow_html=True)
        st.write(f'<div style="text-align:left">{email}</div>', unsafe_allow_html=True)
        st.write(f'<div style="text-align:left">{linkedin}</div>', unsafe_allow_html=True)

    

    
# فصل 1    
    
if add_selectbox == 'فصل 1':
    st.write('')
    st.write('')
    st.write('')
    entekhabmozoo1 = option_menu(menu_title="کدام سر فصل را میخواهید؟",
                                options=['الگو های مثلثی',"الگو های مربعی","الگو های مکعبی","دنباله فیبوناتچی",'فاکتوریل'],
                                icons=['triangle','square','box','123','exclamation-lg'],
                                orientation='vertical')
    if entekhabmozoo1 == 'الگو های مثلثی':
        n = 1
        st.write('فرمول: (n*(n+1))/2')
        while n < 1414:
            st.write(n*(n+1)/2)
            n += 1
    elif entekhabmozoo1 == 'الگو های مکعبی':
        n = 1 
        st.write('فرمول: n**3')
        while n < 101:
            st.write((n**3))
            n += 1    
    elif entekhabmozoo1 == 'الگو های مربعی':
        n = 1
        st.write('فرمول: n**2')
        while n< 1001:
            st.write((n**2))
            n += 1
    elif entekhabmozoo1 == 'دنباله فیبوناتچی':
        st.write('فرمول: از 0 شروع میشود و بعد دو تا یک و بعد دو عدد قبلی با همه جمع میشود و عدد بعدی را میسازند')
        def fibonacci(n):
            fib = [0,1]
            while fib[-1] < n:
                fib.append(fib[-1] + fib[-2])
            return fib[:-1]
        n = st.number_input('یک عدد وارد کنید: ')
        fib = fibonacci(n)
        st.write(fib)
    elif entekhabmozoo1 == 'فاکتوریل':
        chandfactorial = st.number_input("چند فاکتوریل: ", value=5 , step=1)
        if chandfactorial<0:
            st.error('لطفا عددی بزرگ تر از 0 وارد کنید')
        else:
            result = math.factorial(chandfactorial)
            factorial = 'جواب'
            factorial1 = 'برابر است با: '
            st.write(f'<div style="text-align:right">{factorial}{chandfactorial}{factorial1}{result}</div>', unsafe_allow_html=True)


# فصل 2         

elif add_selectbox == "فصل 2":
    st.write('')
    st.write('')
    st.write('')
    entekhabmozoo2 = option_menu(menu_title="کدام سر فصل را میخواهید؟",
                                options=['جمع و تفریق اعداد صحیح',"ضرب و تقسیم اعداد صحیح"],
                                icons=['plus-slash-minus','x-lg'],
                                orientation='vertical')
    adad0 = 'ففط میتوانید دو عدد وارد کنید'
    st.write(f'<div style="text-align:right">{adad0}</div>', unsafe_allow_html=True)
    adad1 = st.slider('عدد اول را وارد کنید: ')
    adad2 = st.slider('عدد دوم را وارد کنید: ')
    if entekhabmozoo2 == 'جمع و تفریق اعداد صحیح':
        mosbatmanfi = st.text_input('جمع یا تفریق(+ و - ) ')
        if mosbatmanfi == '+':
            jam = 'جواب جمع دو عدد برابر است با: '
            st.write(f'<div style="text-align:right">{jam}{float(adad1)+float(adad2)}</div>', unsafe_allow_html=True)
        elif mosbatmanfi == '-':
            tafrigh = 'جواب تفریق دو عدد برابر است با: '
            st.write(f'<div style="text-align:right">{tafrigh}{float(adad1)-float(adad2)}</div>', unsafe_allow_html=True)
    elif entekhabmozoo2 == 'ضرب و تقسیم اعداد صحیح':
        zarbotaghsim = st.text_input('ضرب و تقسیم(* و /)')
        if zarbotaghsim == '*':
            zarb = 'جواب جمع دو عدد برابر است با: '
            st.write(f'<div style="text-align:right">{zarb}{float(adad1)*float(adad2)}</div>', unsafe_allow_html=True)
        elif zarbotaghsim == '/': 
            taghsim = 'جواب جمع دو عدد برابر است با: '
            st.write(f'<div style="text-align:right">{taghsim}{float(adad1)/float(adad2)}</div>', unsafe_allow_html=True)

            

# فصل 3
            
            
elif add_selectbox == 'فصل 3':
    st.write('')
    st.write('')
    st.write('')
    entekhabmozoo3 = option_menu(menu_title='کدام سر فصل را میخواهید؟',
                                    options=['ساده کردن عبارت جبری','مقدار عددی عبارت جبری'],
                                    icons=['xyz','math-xy'],
                                    orientation='vertical')
    if entekhabmozoo3 == 'ساده کردن عبارت جبری':
        try:
            ebaratjabrisade = st.text_input('جبر خود را وارد کنید: ')
            result = sm.simplify(ebaratjabrisade)
            st.write(f'{result}')
        except:
            pass
    elif entekhabmozoo3 == 'مقدار عددی عبارت جبری':
        try:
            adad0 = 'فقط میتوانید دو عدد وارد کنید'
            st.write(f'<div style="text-align:right">{adad0}</div>', unsafe_allow_html=True)
            adad1 = st.slider('عدد اول را وارد کنید: ')
            adad2 = st.slider('عدد دوم را وارد کنید: ')
            xyay = st.text_input('عدد اول کدام است؟ x , y')
            if xyay == 'x':
                x = adad1
                y = adad2
            elif xyay == 'y':
                x = adad2
                y = adad1
            ebaratjabrimeghdar = st.text_input('جبر خود را وارد کنید: ')

            result = eval(ebaratjabrimeghdar)
            text = 'جواب ='
            st.write(f'<div style="text-align:right">{text}{result}</div>', unsafe_allow_html=True)
        except:
            pass
# فصل 5
                    



elif add_selectbox == 'فصل 5':
    st.write('')
    st.write('')
    st.write('')
    entekhabmozoo5 = option_menu(menu_title='کدام سرفصل را میخواهید؟',
                                 options=['اعداد اول','ب.م.م','ک.م.م'],
                                 icons=['calendar-proton-23','parentheses','braces'],
                                 orientation='vertical')

    if entekhabmozoo5 == 'اعداد اول':
        haundred_or_tausend = st.number_input('1000 or 100')
        if haundred_or_tausend == 100:
            st.write('2,3,5,7,11,13,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97')
        elif haundred_or_tausend == 1000:
            st.write('2,3,5,7,11,13,19,23,29,31,37,41,43,47,53,159,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,397,401,409,419,421,431,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997')
    elif entekhabmozoo5 == 'ب.م.م':
        adad0 = 'فقط میتوانید دو عدد وارد کنید'
        st.write(f'<div style="text-align:right">{adad0}</div>', unsafe_allow_html=True)
        adad1 = st.slider('عدد اول را وارد کنید: ')
        adad2 = st.slider('عدد دوم را وارد کنید: ')
        st.write(math.gcd(adad1, adad2))
    elif entekhabmozoo5 == 'ک.م.م':
        adad0 = 'فقط میتوانید دو عدد وارد کنید'
        st.write(f'<div style="text-align:right">{adad0}</div>', unsafe_allow_html=True)
        adad1 = st.slider('عدد اول را وارد کنید: ')
        adad2 = st.slider('عدد دوم را وارد کنید: ')
        st.write(math.lcm(adad1,adad2)) 
        
# # فصل 6    


elif add_selectbox == 'فصل 6':
    st.write('')
    st.write('')
    st.write('')
    chandvajhi = st.number_input('چند وجهی میخواهید؟ عدد وارد کنید: ')
    entekhabmozoo6 = option_menu(menu_title='کدام سر فصل را میخواهید؟ ',
                                 options=['تعداد یال ها','تعداد رئوس','تعداد وجه های جانبی','تعداد وجه کل'],
                                 icons=['cube-16-regular','3d-cube-sphere','cube-fill','cube-unfolded'],
                                 orientation='vertical')

    if entekhabmozoo6 == 'تعداد یال ها':
        yal = 3 * chandvajhi
        yal1 = 'تعداد یال ها برابر است با: '
        st.write(f'<div style="text-align:right">{yal1} {yal}</div>', unsafe_allow_html=True)
    elif entekhabmozoo6 == 'تعداد رئوس':
        raas = 2 * chandvajhi
        raas1 = 'تعداد رئوس برابر است با: '
        st.write(f'<div style="text-align:right">{raas1} {raas}</div>', unsafe_allow_html=True)
    elif entekhabmozoo6 == 'تعداد وجه های جانبی':
        vajh_janebi = chandvajhi
        vajh_janebi1 = 'تعداد وجه های جانبی برابر است با '
        st.write(f'<div style="text-align:right">{vajh_janebi} {vajh_janebi1}</div>', unsafe_allow_html=True)
    elif entekhabmozoo6 == 'تعداد وجه کل':
        kol_vojooh = chandvajhi + 2
        kol_vojooh1 = 'تعداد کل وجه های برابر است با: '
        st.write(f'<div style="text-align:right">{kol_vojooh} {kol_vojooh1}</div>', unsafe_allow_html=True)
    
# # فصل 7

            
elif add_selectbox == 'فصل 7':
    st.write('')
    st.write('')
    st.write('')
    entekhabmozoo7 = option_menu(menu_title='کدام سرفصل را میخواهید؟',
                                 options=['اعداد مربعی','رادیکال','تفریق توان','جمع توان'],
                                 icons=['superscript','subscript','minus-lg','plus-lg'],
                                 orientation='vertical')
    adad0 = 'فقط میتوانید دو عدد وارد کنید'
    st.write(f'<div style="text-align:right">{adad0}</div>', unsafe_allow_html=True)
    adad1 = st.slider('عدد اول را وارد کنید: ')
    adad2 = st.slider('عدد دوم را وارد کنید: ')
    if entekhabmozoo7 == 'اعداد مربعی':
        entekhabadadmoraba = option_menu(menu_title='کدام را میخواهید؟',
                                         options=['عدد اول به توان عدد دوم','مجذور','عدد دوم به توان عدد اول'],
                                         icons=['','',''],
                                         orientation='vertical')
        if entekhabadadmoraba == 'عدد اول به توان عدد دوم':
            st.write(adad1 ** adad2)
        elif entekhabadadmoraba == 'عدد دوم به توان عدد اول':
            st.write(adad2 ** adad1)
        elif entekhabadadmoraba == 'مجذور':
            yekyado = option_menu(menu_title='عدد اول یا عدد دوم',
                                options=['عدد اول','عدد دوم'],
                                orientation='vertical')
            if yekyado == 'عدد اول':
                st.write(adad1**2)
            elif yekyado == 'عدد دوم': 
                st.write(adad2**2)
    elif entekhabmozoo7 == 'رادیکال':
        adad1yaadad2 = option_menu(menu_title='عدد اول یا عدد دوم؟',
                                   options=['عدد اول', 'عدد دوم'],
                                   orientation='vertical')
        if adad1yaadad2 == 'عدد اول':
            st.write(np.sqrt(adad1))
        if adad1yaadad2 == 'عدد دوم':
            st.write(np.sqrt(adad2))
    elif entekhabmozoo7 == 'تفریق توان':
        oneortwo = option_menu(menu_title='عدد اول یا عدد دوم',
                                options=['عدد اول','عدد دوم'],
                                orientation='vertical')
        if oneortwo == 'عدد اول':
            tavan1 = st.number_input('توان عدد اول: ')
            tavan2 = st.number_input('توان عدد دوم: ')
            st.write((adad1 ** tavan1) - (adad2 ** tavan2))
        elif oneortwo == 'عدد دوم':
            tavan3 = st.number_input('توان عدد دوم: ')
            tavan4 = st.number_input('توان عدد اول: ')
            st.write((adad1 ** tavan3) - (adad2 ** tavan4))
    elif entekhabmozoo7 == 'جمع توان':
        oneortwo2 = option_menu(menu_title='عدد اول یا عدد دوم',
                                options=['عدد اول','عدد دوم'],
                                orientation='vertical')
        if oneortwo2 == 'عدد اول':
            tavan5 = st.number_input('توان عدد اول: ')
            tavan6 = st.number_input('توان عدد دوم: ')
            st.write((adad1 ** tavan5) + (adad2 ** tavan6))
        elif oneortwo2 == 'عدد دوم':
            tavan7 = st.number_input('توان عدد دوم: ')
            tavan8 = st.number_input('توان عدد اول: ')
            st.write((adad1 ** tavan7) + (adad2 ** tavan8))
    
# فصل 8          
            
elif add_selectbox == 'فصل 8':
    st.write('')
    st.write('')
    st.write('')
    mokhatasat = 'مختصات'
    st.write(f'<div style="text-align:center">{mokhatasat}</div>', unsafe_allow_html=True)
    adad0 = 'فقط میتوانید دو عدد وارد کنید'
    st.write(f'<div style="text-align:right">{adad0}</div>', unsafe_allow_html=True)
    adad1 = st.slider('عدد اول را وارد کنید: ')
    adad2 = st.slider('عدد دوم را وارد کنید: ')
    x = adad1
    y = adad2
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    st.pyplot(fig)
             
# فصل 9     
     
elif add_selectbox == 'فصل 9':
    st.write('')
    st.write('')
    st.write('')
    entekhabmozoo9 = option_menu(menu_title='کدام سر فصل را میخواهید؟',
                                 options= ['نمودار میله ای ','نمودار خطی','نمودار دایره ای','وتر مثلث'],
                                 icons= ['bar-chart-line','graph-up','pie-chart','triangle-ruler'],
                                 orientation='vertical')
    if entekhabmozoo9 == 'نمودار میله ای ':
        try:
            x = [st.number_input('X1: '),st.number_input('X2: '),st.number_input('X3: '),st.number_input('X4: '),st.number_input('X5: ')]
            y = [st.number_input('Y1: '),st.number_input('Y2: '),st.number_input('Y3: '),st.number_input('Y4: '),st.number_input('Y5: ')]
            fig, ax = plt.subplots()
            ax.bar(x, y)
            st.pyplot(fig)
        except:
            pass
    elif entekhabmozoo9 == 'نمودار دایره ای':
        try:
            labels = [st.text_input('موضوع 1: '),st.text_input('موضوع 2: '),st.text_input('موضوع 3: '),st.text_input('موضوع 4: ')]
            sizes = [st.number_input('عدد اول: '),st.number_input('عدد دوم: '),st.number_input('عدد سوم: '),st.number_input('عدد چهارم: ')]
            fig, ax= plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)
        except:
            pass
    elif entekhabmozoo9 == 'نمودار خطی':
        try:
            x = [st.number_input('X1: '),st.number_input('X2: '),st.number_input('X3: '),st.number_input('X4: '),st.number_input('X5: '),st.number_input('X6: '),st.number_input('X7: '),st.number_input('X8: ')]
            y = [st.number_input('Y1: '),st.number_input('Y2: '),st.number_input('Y3: '),st.number_input('Y4: '),st.number_input('Y5: '),st.number_input('Y6: '),st.number_input('Y7: '),st.number_input('Y8: ')]
            fig, ax = plt.subplots()
            ax.plot(x, y)
            st.pyplot(fig)
        except:
            pass
    elif entekhabmozoo9 == 'وتر مثلث':
        adad0 = 'فقط میتوانید دو عدد وارد کنید'
        st.write(f'<div style="text-align:right">{adad0}</div>', unsafe_allow_html=True)
        adad1 = st.slider('عدد اول را وارد کنید: ')
        adad2 = st.slider('عدد دوم را وارد کنید: ')
        st.write(np.sqrt((adad1**2)+(adad2**2)))

 