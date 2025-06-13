import streamlit as st
import pandas as pd
from datetime import datetime
import random
st.set_page_config(page_title='广西职业师范学院',layout='wide')
st.image('https://img1.baidu.com/it/u=881222942,1912575794&fm=253&fmt=auto&app=120&f=JPEG?w=380&h=380',width=250)

tab1, tab2, tab3 = st.tabs(["数字档案", "南宁美食数据", "个人简历生成器"])


with tab1:
    st.title("🕶️ 学生 小陆 - 数字档案")



# 基础信息章节

    st.header("🔑 基础信息")

    st.text("学生ID: NEO-2023-001")

    st.markdown("**注册时间**: `2023-10-01 08:30:17` | **精神状态**: ✅ 正常")

    st.markdown("**当前教室**: `实训楼301` | **安全等级**: `绝密`")



# 技能矩阵章节

    st.header("📊 技能矩阵")

    col1, col2, col3 = st.columns(3)

    col1.metric("C语言", "95%", "2%", help="近期训练提升") 

    col2.metric("Python", "87%", "-1%")

    col3.metric("Java", "68%", "-10%", help="用则进废则退")



# 进度条展示

    st.subheader("Streamlit课程进度")

    st.progress(28, text="Streamlit课程进度")



# 任务日志章节

    st.header("📝 任务日志")

    mission_data = {

        "日期": ["2023-10-01", "2023-10-05", "2023-10-12"],

        "任务": ["学生数字档案", "课程管理系统", "数据图表展示"],

        "状态": ["✅ 完成", "🕒 进行中", "❌ 未完成"],

        "难度": ["★☆☆☆☆", "★★☆☆☆", "★★★☆☆"]

        }

    mission_df = pd.DataFrame(mission_data)

    st.table(mission_df.style.applymap(

        lambda x: 'color: #0f0' if x == "✅ 完成" else 'color: #ff0')

    )



# 代码块展示

    st.subheader("🔐 最新代码成果")

    st.code('''def matrix_breach():

        while True:

            if detect_vulnerability():

                exploit()

                return "ACCESS GRANTED"

            else:

                stealth_evade()''', language='python')



# 动态信息流

    st.write("---")

    st.write("`>> SYSTEM MESSAGE:` 下一个任务目标已解锁...")

    st.write("`>> TARGET:` 课程管理系统")

    st.write("`>> COUNTDOWN:`", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))



# 终端效果

    st.markdown("""

    系统状态: 在线

    连接状态: 已加密

    """)
with tab2:

    st.title("😍南宁美食探索")
    st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置")
    restaurants = pd.DataFrame({
        "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "白妈螺狮粉"],
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "人均消费(元)": [15, 20, 25, 35, 50],
        "lat": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "lon": [108.222177,108.353921,108.266629,108.378664,108.245804]

    })
    df=pd.DataFrame(restaurants)

    st.header("🗺️南宁美食地图")
    st.map(df)

    st.header("🏆餐厅评分")
    st.bar_chart(df,x="餐厅",y="评分")

    st.header("✨不同类型餐厅价格")
    df_price=df[["类型","人均消费(元)"]]
    st.line_chart(df, x='类型',y='人均消费(元)',use_container_width=True)

    st.header("😋用餐高峰时段")
    data = {
        '月份':['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月'],
        '星艺会尝不忘':[12,34,25,43,10,12,33,45,66,70,80,50],
        '高峰柠檬鸭':[20,40,30,60,80,20,33,43,23,55,66,59],
        '复记老友粉':[10,30,50,70,80,20,33,37,54,56,12,20],
        '好友缘':[20,33,43,50,70,40,30,50,44,77,60,90],
        '白妈螺狮粉':[12,30,40,24,50,33,47,59,80,76,56,34]
    }
# 根据上面创建的data，创建数据框
    df = pd.DataFrame(data)
# 定义数据框所用的新索引
    index = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12], name='序号')
# 将新索引应用到数据框上
    df.index = index
    st.header("用餐高峰时段")
    st.area_chart(df, x='月份')


    st.header("🍽️ 餐厅详情")
    restaurants = {
        "星艺会尝不忘": {
           "评分": "4.2/5.0",
            "人均消费": "15元",
             "推荐菜品": ["桂林米粉", "瘦肉粉", "干拌粉"],
             "拥挤度": 84
        
         },
         "高峰柠檬鸭": {
             "评分": "4.5/5.0",
              "人均消费": "20元",
             "推荐菜品": ["特色套餐", "地方消食", "时令蔬菜"],
             "拥挤度":90
    
          },
         "复记老友粉": {
             "评分": "4.0/5.0",
              "人均消费": "25元",
             "推荐菜品": ["老友牛肉", "老友猪肉", "炒粉"],
             "拥挤度":80
          },
            "好友缘": {
             "评分": "4.7/5.0",
              "人均消费": "35元",
             "推荐菜品": ["特色套餐", "地方消食", "时令蔬菜"],
             "拥挤度":94
          },
            "白妈螺蛳粉": {
             "评分": "4.3/5.0",
              "人均消费": "50元",
             "推荐菜品": ["特色套餐", "地方消食", "时令蔬菜"],
             "拥挤度":86
          }
    }
    selected_restaurant = st.selectbox("选择餐厅",options=list(restaurants.keys()),index=0)
    info = restaurants[selected_restaurant]
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(selected_restaurant)
        st.write(f"评分：{info['评分']}")
        st.write(f"人均消费：{info['人均消费']}")
        st.subheader("当前拥挤程度")
        st.progress(info["拥挤度"], text=f"{info['拥挤度']}% 拥挤")
        st.subheader("🎲 今日午餐推荐")
        if st.button("帮我选午餐", key="lunch_btn"):
            random_shop = random.choice(list(restaurants.keys()))
            st.success(f"今日推荐：{random_shop}")
    with col2:
        st.write("本店推荐菜品：")
        for dish in info["推荐菜品"]:
            st.markdown(f"- {dish}")
        
with tab3:
    
    
    st.title('👨‍💼 个人简历生成器')
    st.text('使用Streamlit创建你的个性化简历')
    col_left, col_right = st.columns(2)

    with col_left:
    # 左侧表单：用 st.text_input/st.selectbox 等组件
        st.header('📝 信息表单')
        st.write('***')
        xm = st.text_input('姓名')
        job = st.text_input('职业')
        phone = st.text_input('电话号码')
        email = st.text_input('邮箱')
        birthday = st.text_input('出生日期')
        xb = st.radio(
            '性别',
            ['男', '女', '其他'],
            horizontal=True
        )
        education = st.selectbox('学历', ['小学', '初中', '高中', '大专', '本科', '研究生'])

        def my_format_func(option):
            return f'{option}'

        st.multiselect(
            '语言能力(可多选)',
            ['Chinese', 'English', 'Japanese', 'French', 'Spanish', 'Arabic'],
            format_func=my_format_func,
        )
        jn = st.multiselect(
            '技能(可多选)',
            ['SQL', 'python', 'C语言', 'Java', '数据库'],
            format_func=my_format_func,
        )
        time = st.selectbox(
            '每日最佳联系时间段',
            ['9:30-11:00', '14:30-17:30', '19:00-20:00', '21:00-22:00'],
        )

        my_range = range(0, 21)
        jy = st.select_slider('工作经验（年）', options=my_range)
        st.write(jy)
        xz = st.select_slider(
            '期望薪资范围（元）',
            options=range(5000, 50001),
            value=(10000, 20000)
        )
        introduced = st.text_area('个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点...')
        uploaded_photo = st.file_uploader('上传个人照片', type=['jpg', 'jpeg', 'png', 'gif'])
        if uploaded_photo is not None:
        # 显示上传的照片
            st.session_state['photo'] = uploaded_photo
            st.image(uploaded_photo, caption='您上传的照片')
        else:
            st.session_state['photo'] = None

    with col_right:
    # 右侧实时预览：用 st.write/st.header 渲染内容
        st.header('简历实时预览')
        st.write('***')
        info_col1, info_col2 = st.columns(2)
        with info_col1:
            st.write(f"职位：{job}")
            st.write(f"电话：{phone}")
            st.write(f"邮箱：{email}")
            st.write(f"出生日期：{birthday.strftime('%Y/%m/%d') if birthday else ''}")

        with info_col2:
        # 基础信息
            st.write(f"性别：{xb}")
            st.write(f"学历：{education}")
            st.write(f"工作经验：{jy}")
            st.write(f"期望薪资：{xz}")
            st.write(f"个人简介：{introduced}")
            st.write(f"最佳联系时间: {time}")

        st.write("***")
# 个人简介
        st.header("个人简介")

        st.write("***")
        st.header("专业技能")
        st.write(jn)

