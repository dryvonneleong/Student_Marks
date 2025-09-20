
import streamlit as st
import pandas as pd

data = {'Name': ['Tan Yong Xiang', 'Chye Yong Xin', 'Wong Wei Feng', 'Tai Wei Horng', 'Sueanne Foo Su Xin', 'Yaashana', 'Gan Sin Hui', 'Leo Jia Yee', 'Liew Qian Yi', 'Loo Pei Yi', 'Lee Tze Lok', 'Loo Wing Hong', 'Choy Zhen Yang', 'Yong Zheng Xian', 'Aviinaash Mani Maaran', 'Owen Low', 'Lim Chern Hau', 'Poh Wei Wei ', 'Zra Amar Zulhaziq Bin Zulkifli', 'Keerthika A/P Venkata Giri  Naidu ', 'Phua Ying Ying', 'Deepavaathy', 'Gan Cai Yan', 'Lee Mei Kei', 'Lim Fei Yang-Deutche Bank', 'Ong Xin Ying', 'Ang Li Fang', 'Chan Wei Zhi Natalie', 'Khu Miky', 'Pang Yue Ning', 'Tie Yun Theng', 'Cheong Hui Dee', 'Isaac A/L John Ramesh', 'Lim Lai Yee', 'Preethika A/p Muthu Kumaran', 'Tan See Wai-Starbuck', 'Thien Yaw Hsiang', 'Alicia Low Pui Yan', 'Ang Zi Yang', 'Loo Yun Wei', 'Low Yee Hua', 'Chong Jia Yee', 'Kong Jin Mun', 'Tan Zoe', 'You Jing Xiu', 'ONG JUN KHAI', 'ANG YUE HAO', 'POON CHUN YUAN', 'SOH YU XUAN', 'SOONG MUN CHOY', 'Lum Kar Man', 'Goon De Xon', 'Chay Joe Yan', 'Yong Yuen Xian ', 'Yow Enqi', 'Chong Hee Heng', 'Chong Siong Zhi', 'Lo Woan En', 'Ng Hao Zheng', 'Mathavender A/L Muniandi', 'Tan Ching Er ', 'Soh Ker Qing ', 'Chin Wen Shuen ', 'Lau Shi Shu ', 'Saw Tian Le ', 'Low Fen Yee', 'Shee Jie Xin ', 'Ting Mei Xin', 'Lim Hwa Jin ', 'Hay Shan Mian ', 'Chua Jia Xuan', 'Fam Pei Yee', 'Lim Jiar Xuan', 'Tan Jia Ni', 'Tang Tuang Jun', 'Chan Sze Jia', 'Olivia Tung', 'Shivashangary', 'Teh Kai Jun', 'Yuki Hoo Shu Zhen', 'CHOW JIA NING', 'CHEW ZHI WEI', 'LEE JIA XUAN', 'SIA WEI TUNG', 'TEE GUI QIAN', 'WONG XIU WEN', 'POO JING WOON ', 'CHAI YI LIN', 'CHEE YI SHAN', 'FOONG PUI SAN', 'TAN GWO FU', 'YAP HO YAN', 'LOK EN HUI', 'LAI QING GUO', 'LIM MEI YI', 'POH LI YIN', 'WONG JIA JUN'], 'Marks': [80, 96, 90, 96, 90, 94, 96, 96, 96, 94, 94, 92, 94, 88, 80, 92, 80, 86, 92, 96, 74, 88, 96, 92, 84, 94, 90, 96, 90, 90, 92, 92, 66, 90, 86, 84, 92, 94, 82, 94, 94, 96, 94, 94, 90, 90, 90, 92, 98, 92, 94, 90, 90, 94, 92, 90, 96, 92, 96, 96, 96, 98, 92, 92, 90, 94, 94, 96, 92, 96, 96, 90, 98, 96, 94, 92, 94, 90, 90, 92, 90, 92, 86, 90, 92, 92, 98, 92, 96, 96, 92, 98, 88, 92, 92, 90, 92]}
df = pd.DataFrame(data)

st.title('Student Marks Viewer')

student_name = st.text_input('Enter your full name exactly as in the list:')

if student_name:
    result = df[df['Name'].str.strip().str.lower() == student_name.strip().lower()]
    if not result.empty:
        st.success(f"Hi {student_name}, your mark is: {result.iloc[0]['Marks']}")
    else:
        st.error('Name not found. Please check the spelling and try again.')
