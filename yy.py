import streamlit as st

import pandas as pd
import random
# 设置页面布局为侧边栏布局（侧边栏在左，内容在右  ）
st.set_page_config(layout="wide")

# 左侧导航栏
with st.sidebar:
    st.markdown("### 导航")
    selected = st.radio(
        "选择页面",
        ["首页", "个人简历生成器", "音乐播放器", "南宁美食数据", "数字档案"]
    )

# 右侧主页内容
st.title("主页")

if selected == "首页":
    # 插入图片，这里请替换成你实际的图片路径，支持本地路径（需注意路径访问权限  ）或网络图片链接
    st.image("https://www.gxvnu.edu.cn/__local/7/4F/5D/AD938A49125924C082992B16BDD_98ECEA17_BD556.jpg?e=.jpg")  
    # 以下是文字介绍内容，可根据实际替换
    st.markdown("""
    广西职业师范学院（原广西经济管理干部学院）坐落于广西首府南宁市风景秀丽的邕江之滨、相思湖畔，是自治区人民政府直属、自治区教育厅主管的公办全日制普通本科学校，致力于培养区域经济社会发展所需要的高素质应用型、技术技能型人才和职业教育师资。

学校随着广西的解放而诞生，其前身为创建于1951年5月的广西省行政干部训练班。其后，为适应不同历史时期广西经济建设需要，学校历经了广西人民革命大学、广西行政干部学校、广西经济干部学校、广西经济管理干部学院等历史沿革，并于2019年6月经教育部批准设置为“广西职业师范学院”。在不同历史时期，学校聚焦“服务广西经济建设”发展主线，不忘建校初心、勇担办学使命，为广西经济建设和社会发展作出了不可磨灭的突出贡献，享有良好的办学声誉和广泛的社会影响。近年来，学校围绕“地方性、应用型、职师类”办学定位，落实“以本为本、应用为先、职师特色”办学思路，在服务地方产业转型升级和职业教育提质增效上取得显著成效。

学校拥有一支师德师风优良、学术水平较高、教学经验丰富的专兼职师资队伍，其中，取得硕士、博士学位教师427人。拥有包含自治区教学名师、模范教师、优秀专家、高校思想政治教育卓越教师等在内的高水平教师团队，其中，广西高等学校高水平创新团队2个，自治区课程思政教学团队5个，自治区劳模创新工作室1个。在近年教学成果评选中，获国家级、自治区级教学成果奖16项，其中，获国家级教学成果奖一等奖1项、二等奖1项；获自治区教学成果一等奖4项、二等奖6项，三等奖4项。近五年来，获厅级及以上纵向科研项目立项285项，其中国家级1项、省部级57项、厅级227项；获省部级科研成果奖6项，其中二等奖1项、三等奖5项。

学校现有12个二级学院（部），普通本科专业33个，涵盖经济学、管理学、工学、理学、教育学、文学、法学、艺术学等八个学科。获教育部“新工科”研究与实践项目1个，自治区级新工科、新文科研究与实践项目2项，广西高等学校特色专业及课程一体化建设项目3个，自治区级本科一流课程4门，自治区级课程思政示范课5门,自治区级虚拟教研室建设试点2个，广西高校重点实验室1个，自治区级实验教学中心2个，自治区级协同育人平台1个，自治区中小学生研学实践教育基地、劳动教育实践基地各1个。建有新工科协同育人中心等100多个校内外实习实训基地，与多所广西中职学校共建职业教育实习基地。近年来，以加强创新创业教育为抓手，全面促进人才培养供给侧和产业发展需求侧结构要素全方位融合，应用型人才培养质量广受认可，连续被评为广西普通高校毕业生就业创业工作突出单位，也是全区普通高校招生录取工作表现突出单位。

学校曾中标获得6项广西重大课题，并承担“推动广西经济高质量发展的重点方向和路径对策研究”等多项自治区党委、政府资政课题以及自治区工信厅、国家发展改革委、财政厅等部门专项课题的研究工作，完成自治区两化融合项目“广西新能源汽车监测平台”的建设，凸显了服务广西的特色和优势。与广西西江开发投资集团高质量共建“广西船联网工程技术研究中心”等多个校企深度合作项目，积极推进产教融合、科技创新成果转化工作，大力开展面向中小微企业的技术服务、咨询服务活动。学校还是广西干部教育培训高校基地、第七批自治区级专业技术人员继续教育基地、自治区职业教育师资培养培训基地、广西知识产权培训基地、广西生态环境保护综合行政执法实训基地以及企业经营管理人员培训基地，培训了一大批高素质党政干部、“双师型”职教师资和企业经营管理人才。

面向未来，学校将坚守建校初心、牢记办学使命，紧扣“创新性驱动，特色化建设，内涵式提升，高质量发展”总要求，深化产教融合、校企合作，推进工学结合、知行合一，努力将学校办成特色鲜明的高水平普通本科学校，在全面建设新时代壮美广西新征程中再谱新篇、再续华章。
""")
elif selected == "个人简历生成器":
    
  
  st.title('📄 个人简历生成器')
  st.text('使用Streamlit创建你的个性化简历')
  col_left, col_right = st.columns(2)
  with col_left:
# 左侧表单：用 st.text_input/st.selectbox 等组件
   st.header('个人信息表单')
   name=st.text_input('姓名')
   job=st.text_input('职业')
   phone=st.text_input('电话号码')
   email=st.text_input('邮箱')
   birthday=st.text_input('出生日期')
   xb=st.radio(
    '性别',
    ['男', '女', '其他'],
    horizontal=True
  )
   education = st.selectbox('学历',['小学', '初中', '高中','大专','本科','研究生'])

   def my_format_func(option):
    return option
   jn=st.multiselect(
    '技能(可多选)',
    ['SQL', 'python', 'C语言', 'Java', '数据库'],
    format_func=my_format_func
  )
   time = st.selectbox('每日最佳联系时间段',
                    ['9:30-11:00', '14:30-17:30', '19:00-20:00','21:00-22:00'])

   my_range = range(0, 21)
   jy=st.select_slider('工作经验（年）', options=my_range)
   xz= st.number_input('期望薪资', 5000, 500001)

   jl=st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点...')
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
    info_col1,info_col2=st.columns(2)
    with info_col1:
        st.write(f"姓名: {name}")
        st.write(f"职位: {job}")
        st.write(f"电话: {phone}")
        st.write(f"邮箱: {email}")
        st.write(f"出生日期: {birthday.strftime('%Y/%m/%d') if birthday else ''}")
    with info_col2:
        # 基础信息
       st.write(f"性别: {xb}")
       st.write(f"学历: {education}")
       st.write(f"工作经验: {jy}")
       st.write(f"期望薪资: {xz}")
       st.write(f"最佳联系时间: {time}")

# 个人简介
    st.header('个人简介')
    st.write(jl)

# 专业技能
    st.header('专业技能')
    st.write(jn) 

elif selected=="音乐播放器":
    
    st.title('🎵 简易音乐播放器')
    st.text('使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制')

# 判断内存中(session_state)有没有a
    if 'a' not in st.session_state:
        st.session_state['a'] = 0

    image_arr = [
        {
        '图片': 'https://p1.music.126.net/wSMfGvFzOAYRU_yVIfquAA==/2946691248081599.jpg?param=130y130',
        'title': '凄美地',
        '歌手': '郭顶',
        '时长': '3:07',
        'audio_file': 'https://music.163.com/#/song?id=436346833'
        },
        {
        '图片': 'https://p1.music.126.net/flFrObLA9GZdj8B0b6ni1A==/109951165480807278.jpg?param=130y130',
        'title': '是但求其爱',
        '歌手': '陈奕迅',
        '时长': '3:52',
        'audio_file': 'https://music.163.com/#/song?id=1496602290'
        },
        {
        '图片': 'https://p1.music.126.net/CDhYcShQKH2VAMENuCxWWQ==/109951164166513349.jpg?param=130y130',
        'title': '悬溺',
        '歌手': '葛东琪',
        '时长': '3:39',
        'audio_file': 'https://music.163.com/#/song?id=1397345903'
        }
    ]

    st.image(image_arr[st.session_state['a']]['图片'], caption=image_arr[st.session_state['a']]['title'])
    st.write(image_arr[st.session_state['a']]['歌手'])
    st.write(image_arr[st.session_state['a']]['时长'])
    st.audio(image_arr[st.session_state['a']]['audio_file'])

    def next():
    # 声明a使用的是外面的全局变量a
        global a
    # 我做什么事？
        st.session_state['a'] = (st.session_state['a'] + 1) % len(image_arr)

    def prv():
        st.session_state['a'] = (st.session_state['a'] - 1) % len(image_arr)

    c1, c2 = st.columns(2)
    with c1:
        st.button('上一首', on_click=prv, use_container_width=True)
    with c2:
        st.button('下一首', on_click=next, use_container_width=True)

    with st.expander("使用说明", expanded=True):
        st.markdown("""
        ### 播放器功能说明：
        - **播放/暂停**：点击中间的播放/暂停按钮控制音乐播放
        - **切歌功能**：使用左右箭头按钮切换上一首/下一首
        - **歌曲列表**：从列表中选择任意歌曲播放（示例暂未实现，可扩展）

        ### 扩展功能规划（可实现）：
        - 实现基本的播放控制功能（真实音频播放）
        - 添加专辑封面显示（已演示，可优化样式）
        - 实现切歌功能（上一首/下一首、可扩展歌曲列表）
        - 显示歌曲信息（标题、歌手、时长，已演示）
        ### 扩展练习（可选）
        - 添加随机播放功能
        - 实现音量控制
        - 添加播放进度显示（真实关联音频时长）
        """)

    # ---- 底部标识（可选） ----
    st.markdown("""
    ---
    Streamlit音乐播放器 | 课堂练习示例 | 使用Python+Streamlit构建
    """)






    
elif selected == "南宁美食数据":
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
elif selected == "数字档案":
    st.title('学生 小陆-数字档案:sunglasses: :anchor: sixth')
    st.header('基础信息:key:')
    st.markdown('学生ID: :NEO-2023-001')
    st.markdown('注册时间: :green[2023-10-01]|精神状态: 正常')
    st.markdown('当前教室: :green[实训楼301]|安全等级: :green[绝密]')
    st.sidebar.header('技能矩阵:star: :anchor: 技能矩阵')
    c1, c2, c3 = st.columns(3)
    c1.metric(label="c语言", value="95%", delta="2%")
    c2.metric(label="python", value="87%", delta="-1%")
    c3.metric(label="java", value="68%", delta="-10%", delta_color="off")

    st.write("### Streamlit课程进度")
    st.write("*Streamlit课程进度*")
    st.subheader('***')
    st.progress(25)#Assuming 25% progress
    st.markdown('***')
    data = {
    '日期':['2023-10-01', '2023-10-05', '2023-10-12'],
    '任务':['学生数字档案', '课程管理系统', '数据图表展示'],
    '状态':['✅ 完成', '⏳ 进行中', '✖ 未完成'],
    '难度':['★★☆☆☆', '★☆☆☆☆', '★★★☆☆']
    }
    index = pd.Series([0,1,2])
    df = pd.DataFrame(data, index=index)
    st.header('任务日志:mag:')
    st.table(df)
    st.subheader('最终代码成果:lock:')
    python_code = """def matrix_branch():
        while True:
            if detect_vulnerability():
                exploit()
                return "ACCESS GRANTED"
            else:
                stealth_evade()
      
    """
    st.code(python_code, language=None)
    st.write("__________")
    st.write(">>>SYSTEM MESSAGE:下个任务目标已解锁...")
    st.write(">>>TARGET:课程管理系统")
    st.write(">>>COUNTDOWN:2025-06-04 16:55:07")
    st.write("系统状态:在线 连接状态:已加密")    
